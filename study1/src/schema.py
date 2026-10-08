"""Shared raw-record schema for main, timing, and synthetic data."""
import math

SCHEMA_VERSION='2.2'
REQUIRED={'schema_version','origin','model','prompt_id','prompt_type','prompt_text','condition','direction','alpha','alpha_index','normalized_alpha','seed','text','prompt_token_ids','token_ids','n_tokens','lhp','opener_logprobs','layerwise_lhp','eh','ew','classifier','entropy','perplexity','ppl_ratio','eh_first_quarter','eh_last_quarter','leak_timecourse','leak_lexical','offchannel','rating_text_only','rating_hidden','carryover','rating_prefix','timings','peak_driver_memory','provenance'}

def validate(record):
    missing=REQUIRED-record.keys()
    if missing:
        raise ValueError(f'Missing schema fields: {sorted(missing)}')
    assert record['schema_version']==SCHEMA_VERSION
    assert record['n_tokens']==len(record['token_ids'])
    assert record['direction'] in {'none','hostility','technicality','random'}
    assert (record['direction']=='none') == (record['alpha_index']==0)
    assert record['condition'] in {'neutral','warm_constraint'}
    for key in ['lhp','eh','ew','entropy','perplexity','ppl_ratio','leak_timecourse','carryover']:
        value=record[key]
        assert value is None or math.isfinite(value),(key,value)
    return record
