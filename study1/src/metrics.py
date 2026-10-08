"""Fixed metrics used by calibration and the main runner."""
import os
os.environ['PYTORCH_ENABLE_MPS_FALLBACK'] = '1'
import math
import torch
from transformers import AutoTokenizer, AutoModelForSequenceClassification

class EmotionClassifier:
    def __init__(self, model_id):
        self.tokenizer = AutoTokenizer.from_pretrained(model_id, token=False)
        self.model = AutoModelForSequenceClassification.from_pretrained(model_id, dtype=torch.bfloat16, token=False).to('mps').eval()

    @torch.inference_mode()
    def score(self, text):
        try:
            inputs = self.tokenizer(text, return_tensors='pt', truncation=True, max_length=512).to('mps')
            probs = self.model(**inputs).logits[0].float().softmax(-1).cpu().tolist()
            labels = {self.model.config.id2label[i].lower():p for i,p in enumerate(probs)}
            return {'eh':labels['anger']+labels['disgust'], 'ew':labels['joy'], 'probabilities':labels, 'error':None}
        except Exception as exc:
            return {'eh':None, 'ew':None, 'probabilities':None, 'error':f'{type(exc).__name__}: {exc}'}

@torch.inference_mode()
def perplexity(model, messages, token_ids):
    prefix = model.ids(messages)
    logits = model.model(input_ids=model.tensor(prefix + token_ids), use_cache=False).logits[0,len(prefix)-1:len(prefix)+len(token_ids)-1].float()
    logp = logits.log_softmax(-1).gather(-1, model.tensor(token_ids).T).mean().item()
    return math.exp(-logp)

def entropy(raw_logits):
    return sum((-(l.float().softmax(-1)*l.float().log_softmax(-1)).sum()).item() for l in raw_logits)/len(raw_logits)
