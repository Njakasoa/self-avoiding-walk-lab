"""Freeze a full standalone M4 replay and local PDF build in a research receipt."""
import argparse
import importlib.util
import json
from pathlib import Path
import sys

from src.provenance import ROOT, run_record


def main():
    if not __debug__:
        raise RuntimeError('Run without -O: proof checkers require assertions')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('experiment_id')
    parser.add_argument('--tectonic', default='tectonic')
    args = parser.parse_args()
    manifest = json.loads((ROOT/'publication/source_manifest.json').read_text())
    inputs = ['src/provenance.py', 'experiments/m4_publication_batch.py',
              'publication/source_manifest.json']
    inputs += ['publication/'+rel for rel in manifest['sha256']]

    def produce():
        spec = importlib.util.spec_from_file_location(
            'publication_replay', ROOT/'publication/reproduce.py')
        replay = importlib.util.module_from_spec(spec)
        spec.loader.exec_module(replay)
        previous = sys.argv
        try:
            sys.argv = ['reproduce.py', '--pdf', '--tectonic', args.tectonic]
            replay.main()
        finally:
            sys.argv = previous
        return json.loads((ROOT/'publication/VALIDATION.json').read_text())

    command = (f'PYTHONPATH=. .venv/bin/python experiments/m4_publication_batch.py '
               f'{args.experiment_id} --tectonic {args.tectonic}')
    print(run_record(args.experiment_id, command,
                     {'pdf': True, 'tectonic': args.tectonic}, inputs, produce))


if __name__ == '__main__':
    main()
