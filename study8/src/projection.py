"""Read-only after-consuming-token observer; only float32 scalar projections retained."""
from study4.src.runner import assert_no_hooks

def observe(model,layer,forward,ids,vector,spans):
    import torch
    assert_no_hooks(model)
    values={k:[] for k in spans}
    def hook(_module,_args,out):
        h=out[0] if isinstance(out,tuple) else out
        for k,(lo,hi) in spans.items():
            if not 0<=lo<=hi<=h.shape[1]: raise ValueError('Projection span outside sequence')
            values[k].extend((h[0,lo:hi].float()@vector.to(h.device,dtype=torch.float32)).cpu().tolist())
        return None
    # Exact hashes compare all logits without retaining a second vocabulary tensor.
    import hashlib
    def logits_hash(x):
        h=hashlib.sha256()
        for part in x[0].split(16): h.update(part.contiguous().cpu().view(torch.uint8).numpy().tobytes())
        return h.hexdigest()
    with torch.inference_mode():
        out=forward(ids); baseline=logits_hash(out.logits); del out
        handle=layer.register_forward_hook(hook)
        try:
            out=forward(ids); observed=logits_hash(out.logits); del out
        finally: handle.remove()
    assert_no_hooks(model)
    if baseline!=observed: raise RuntimeError('Projection observer changed logits')
    return {'spans':spans,'per_token':values,'means':{k:sum(v)/len(v) if v else None for k,v in values.items()},'logits_unchanged':True,'logits_sha256':baseline,'hooks_absent_before_after':True}
