"""Offline public-deposit verification test; no author approval is fabricated."""
import hashlib,io,json,zipfile
from unittest.mock import patch
from .autopilot import verify_public_deposit
from .common import save_once

def main():
    prereg=b'synthetic preregistration bytes';config=b'synthetic config bytes'
    local={'doi':'10.5281/zenodo.123','prereg_sha256':hashlib.sha256(prereg).hexdigest(),'config_sha256':hashlib.sha256(config).hexdigest()}
    buffer=io.BytesIO()
    with zipfile.ZipFile(buffer,'w') as z:z.writestr('study2/PREREG.md',prereg);z.writestr('study2/config.yaml',config)
    payload=buffer.getvalue()
    record={'id':123,'doi':local['doi'],'submitted':True,'files':[{'key':'study2.zip','checksum':'md5:'+hashlib.md5(payload).hexdigest(),'links':{'self':'https://zenodo.org/synthetic-file'}}]}
    with patch('urllib.request.urlopen',side_effect=[io.BytesIO(json.dumps(record).encode()),io.BytesIO(payload)]):
        result=verify_public_deposit(local)
        assert set(result['verified_specification_files'])=={'PREREG.md','config.yaml'}
    wrong=dict(local,config_sha256='0'*64)
    with patch('urllib.request.urlopen',side_effect=[io.BytesIO(json.dumps(record).encode()),io.BytesIO(payload)]):
        try:verify_public_deposit(wrong)
        except RuntimeError as e:assert 'both approved Study 2 specification hashes' in str(e)
        else:raise AssertionError('Wrong study/config accepted')
    save_once('results/deposit_verification_checks.json',{'matching_published_archive':'PASS','wrong_specification_rejected':'PASS','network_used':False})
    print('PASS: deposit verifies approved bytes and rejects different specification')
if __name__=='__main__':main()
