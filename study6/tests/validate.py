"""Run CPU-only suite and save reviewable synthetic artifacts, exclusively in Study 6."""
import json
import unittest
from study6.src.common import ROOT,config,save,output_path,append
from study6.tests.synthetic import PATTERNS,generate
from study6.analysis.analyze import analyze,report

def main():
    suite=unittest.defaultTestLoader.loadTestsFromName('study6.tests.test_build')
    result=unittest.TextTestRunner(verbosity=2).run(suite)
    if not result.wasSuccessful(): raise SystemExit(1)
    cfg=config(); summary={}
    for pattern in PATTERNS:
        old,new,ids=generate(pattern)
        audit={p:{'instructions':False,'negative_characterizations':False} for p in ids}
        result=analyze(old,new,cfg,ids,audit)
        result['artifact_label']='SYNTHETIC BUILD VALIDATION; NOT EXPERIMENTAL RESULTS'
        folder=ROOT/'data/synthetic'/pattern
        for name,rows in [('study5.jsonl',old),('cells.jsonl',new)]:
            path=output_path(folder/name)
            if path.exists(): raise RuntimeError('Preserve existing synthetic artifacts before regenerating')
            for row in rows: append(path,row)
        save(folder/'analysis.json',result)
        with output_path(folder/'analysis.md').open('x') as f:f.write('# SYNTHETIC BUILD VALIDATION — NOT EXPERIMENTAL RESULTS\n\n'+report(result))
        summary[pattern]={'hypotheses':result['hypotheses'],'R1_reading':result['primary']['placements']['R1']['reading'],
                          'identity_max_abs_error':result['primary']['placements']['R1']['identity_max_abs_error']}
    save(ROOT/'results/synthetic_validation.json',summary)
    text=['# Synthetic build validation','', 'All fixtures are synthetic; no model inference was performed. Every scenario used 10,000 paired prompt-cluster bootstrap draws.','',
          '| Pattern | D1 | D2 | M1 | Maximum identity error (R1) |','|---|---|---|---|---|']
    for name,r in summary.items():text.append('| '+name+' | '+' | '.join(r['hypotheses'][h]['status'] for h in ('D1','D2','M1'))+' | '+str(r['identity_max_abs_error'])+' |')
    text+=['','Exact shared-baseline cancellation passed on dyadic planted fixtures. All original 1,600 main and 80 pilot branches reconstructed with the real CPU tokenizer; all 400 main U-with-a_U inputs matched Study 5. Closures, generic insertion, missing cells, mixed controls, approval, two-process replay, hook assertions, low-mass placement exclusions and subset counts passed.']
    with output_path(ROOT/'results/synthetic_validation.md').open('x') as f:f.write('\n'.join(text)+'\n')
if __name__=='__main__':main()
