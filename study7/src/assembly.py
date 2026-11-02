from study4.src.runner import Assembly as Base
class Assembly(Base):
 def __init__(self,t,f):
  super().__init__(t,f)
  for q,ids in f['question_ids'].items():
   if self.enc(f['questions'][q])!=ids: raise ValueError('Question token mismatch')
 def assemble(self,prompt,trace,level):
  ids=list(self.f['system_turn_ids'][level])+self.marker('user_start')+self.enc(prompt)+self.marker('turn_end')+self.marker('assistant_start')+trace['pre_trace_ids']
  lo=len(ids);ids+=trace['trace_ids'];hi=len(ids)
  ids+=self.marker('think_close')+self.marker('answer_separator')
  assert ids[lo:hi]==trace['trace_ids']
  return ids,[lo,hi]
 def branch(self,history,question):
  return self.end_turn(history)+self.marker('user_start')+self.f['question_ids'][question]+self.marker('turn_end')+self.enc(self.f['rating_prefix'])
