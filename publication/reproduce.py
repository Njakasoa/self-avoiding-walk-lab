"""Recompute the bundled proof objects and scientific figure locally.

Run with --pdf --tectonic /path/to/tectonic to also compile main.tex.
The checkers and manuscript are self-contained in this directory.
"""
from pathlib import Path
import argparse
import hashlib
import importlib.util
import json
import os
import shutil
import subprocess
import sys
import tempfile

ROOT=Path(__file__).resolve().parent
CHECKERS=ROOT/'proof-checkers'


def sha(path):return hashlib.sha256(path.read_bytes()).hexdigest()


def module(name,path):
    spec=importlib.util.spec_from_file_location(name,path)
    value=importlib.util.module_from_spec(spec);spec.loader.exec_module(value)
    return value


def main():
    if not __debug__:
        raise RuntimeError('Run without -O: the proof checkers require assertions')
    p=argparse.ArgumentParser(description=__doc__)
    p.add_argument('--pdf',action='store_true')
    p.add_argument('--tectonic',default='tectonic')
    p.add_argument('--no-figures',action='store_true')
    args=p.parse_args()
    manifest_path=ROOT/'source_manifest.json'
    if not manifest_path.exists():raise RuntimeError('Missing source_manifest.json')
    manifest=json.loads(manifest_path.read_text())
    for rel,wanted in manifest['sha256'].items():
        if sha(ROOT/rel)!=wanted:raise RuntimeError(f'Source hash mismatch: {rel}')
    sys.path.insert(0,str(CHECKERS))
    import critical_integrals,intervals,moment_identities,independent_identities,reference_counts
    exact=critical_integrals.produce()
    expected=json.loads((CHECKERS/'expected-integrals.json').read_text())
    assert exact==expected,'Integral certificate differs from frozen payload'
    root_identities=moment_identities.produce()
    independent=independent_identities.exact_checks()
    finite=intervals.produce()
    counts=reference_counts.counts()
    assert counts['ramp_counts']==[0,1,2,4,9,20,46,108,257,615,1478,3567,8641]
    assert counts['hook_counts']==[0,0,0,0,1,3,8,20,49,120,294,721,1768]
    outputs=[]
    if not args.no_figures:
        outputs+=module('publication_figure',ROOT/'figures/generate.py').generate(exact)
    if args.pdf:
        executable=shutil.which(args.tectonic)
        if executable is None:raise RuntimeError('Tectonic not found; supply --tectonic PATH')
        build=ROOT/'build';build.mkdir(exist_ok=True)
        env=os.environ.copy()
        env.setdefault('XDG_CACHE_HOME',str(Path(tempfile.gettempdir())/'saw-lab-tex-cache'))
        env.setdefault('SOURCE_DATE_EPOCH','1789171200')
        proc=subprocess.run([executable,'--untrusted','--keep-logs','--outdir',str(build),'main.tex'],cwd=ROOT,env=env,text=True,stdout=subprocess.PIPE,stderr=subprocess.STDOUT)
        (build/'compile-output.txt').write_text(proc.stdout)
        if proc.returncode:raise RuntimeError(f'LaTeX compilation failed; see {build}/compile-output.txt')
        shutil.copyfile(build/'main.pdf',ROOT/'main.pdf');outputs.append('main.pdf')
    result={'status':'PASS','publication_priority':'UNRESOLVED',
            'integral_certificate_exact_match':True,
            'symbolic_checks':root_identities['checks'],
            'independent_symbolic_checks':independent,
            'finite_poles_checked':finite['count'],'geometric_length':counts['max_n'],
            'source_manifest_sha256':sha(manifest_path),
            'outputs':{rel:sha(ROOT/rel) for rel in outputs},
            'pdf_compiled':args.pdf,
            'scope':'Computational certificates replayed. The analytic infinite-pole proof is in main.tex and the documented independent review; these programs are not a formal proof assistant.'}
    (ROOT/'VALIDATION.json').write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print(json.dumps(result,indent=2,sort_keys=True))


if __name__=='__main__':main()
