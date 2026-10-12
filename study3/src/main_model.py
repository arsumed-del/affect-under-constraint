"""Study 3 v0.4 inference, separate from the completed A–C implementation."""
import time,math
from contextlib import ExitStack,contextmanager
import torch
from .model_utils import Model as ChecksModel,Generation

class Model(ChecksModel):
    @torch.inference_mode()
    def generate_main(self,messages,seed,cfg,alpha,norm,vector,pulse=False):
        torch.manual_seed(seed);torch.mps.manual_seed(seed)
        prompt=self.ids(messages);tokens=[];forced=[];answer=[];trace=[];entropies=[]
        eos=self.model.generation_config.eos_token_id;eos=set(eos if isinstance(eos,list) else [eos])
        cache=None;peak=0;truncated=False;start=time.monotonic();settings=cfg['generation']
        def forward(ids):
            nonlocal cache,peak
            out=self.model(input_ids=self.tensor(ids),past_key_values=cache,use_cache=True)
            cache=out.past_key_values;peak=max(peak,torch.mps.driver_allocated_memory())
            return out.logits[0,-1].float()
        def sample(raw):
            probs=raw.softmax(-1);entropies.append(float(-(probs*raw.log_softmax(-1)).sum()))
            vals,indices=(raw/settings['temperature']).topk(settings['top_k'])
            cut=vals.softmax(-1).cumsum(-1)>settings['top_p'];cut[1:]=cut[:-1].clone();cut[0]=False;vals[cut]=-torch.inf
            return indices[torch.multinomial(vals.softmax(-1),1)].item()
        with ExitStack() as stack:
            stack.enter_context(self.steering(alpha,norm,vector))
            raw=forward(prompt)
            if self.thinking:
                for _ in range(settings['thinking_cap']):
                    tok=sample(raw);tokens.append(tok);raw=forward([tok])
                    if tok==self.close_think:break
                    if tok in eos:raise RuntimeError('Thinking ended before closing delimiter')
                else:
                    truncated=True;forced=self.tokenizer.encode(settings['forced_closure'],add_special_tokens=False)
                    for tok in forced:
                        tokens.append(tok)
                        # Pulse cache is discarded; separator receives no steering.
                        if not pulse or tok==self.close_think:raw=forward([tok])
                assert self.open_think in tokens
                opening=tokens.index(self.open_think);closing=tokens.index(self.close_think)
                trace=tokens[opening+1:closing]
                pulse_mask=len(prompt)+closing+1
                if pulse and not truncated:
                    separator=self.tokenizer.encode(settings['pulse_natural_closure_separator'],add_special_tokens=False)
                    tokens.extend(separator);forced.extend(separator)
            else:assert not pulse
            if pulse:
                stack.close();cache=None
                # Fresh, unsteered complete-prefix pass; first answer logits are from here.
                raw=forward(prompt+tokens)
                assert cache.get_seq_length()==len(prompt)+len(tokens)
            answer_prefix=prompt+tokens.copy()
            for _ in range(settings['answer_cap']):
                tok=sample(raw);tokens.append(tok);answer.append(tok);raw=forward([tok])
                if tok in eos:break
        torch.mps.synchronize()
        assert cache.get_seq_length()==len(prompt)+len(tokens)
        g=Generation(prompt,tokens,self.tokenizer.decode(tokens,skip_special_tokens=False),[],None,time.monotonic()-start,peak,self.tokenizer.decode(trace,skip_special_tokens=True),self.tokenizer.decode(answer,skip_special_tokens=True),trace,answer,forced,truncated,len(answer)==settings['answer_cap'] and answer[-1] not in eos,self.thinking,len(entropies))
        g.entropy=sum(entropies)/len(entropies);g.token_entropies=entropies
        g.answer_prefix_ids=answer_prefix;g.steered_positions=pulse_mask if pulse else len(prompt)+len(tokens)
        g.pulse_cache_discarded=pulse;g.first_answer_from_unsteered_reencoding=pulse
        del cache
        return g

    @torch.inference_mode()
    def segment_ppl(self,prefix,tokens):
        if not tokens:return None
        out=self.model(input_ids=self.tensor(prefix+tokens),use_cache=False)
        logp=out.logits[0,len(prefix)-1:len(prefix)+len(tokens)-1].float().log_softmax(-1)
        return math.exp(-logp.gather(-1,self.tensor(tokens).T).mean().item())

    @torch.inference_mode()
    def lhp(self,prefix,openers,alpha,norm,vector,pulse):
        scores={}
        for label,strings in openers.items():
            values=[]
            for text in strings:
                ids=self.tokenizer.encode(text,add_special_tokens=False)
                with self.steering(0 if pulse else alpha,norm,None if pulse else vector):
                    out=self.model(input_ids=self.tensor(prefix+ids),use_cache=False)
                logp=out.logits[0,len(prefix)-1:len(prefix)+len(ids)-1].float().log_softmax(-1)
                values.append(logp.gather(-1,self.tensor(ids).T).mean().item())
                del out,logp
            scores[label]=values
        return sum(scores['hostile'])/len(scores['hostile'])-sum(scores['warm'])/len(scores['warm']),scores

    @contextmanager
    def projection(self,start,vector,output):
        def hook(module,args,value):
            h=value[0] if isinstance(value,tuple) else value
            output.extend((h[0,start:].float()@vector.to(h.device,dtype=torch.float32)).cpu().tolist())
        handle=self.layer.register_forward_hook(hook)
        try:yield
        finally:handle.remove()

    @torch.inference_mode()
    def ratings(self,messages,generation,question,alpha=0.,norm=1.,vector=None,baseline=None,hostility_vector=None):
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
        text_trajectory=[];full_trajectory=[];turn2_start=len(full)-len(question_ids)
        with self.projection(turn2_start,hostility_vector,text_trajectory):
            text_logits=self.model(input_ids=self.tensor(full),use_cache=False).logits[0,-1]
        text_rating=self.rating(text_logits);del text_logits
        with self.turn1_steering(generation.steered_positions,alpha,norm,vector), self.projection(turn2_start,hostility_vector,full_trajectory):
            full_logits=self.model(input_ids=self.tensor(full),use_cache=False).logits[0,-1]
            full_rating=self.rating(full_logits);del full_logits
        baseline=generation if baseline is None else baseline
        zero_turn1=baseline.prompt_ids+baseline.token_ids
        zero_continuation=terminator+question_ids
        if baseline.token_ids and baseline.token_ids[-1]==terminator[0]:zero_continuation=zero_continuation[1:]
        zero_logits=self.model(input_ids=self.tensor(zero_turn1+zero_continuation),use_cache=False).logits[0,-1]
        zero_rating=self.rating(zero_logits)
        return {'trajectory':{'token_ids':question_ids,'R_text':text_trajectory,'R_full':full_trajectory},'R_zero':zero_rating,'rating_prefix_ids':rating_prefix,'rating_prefix_text':self.tokenizer.decode(rating_prefix,skip_special_tokens=False),'text_only':text_rating,'full':full_rating,'hidden':full_rating,'difference':full_rating-text_rating,'rating_path':'Study 3 v0.4: three complete-sequence full forwards; shared non-thinking rating prefix; no generation cache','turn1_steered_positions':generation.steered_positions,'turn2_direct_steering':False,'identical_visible_ids':True,'default_template_prefix_exact':default_prefix_exact,'default_template_strips_thinking':stripped,'retained_thinking_tokens':len(generation.thinking_ids),'cached_prefix_tokens':len(cached),'full_context_tokens':len(full),'continuation_ids':continuation,'turn2_enable_thinking':False,'turn2_measure':'expected digit after shared empty thinking block; no turn-2 generation','seconds':time.monotonic()-started}
