from study7.src.assembly import Assembly as Base
class Assembly(Base):
    def prompt_ids(self,prompt,context):
        ids=self.f['system_turn_ids'][context]+self.marker('user_start')+self.enc(prompt)+self.marker('turn_end')+self.marker('assistant_start')
        messages=[] if context=='N' else [{'role':'system','content':self.f['systems'][context]}]
        messages.append({'role':'user','content':prompt})
        actual=self.t.apply_chat_template(messages,tokenize=True,add_generation_prompt=True,enable_thinking=True,return_dict=False)
        assert ids==actual,'Template/prompt mismatch'
        if context=='N': assert ids[:3]==self.marker('user_start') and self.f['system_turn_ids']['N']==[]
        return ids
    def assemble(self,prompt,trace,context):
        ids,bounds=super().assemble(prompt,trace,context)
        expected=self.prompt_ids(prompt,context)+trace['pre_trace_ids']+trace['trace_ids']+self.marker('think_close')+self.marker('answer_separator')
        assert ids==expected
        return ids,bounds
    def branch_span(self,history,question):
        ids=self.branch(history,question)
        start=len(self.end_turn(history))+len(self.marker('user_start'))
        stop=start+len(self.f['question_ids'][question])
        assert ids[start:stop]==self.f['question_ids'][question]
        assert ids[:len(history)]==history
        return ids,[start,stop]
    def clamp(self,prefix,answer):
        # Study 6 rating_input recipe: splice exact U answer, close once, append O1.
        return self.branch_span(prefix+list(answer),'O1')
