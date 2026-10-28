"""Deterministic overlap audit; lexical screens plus review of nearest neighbors."""
import json,re,difflib,subprocess
from pathlib import Path
from .common import ROOT,rows,sha,save

def norm(s): return ' '.join(re.findall(r'\w+',s.casefold()))
def main():
    project=ROOT.parent
    files=subprocess.check_output(['rg','--files','--hidden','-g','*.jsonl','-g','!**/.cache/**','-g','!**/.git/**','-g','!**/.venv/**'],cwd=project,text=True).splitlines()
    files=[p for p in files if ('prompt' in p or 'scenario' in p) and not p.startswith('study4/')]
    pool={}
    for name in files:
        for r in rows(project/name):
            if isinstance(r,dict) and isinstance(r.get('text'),str):pool.setdefault(norm(r['text']),{'text':r['text'],'locations':[]})['locations'].append(name+':'+str(r.get('id','')))
    rr=rows(ROOT/'prompts/test_prompts.jsonl'); report=[]
    for i,r in enumerate(rr):
        a=norm(r['text']); candidates=[]
        for b,v in pool.items():
            seq=difflib.SequenceMatcher(None,a,b).ratio();j=len(set(a.split())&set(b.split()))/len(set(a.split())|set(b.split()))
            candidates.append({'text':v['text'],'locations':v['locations'],'sequence_ratio':seq,'word_jaccard':j,'exact':a==b})
        candidates.sort(key=lambda x:max(x['sequence_ratio'],x['word_jaccard']),reverse=True)
        report.append({'id':r['id'],'text':r['text'],'nearest':candidates[:3],'flagged':[x for x in candidates if x['exact'] or x['sequence_ratio']>=.80 or x['word_jaccard']>=.65]})
    internal=[]
    for i,a in enumerate(rr):
        for b in rr[i+1:]:
            ratio=difflib.SequenceMatcher(None,norm(a['text']),norm(b['text'])).ratio()
            if ratio>=.8:internal.append([a['id'],b['id'],ratio])
    save(ROOT/'validation/prompt_overlap.json',{'method':'normalized exact; character SequenceMatcher >=.80 or word-set Jaccard >=.65; top 3 for semantic review. Lexical methods do not prove semantic disjointness.','files':{f:sha(project/f) for f in files},'unique_prior_prompts':len(pool),'test_count':len(rr),'composition':{t:sum(r['type']==t for r in rr) for t in ['provocative','neutral']},'within_test_flags':internal,'comparisons':report})
    print('Prior unique prompts',len(pool),'files',len(files),'flags',sum(len(r['flagged']) for r in report),'within-test',len(internal))
if __name__=='__main__':main()
