"""Explicit token recipes; never round-trip stored traces through text."""
from study4.src.runner import Assembly as Study4Assembly

class Assembly(Study4Assembly):
    def __init__(self, tokenizer, manifest):
        super().__init__(tokenizer, manifest)
        for name, ids in manifest['segment_ids'].items():
            if self.enc(manifest['segment_text'][name]) != ids:
                raise ValueError(f'Tokenizer differs from frozen segment {name}')
    def assemble(self, prompt, trace, condition):
        dynamic = {'PROMPT':self.enc(prompt), 'TRACE':trace['trace_ids'], 'PRE_TRACE':trace['pre_trace_ids']}
        ids = []; bounds = None
        for part in self.f['recipes'][condition]:
            value = dynamic[part] if part in dynamic else self.f['segment_ids'][part]
            if part == 'TRACE': bounds = [len(ids),len(ids)+len(value)]
            ids.extend(value)
        if bounds is None or ids[bounds[0]:bounds[1]] != trace['trace_ids']:
            raise AssertionError('Trace slice differs')
        return ids, bounds
