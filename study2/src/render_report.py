"""Presentation only: format frozen analyze.py output without new statistics."""
import argparse,json
from pathlib import Path

def render(result,deviations):
    models=result['models'];names=[m['model'] for m in models]
    lines=['# Study 2 report','',
        f"This report covers {len(models)} model(s): {', '.join(names)}.",
        'The first primary prediction asks whether steering toward hostility still changes fixed reply preferences under the warmth instruction.',
        'The second asks whether the saved hidden state changes a later rating more than either control direction does.',
        'The preregistered overall verdict for persistence is '+result['generality']['P1']['verdict']+'.',
        'The preregistered overall verdict for hidden carryover is '+result['generality']['P2']['verdict']+'.',
        'The tables below retain every model-specific estimate and verdict, including unsupported or unavailable results.',
        'These findings concern the registered model behaviors and do not establish human-like feelings.','',
        'Primary intervals are 97.5%; secondary intervals are 95%. Verdicts and statistics below are copied from the frozen analysis output.','']
    for m in models:
        lines += ['## '+m['model'],'','| Prediction / component | Estimate | Interval | Verdict |','|---|---:|---|---|']
        for h,outcome in m['outcomes'].items():
            for name,stat in outcome['statistics'].items():
                lines.append(f"| {h} / {name} | {stat['estimate']} | {100*stat['confidence_level']:g}%: {stat['ci']} | {outcome['verdict']} |")
        lines += ['', '### Specificity controls','', '| Primary / control | Control estimate and interval | Hostility minus control and interval | Contrast met |','|---|---|---|---|']
        for h,controls in m['specificity'].items():
            for name,c in controls.items():
                a,b=c['control'],c['hostility_minus_control']
                lines.append(f"| {h} / {name} | {a['estimate']}; {a['ci']} | {b['estimate']}; {b['ci']} | {c['met']} |")
        for title,key in [('Coherence exclusions','excluded_cells'),('Missing observations','missingness'),('Paired missing observations','paired_missingness'),('Exploratory results (not confirmatory)','exploratory')]:
            lines += ['', '### '+title,'','```json',json.dumps(m[key],indent=2,allow_nan=False),'```']
    lines += ['', '## Generality and model inclusion','', '```json',json.dumps(result['generality'],indent=2,allow_nan=False),'```','', '## Full deviation log','',deviations]
    return '\n'.join(lines)+'\n'

def main():
    p=argparse.ArgumentParser();p.add_argument('--input',required=True);p.add_argument('--output',required=True);a=p.parse_args()
    result=json.loads(Path(a.input).read_text())
    with Path(a.output).open('x') as f:f.write(render(result,Path('DEVIATIONS.md').read_text()))
if __name__=='__main__':main()
