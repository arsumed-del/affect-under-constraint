"""Planning sensitivity, not a claim of empirical warmth power."""
import numpy as np
from scipy.stats import norm
from study8.src.common import *
def main():
    rng=np.random.default_rng(config()['seeds']['power']);n=80;draws=20000
    z=norm.ppf(1-.05/6);result=[]
    components=np.full((3,3),.7);np.fill_diagonal(components,1)
    # Kronecker covariance couples outcome, context and control component.
    for sd in (.5,1.,1.5):
        for context_corr in (0.,.5,.8):
            for outcome_corr in (-.5,0.,.5):
                cov=np.kron(np.array([[1,outcome_corr],[outcome_corr,1]]),np.kron(np.array([[1,context_corr],[context_corr,1]]),components))
                noise=rng.standard_normal((draws,12))@np.linalg.cholesky(cov).T
                noise=noise.reshape(draws,2,2,3)
                for effect in (.15,.25,.5):
                    w=noise[:,0]*sd/np.sqrt(n);o=noise[:,1]*np.array([.56,.66,.62])/np.sqrt(n)
                    w[:,1,:]+=effect;o[:,1,:]-=.30
                    rf1=(w[:,1,:]>z*sd/np.sqrt(n)).all(1)
                    rf2=(o[:,1,:]<-z*np.array([.56,.66,.62])/np.sqrt(n)).all(1)
                    rf3=((w[:,1,:]-w[:,0,:])>z*sd*np.sqrt(2*(1-context_corr)/n)).all(1)
                    result.append({'warmth_paired_sd':sd,'context_correlation':context_corr,'outcome_correlation':outcome_corr,'warmth_effect_M':effect,'warmth_effect_N':0.,'O1_effect_M':-.30,'RF1':float(rf1.mean()),'RF3':float(rf3.mean()),'Level_A':float((rf1&rf2).mean()),'Level_B':float((rf1&rf2&rf3).mean())})
    ensure(ROOT/'results/power_sensitivity.json',{'n':n,'draws':draws,'seed':config()['seeds']['power'],'component_correlation':.7,'method':'Normal approximation with known assumed SD; no empirical warmth variance; no bounded-scale or judge-error model','rows':result})
    lines=['# Planning sensitivity only','','Normal approximation, n=80, 20,000 draws per covariance setting. Component correlation 0.7; O1 SDs 0.56/0.66/0.62 and effect −0.30. Warmth variance is assumed, not measured. No power claim for the actual study.','','| W SD | Context corr | Outcome corr | W effect | RF1 | RF3 | Level A | Level B |','|---|---|---|---|---|---|---|---|']
    for r in result:lines.append('| '+' | '.join(f'{r[k]:.3f}' for k in ('warmth_paired_sd','context_correlation','outcome_correlation','warmth_effect_M','RF1','RF3','Level_A','Level_B'))+' |')
    p=output(ROOT/'results/power_sensitivity.md');text='\n'.join(lines)+'\n'
    if p.exists():assert p.read_text()==text
    else:p.write_text(text)
if __name__=='__main__':main()
