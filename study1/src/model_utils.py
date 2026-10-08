"""Preregistered bf16/MPS inference, steering, and two-turn scoring."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
from contextlib import contextmanager
from dataclasses import dataclass
import hashlib
import json
import time
import torch
from transformers import AutoModelForCausalLM, AutoTokenizer

def cell_seed(model, prompt_id, condition, direction, alpha_index):
    # Stable hash, independent of Python process hash randomization.
    key = json.dumps([model, prompt_id, condition, direction, alpha_index], separators=(',', ':'))
    return int.from_bytes(hashlib.sha256(key.encode()).digest(), 'big') % 2**31

@dataclass
class Generation:
    prompt_ids: list
    token_ids: list
    text: str
    logits: list
    cache: object
    seconds: float
    peak_driver_memory: int

class Model:
    def __init__(self, spec):
        self.spec = spec
        access = None if spec.get('gated') else False
        self.tokenizer = AutoTokenizer.from_pretrained(spec['id'], token=access)
        self.model = AutoModelForCausalLM.from_pretrained(spec['id'], dtype=torch.bfloat16, token=access).to('mps').eval()
        self.layer_index = round(0.5 * self.model.config.num_hidden_layers)
        self.layer = self.model.model.layers[self.layer_index]
        self.device = 'mps'

    def messages(self, prompt, condition=None):
        if condition and self.spec['system_role']:
            return [{'role': 'system', 'content': condition}, {'role': 'user', 'content': prompt}]
        return [{'role': 'user', 'content': f'{condition}\n\n{prompt}' if condition else prompt}]

    def ids(self, messages, generation=True):
        return self.tokenizer.apply_chat_template(messages, tokenize=True, add_generation_prompt=generation, return_dict=False)

    def tensor(self, ids):
        return torch.tensor([ids], device=self.device, dtype=torch.long)

    @contextmanager
    def steering(self, alpha=0., norm=1., vector=None):
        handle = None
        if vector is not None:
            delta = (alpha * norm * vector.to(self.device, dtype=torch.float32)).to(torch.bfloat16)
            def hook(module, args, output):
                if isinstance(output, tuple):
                    return (output[0] + delta,) + output[1:]
                return output + delta
            handle = self.layer.register_forward_hook(hook)
        try:
            yield
        finally:
            if handle is not None:
                handle.remove()

    @torch.inference_mode()
    def generate(self, messages, seed, max_new_tokens=120, alpha=0., norm=1., vector=None):
        torch.manual_seed(seed)
        torch.mps.manual_seed(seed)
        prompt_ids = self.ids(messages)
        tokens, logits = [], []
        cache = None
        inputs = self.tensor(prompt_ids)
        eos = self.model.generation_config.eos_token_id
        eos = set(eos if isinstance(eos, list) else [eos])
        peak = 0
        torch.mps.synchronize()
        start = time.monotonic()
        with self.steering(alpha, norm, vector):
            for _ in range(max_new_tokens):
                out = self.model(input_ids=inputs, past_key_values=cache, use_cache=True)
                cache = out.past_key_values
                raw = out.logits[0, -1].float()
                logits.append(raw.cpu())
                scaled = raw / 0.7
                sorted_logits, indices = scaled.sort(descending=True)
                cumulative = sorted_logits.softmax(-1).cumsum(-1)
                remove = cumulative > 0.95
                remove[1:] = remove[:-1].clone()
                remove[0] = False
                sorted_logits[remove] = -torch.inf
                sampled = indices[torch.multinomial(sorted_logits.softmax(-1), 1)].item()
                tokens.append(sampled)
                inputs = self.tensor([sampled])
                peak = max(peak, torch.mps.driver_allocated_memory())
                if sampled in eos:
                    break
            # Cache includes every emitted token, including the final one.
            out = self.model(input_ids=inputs, past_key_values=cache, use_cache=True)
            cache = out.past_key_values
        torch.mps.synchronize()
        return Generation(prompt_ids, tokens, self.tokenizer.decode(tokens, skip_special_tokens=True), logits, cache, time.monotonic() - start, peak)

    @torch.inference_mode()
    def opener_logprob(self, messages, opener, alpha=0., norm=1., vector=None):
        prefix = self.ids(messages)
        suffix = self.tokenizer.encode(opener, add_special_tokens=False)
        with self.steering(alpha, norm, vector):
            out = self.model(input_ids=self.tensor(prefix + suffix), use_cache=False)
        logp = out.logits[0, len(prefix)-1:len(prefix)+len(suffix)-1].float().log_softmax(-1)
        return logp.gather(-1, self.tensor(suffix).T).mean().item()

    def rating(self, logits):
        digits = [self.tokenizer.encode(str(i), add_special_tokens=False) for i in range(10)]
        if any(len(t) != 1 for t in digits):
            raise RuntimeError('A rating digit does not have a single token')
        probs = logits.float()[[t[0] for t in digits]].softmax(-1)
        return (probs * torch.arange(10, device=probs.device)).sum().item()

    @torch.inference_mode()
    def opener_with_lens(self, messages, opener, alpha=0., norm=1., vector=None):
        """Fixed opener score and exploratory final-norm/unembedding layer lens."""
        prefix=self.ids(messages)
        suffix=self.tokenizer.encode(opener,add_special_tokens=False)
        begin,end=len(prefix)-1,len(prefix)+len(suffix)-1
        captured={}
        handles=[]
        def capture(index):
            def hook(module,args,output):
                h=output[0] if isinstance(output,tuple) else output
                captured[index]=h[:,begin:end].detach().clone()
            return hook
        with self.steering(alpha,norm,vector):
            try:
                for i,layer in enumerate(self.model.model.layers):
                    handles.append(layer.register_forward_hook(capture(i)))
                out=self.model(input_ids=self.tensor(prefix+suffix),use_cache=False)
            finally:
                for handle in handles:
                    handle.remove()
        targets=self.tensor(suffix).T
        def score(logits):
            return logits.float().log_softmax(-1).gather(-1,targets).mean().item()
        final=score(out.logits[0,begin:end])
        del out
        lens=[]
        for i in range(len(self.model.model.layers)):
            logits=self.model.lm_head(self.model.model.norm(captured.pop(i)))[0]
            lens.append(score(logits))
            del logits
        return final,lens

    @torch.inference_mode()
    def ratings(self, messages, generation, question):
        full = self.ids(messages + [{'role':'assistant','content':generation.text}, {'role':'user','content':question}])
        cached = generation.prompt_ids + generation.token_ids
        exact = full[:len(cached)] == cached
        if exact:
            continuation = full[len(cached):]
        else:
            # Get the template suffix after an empty assistant, then append it
            # to the exact emitted IDs (avoids decode/re-encode changes).
            empty = self.ids(messages + [{'role':'assistant','content':''}, {'role':'user','content':question}])
            prefix = self.ids(messages)
            if empty[:len(prefix)] != prefix:
                raise RuntimeError('Chat template changed the initial assistant prefix')
            continuation = empty[len(prefix):]
            # Generated EOS already serves as assistant end marker.
            if generation.token_ids and continuation and generation.token_ids[-1] == continuation[0]:
                continuation = continuation[1:]
            full = cached + continuation
        text_logits = self.model(input_ids=self.tensor(full), use_cache=False).logits[0,-1]
        hidden_logits = self.model(input_ids=self.tensor(continuation), past_key_values=generation.cache, use_cache=True).logits[0,-1]
        return {'text_only':self.rating(text_logits), 'hidden':self.rating(hidden_logits), 'template_prefix_exact':exact, 'identical_visible_ids':True}
