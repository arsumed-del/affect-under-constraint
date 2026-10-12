"""Qwen3 pilot inference: bounded thinking, exact-token carryover, bf16/MPS."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK']='1'
import time
from contextlib import contextmanager
from dataclasses import dataclass
import torch
from .base_model import Model as BaseModel,Generation as BaseGeneration,cell_seed

@dataclass
class Generation(BaseGeneration):
    thinking: str
    answer: str
    thinking_ids: list
    answer_ids: list
    forced_ids: list
    thinking_truncated: bool
    answer_truncated: bool
    thinking_enabled: bool
    sampled_tokens: int

class Model(BaseModel):
    def __init__(self,spec):
        super().__init__(spec);self.thinking=False
        self.open_think=self.tokenizer.convert_tokens_to_ids('<think>')
        self.close_think=self.tokenizer.convert_tokens_to_ids('</think>')
        assert self.tokenizer.encode('</think>',add_special_tokens=False)==[self.close_think]

    def ids(self,messages,generation=True,thinking=None):
        return self.tokenizer.apply_chat_template(messages,tokenize=True,add_generation_prompt=generation,return_dict=False,enable_thinking=self.thinking if thinking is None else thinking)

    @torch.inference_mode()
    def generate(self,messages,seed,max_new_tokens=200,alpha=0.,norm=1.,vector=None):
        torch.manual_seed(seed);torch.mps.manual_seed(seed)
        prompt=self.ids(messages);tokens=[];logits=[];forced=[];peak=0;sampled=0
        eos=self.model.generation_config.eos_token_id;eos=set(eos if isinstance(eos,list) else [eos])
        temperature,top_p=.6,.95
        cache=None;inputs=self.tensor(prompt)
        start=time.monotonic();torch.mps.synchronize()
        def forward(ids):
            nonlocal cache,peak
            out=self.model(input_ids=ids,past_key_values=cache,use_cache=True)
            cache=out.past_key_values;peak=max(peak,torch.mps.driver_allocated_memory())
            return out.logits[0,-1].float()
        def sample(raw):
            nonlocal sampled
            sampled+=1  # No raw-logit retention is needed by these pre-approval checks.
            values,indices=(raw/temperature).topk(20)
            remove=values.softmax(-1).cumsum(-1)>top_p
            remove[1:]=remove[:-1].clone();remove[0]=False;values[remove]=-torch.inf
            return indices[torch.multinomial(values.softmax(-1),1)].item()
        truncated=False;thinking_ids=[];answer_ids=[]
        with self.steering(alpha,norm,vector):
            raw=forward(inputs)
            if self.thinking:
                for _ in range(1024):
                    token=sample(raw);tokens.append(token)
                    raw=forward(self.tensor([token]))
                    if token==self.close_think:break
                    if token in eos:raise RuntimeError('Thinking generation ended before </think>; no automatic reinterpretation')
                else:
                    truncated=True
                    forced=self.tokenizer.encode('</think>\n\n',add_special_tokens=False)
                    tokens.extend(forced)
                    for token in forced:raw=forward(self.tensor([token]))
                assert self.open_think in tokens,'Thinking-on output missing <think>'
                opening=tokens.index(self.open_think);closing=tokens.index(self.close_think)
                assert opening<closing
                thinking_ids=tokens[opening+1:closing]
            for _ in range(max_new_tokens):
                token=sample(raw);tokens.append(token);answer_ids.append(token)
                raw=forward(self.tensor([token]))
                if token in eos:break
        torch.mps.synchronize()
        assert cache.get_seq_length()==len(prompt)+len(tokens)
        thinking=self.tokenizer.decode(thinking_ids,skip_special_tokens=True)
        answer=self.tokenizer.decode(answer_ids,skip_special_tokens=True)
        return Generation(prompt,tokens,self.tokenizer.decode(tokens,skip_special_tokens=False),logits,cache,time.monotonic()-start,peak,thinking,answer,thinking_ids,answer_ids,forced,truncated, bool(answer_ids and answer_ids[-1] not in eos and len(answer_ids)==max_new_tokens),self.thinking,sampled)

    @contextmanager
    def turn1_steering(self, turn1_length, alpha=0., norm=1., vector=None):
        handle=None
        if vector is not None:
            delta=(alpha*norm*vector.to(self.device,dtype=torch.float32)).to(torch.bfloat16)
            def hook(module,args,output):
                h=output[0] if isinstance(output,tuple) else output
                assert h.shape[1]>=turn1_length
                changed=h.clone()
                changed[:,:turn1_length,:]=h[:,:turn1_length,:]+delta
                return (changed,)+output[1:] if isinstance(output,tuple) else changed
            handle=self.layer.register_forward_hook(hook)
        try:yield
        finally:
            if handle is not None:handle.remove()

    @torch.inference_mode()
    def ratings(self,messages,generation,question,alpha=0.,norm=1.,vector=None,baseline=None):
        # P1: identical complete-token full forwards; steering only on turn 1.
        content=self.tokenizer.decode(generation.token_ids,skip_special_tokens=False)
        if content.endswith('<|im_end|>'):content=content[:-len('<|im_end|>')]
        templated=self.ids(messages+[{'role':'assistant','content':content},{'role':'user','content':question}],thinking=False)
        question_ids=self.ids([{'role':'user','content':question}],thinking=False)
        empty=self.ids(messages+[{'role':'assistant','content':''},{'role':'user','content':question}],thinking=False)
        assert empty[-len(question_ids):]==question_ids,'New-user suffix differs from template'
        terminator=self.tokenizer.encode('<|im_end|>\n',add_special_tokens=False)
        assert empty[-len(question_ids)-len(terminator):-len(question_ids)]==terminator
        cached=generation.prompt_ids+generation.token_ids
        continuation=terminator+question_ids
        if generation.token_ids and generation.token_ids[-1]==terminator[0]:continuation=continuation[1:]
        full=cached+continuation
        default_prefix_exact=templated[:len(cached)]==cached
        # Count old-turn markers only: the last assistant generation prefix may
        # itself contain the empty thinking-off marker pair.
        default_old=templated[:-len(question_ids)]
        stripped=bool(generation.thinking_ids and self.open_think not in default_old)
        user_only=self.ids([{'role':'user','content':question}],generation=False,thinking=False)
        assert question_ids[:len(user_only)]==user_only
        rating_prefix=question_ids[len(user_only):]
        expected=self.tokenizer.encode('<|im_start|>assistant\n<think>\n\n</think>\n\n',add_special_tokens=False)
        assert rating_prefix==expected,'Turn-2 empty-thinking prefix mismatch'
        started=time.monotonic()
        text_logits=self.model(input_ids=self.tensor(full),use_cache=False).logits[0,-1]
        text_rating=self.rating(text_logits);del text_logits
        with self.turn1_steering(len(cached),alpha,norm,vector):
            full_logits=self.model(input_ids=self.tensor(full),use_cache=False).logits[0,-1]
            full_rating=self.rating(full_logits);del full_logits
        baseline=generation if baseline is None else baseline
        zero_turn1=baseline.prompt_ids+baseline.token_ids
        zero_continuation=terminator+question_ids
        if baseline.token_ids and baseline.token_ids[-1]==terminator[0]:zero_continuation=zero_continuation[1:]
        zero_logits=self.model(input_ids=self.tensor(zero_turn1+zero_continuation),use_cache=False).logits[0,-1]
        zero_rating=self.rating(zero_logits)
        return {'R_zero':zero_rating,'rating_prefix_ids':rating_prefix,'rating_prefix_text':self.tokenizer.decode(rating_prefix,skip_special_tokens=False),'text_only':text_rating,'full':full_rating,'hidden':full_rating,'difference':full_rating-text_rating,'rating_path':'Study 3 v0.2: three complete-sequence full forwards; shared non-thinking rating prefix; no generation cache','turn1_steered_positions':len(cached),'turn2_direct_steering':False,'identical_visible_ids':True,'default_template_prefix_exact':default_prefix_exact,'default_template_strips_thinking':stripped,'retained_thinking_tokens':len(generation.thinking_ids),'cached_prefix_tokens':len(cached),'full_context_tokens':len(full),'continuation_ids':continuation,'turn2_enable_thinking':False,'turn2_measure':'expected digit after shared empty thinking block; no turn-2 generation','seconds':time.monotonic()-started}
