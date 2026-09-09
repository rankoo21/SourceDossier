import json,pytest
from harness import load,UserError
@pytest.fixture
def env():return load('source_dossier.py','SourceDossier')
def queue(e,other=None):
 e[4].extend(['source alpha confirms release','source beta confirms release','source alpha confirms release','source beta confirms release']);v={'codes':['AGREES','AGREES']};e[3].extend([json.dumps(v),json.dumps(other or v)])
def test_full_attributed_path(env):
 queue(env);env[1].resolve('DOS-1','The package release is available and documented.','https://a.example/release','https://b.example/release');r=json.loads(env[1].get_dossier('dos-1'));assert r['verdict']=='SUPPORTED' and len(r['sources'])==2 and len(r['sources'][0]['digest'])==64
def test_distinct_hosts_and_clean_https(env):
 for a,b in [('https://x.example/a','https://x.example/b'),('http://a.example/a','https://b.example/b'),('https://u:p@a.example/a','https://b.example/b')]:
  with pytest.raises(UserError):env[1].resolve('DOS-1','A sufficiently detailed claim for evaluation.',a,b)
 assert env[5]==[]
def test_duplicate_normalized(env):
 queue(env);env[1].resolve('DOS-1','The package release is available and documented.','https://a.example/r','https://b.example/r')
 with pytest.raises(UserError):env[1].resolve(' dos-1 ','The package release is available and documented.','https://c.example/r','https://d.example/r')
def test_source_disagreement_fails_closed(env):
 env[4].extend(['alpha valid content here','beta valid content here','alpha changed content now','beta valid content here']);v={'codes':['AGREES','AGREES']};env[3].extend([json.dumps(v),json.dumps(v)])
 with pytest.raises(UserError):env[1].resolve('DOS-1','The package release is available and documented.','https://a.example/r','https://b.example/r')
 assert env[1].get_dossier('DOS-1')=='{}'
def test_exact_findings_checked(env):
 queue(env,{'codes':['AGREES','MISSING']})
 with pytest.raises(UserError):env[1].resolve('DOS-1','The package release is available and documented.','https://a.example/r','https://b.example/r')
@pytest.mark.parametrize('raw',['{}','{"codes":["AGREES"]}','{"codes":["YES","AGREES"]}'])
def test_malformed(env,raw):
 env[4].extend(['source alpha confirms release','source beta confirms release']);env[3].append(raw)
 with pytest.raises((ValueError,UserError)):env[1].resolve('DOS-1','The package release is available and documented.','https://a.example/r','https://b.example/r')
