"""Replay W arithmetic using retained sources, without private Git history."""
from pathlib import Path
import hashlib
import json
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    if not __debug__:
        raise RuntimeError('Run without -O: the interval engine requires assertions')
    # These are all local scientific modules executed below. The historical
    # producer driver, analytic notes and source PDF are not executed here.
    groups = {
        'w-identities-v1': ['experiments/w_exact_identities.py',
                            'experiments/w_directed_ramps_check.py'],
        'w-critical-v1': ['proofs/w_critical_certificate.py',
                          'proofs/m3_critical_integrals.py',
                          'proofs/m3_prudent_intervals.py'],
    }
    expected = {}
    for name, sources in groups.items():
        folder = ROOT/'results'/name
        meta = json.loads((folder/'metadata.json').read_text())
        for rel in sources:
            actual = hashlib.sha256((ROOT/rel).read_bytes()).hexdigest()
            if actual != meta['input_hashes'][rel]:
                raise RuntimeError(f'Scientific source hash mismatch: {rel}')
        payload = (folder/'payload.json').read_bytes()
        if hashlib.sha256(payload).hexdigest() != meta['output_hashes']['payload.json']:
            raise RuntimeError(f'Recorded payload hash mismatch: {name}')
        expected[name] = json.loads(payload)
    sys.path.insert(0, str(ROOT))
    from experiments.w_exact_identities import produce as quotients
    from experiments.w_directed_ramps_check import produce as directed
    from proofs.w_critical_certificate import produce as critical
    actual = {'w-identities-v1': {'quotients': quotients(), 'directed': directed()},
              'w-critical-v1': critical(bins=2048, power_bits=16)}
    for name, payload in actual.items():
        if payload != expected[name]:
            raise ArithmeticError(f'Replayed payload differs: {name}')
        print(f'PASS: {name} source hashes and recomputed payload')
    print('Arithmetic replay only; uniform convergence and genuine poles require the reviewed analytic proof.')


if __name__ == '__main__':
    main()
