"""Content-addressed experiment receipts tied to committed source bytes."""
import hashlib,json,platform,subprocess,time,resource
from datetime import datetime,timezone
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]

def sha(path):return hashlib.sha256(Path(path).read_bytes()).hexdigest()
def git(*args):return subprocess.check_output(['git',*args],cwd=ROOT,text=True).strip()

def run_record(experiment_id,command,parameters,source_paths,producer):
    """Refuse unfrozen code; output and documentation changes may remain dirty."""
    commit=git('rev-parse','HEAD');inputs={}
    for rel in sorted(set(source_paths)):
        p=ROOT/rel
        committed=subprocess.check_output(['git','show',f'{commit}:{rel}'],cwd=ROOT)
        if committed!=p.read_bytes():raise RuntimeError(f'Source differs from commit: {rel}')
        inputs[rel]=sha(p)
    start=datetime.now(timezone.utc).isoformat();clock=time.perf_counter()
    result=producer();runtime=time.perf_counter()-clock
    output=ROOT/'results'/experiment_id;output.mkdir(parents=True,exist_ok=False)
    payload=output/'payload.json';payload.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    metadata={'experiment_id':experiment_id,'utc':start,'git_commit':commit,'command':command,
              'parameters':parameters,'seed':None,'deterministic':True,'compiler':subprocess.getoutput('g++ --version').splitlines()[0],
              'python':platform.python_version(),'cpu':next((x.split(':',1)[1].strip() for x in Path('/proc/cpuinfo').read_text().splitlines() if x.startswith('model name')),'unknown'),
              'ram':next(x for x in Path('/proc/meminfo').read_text().splitlines() if x.startswith('MemTotal:')),
              'runtime_seconds':runtime,'peak_rss_kib_process':resource.getrusage(resource.RUSAGE_SELF).ru_maxrss,
              'peak_rss_scope':'Python producer process; child C++ memory not measured',
              'input_hashes':inputs,'output_hashes':{'payload.json':sha(payload)},
              'agent':'root integration; role routing in ORCHESTRATION_LOG.md',
              'verification_status':'producer assertions passed; separate verifier required',
              'git_dirty':bool(git('status','--porcelain'))}
    (output/'metadata.json').write_text(json.dumps(metadata,indent=2,sort_keys=True)+'\n')
    return output
