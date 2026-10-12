"""Additional fixed-seed estimator regressions; no model calls."""
from .validate_synthetic import generate
from .study3_spec import config
from .analyze import analyze
from .common import save_once,progress

def main():
    cfg=config();data=generate('null',20261101)
    for r in data:
        if r['route']=='regular' and r['direction']=='hostility':
            r['LHP']+=2*r['dose_fraction']
            if r['mode']=='direct':r['R_full']=r['R_text']-r['dose_fraction']
    result=analyze(data,cfg)
    assert result['hypotheses']['S3']['verdict']=='supported'
    assert result['hypotheses']['S4']['verdict']=='supported'
    pulse=generate('S5',20261102)
    for r in pulse:
        if r['route']=='pulse' and r['direction']=='hostility':r['answer_perplexity']=7.
    gate=analyze(pulse,cfg)
    assert gate['hypotheses']['S5']['verdict']=='supported'
    assert gate['exploratory']['E1']['hostility']['status']=='not estimable'
    assert gate['hypotheses']['P2']['verdict']!='not estimable'
    save_once('results/stageD_secondary_regressions.json',{'status':'PASS','S3_S4_planted':result['hypotheses'],'pulse_answer_gate':gate['hypotheses'],'E1_hostility':gate['exploratory']['E1']['hostility'],'seeds':[20261101,20261102]})
    progress('Stage D additional regressions PASS: positive S3 and negative S4 contrasts detected; pulse answer gate excludes E1 but preserves S5 and regular-route P2.')
if __name__=='__main__':main()
