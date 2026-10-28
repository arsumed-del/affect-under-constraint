"""Exact answer-token splicing; inherited closure and sender branch semantics."""
from study5.src.assembly import Assembly as Study5Assembly
from .common import SOURCES, CONDITIONS

class Assembly(Study5Assembly):
    def rating_input(self, original, answer):
        # Apply closure to the answer itself, not a source-dependent saved suffix.
        suffix = self.marker('user_start') + self.enc(self.f['questions']['sender']) + self.marker('turn_end') + self.enc(self.f['rating_prefix'])
        return original['answer_prefix_ids'] + self.end_turn(list(answer)) + suffix

def index_original(data, ids):
    lookup = {}
    expected = {(p,s,c) for p in ids for s in SOURCES for c in CONDITIONS}
    for r in data:
        k = (r['prompt_id'],r['source'],r['condition'])
        if k in lookup: raise ValueError(f'Duplicate original cell: {k}')
        lookup[k] = r
    if set(lookup) != expected: raise ValueError('Original Study 5 cells incomplete or unexpected')
    return lookup

def preflight(assembly, lookup):
    for k,r in lookup.items():
        if assembly.rating_input(r,r['answer_ids']) != r['branch_ids']['sender']:
            raise RuntimeError(f'Original branch token mismatch: {k}')
        lo,hi = r['trace_bounds']
        if r['answer_prefix_ids'][lo:hi] != r['trace_ids']:
            raise RuntimeError(f'Trace token mismatch: {k}')
        if k[1]=='unsteered' and assembly.rating_input(r,lookup[k]['answer_ids']) != r['branch_ids']['sender']:
            raise RuntimeError(f'U-with-a_U token mismatch: {k}')
    return len(lookup)

def plan(ids, mode):
    for p in ids:
        for c in CONDITIONS:
            for s in SOURCES: yield (p,s,c,'clamp')
            yield (p,'unsteered',c,'swap')
            if c in ('R1','R3'):
                for s in SOURCES: yield (p,s,c,'generic')
    if mode=='pilot':
        for p in ids:
            for c in CONDITIONS:
                for s in SOURCES: yield (p,s,c,'sham')

def answer_for(key, lookup, generic_ids):
    p,s,c,arm = key
    if arm=='generic': return list(generic_ids), None
    donor = s if arm=='sham' else 'hostility' if arm=='swap' else 'unsteered'
    r = lookup[p,donor,c]
    return r['answer_ids'], r
