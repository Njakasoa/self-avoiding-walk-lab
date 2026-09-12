"""Record finite uniqueness and residue enclosures on the six M7 brackets."""
import argparse
import hashlib
from pathlib import Path

from proofs.check_m3 import receipt
from proofs.m7_finite_poles import BITS, I384, SEEDS
from proofs.m8_finite_derivatives import produce
from src.provenance import run_record

ROOT = Path(__file__).resolve().parents[1]
M7_PAYLOAD_SHA = '75641df0f1a84d231e058302b89d8b5a603a4914a9ddd2b84601c1cf2b50f87f'


def decode(record):
    if record['denominator_power_of_two'] != BITS:
        raise ArithmeticError('wrong interval precision')
    return I384(int(record['lower_numerator']),
                int(record['upper_numerator']), raw=True)


def combine(data, old):
    """Combine derivative boxes with certified existence on identical domains."""
    previous = {row['index']: row for row in old['rows']}
    for row in data['rows']:
        base = previous[row['index']]
        if row['t_bracket'] != base['t_bracket']:
            raise ArithmeticError('derivative and existence domains differ')
        decode(base['left']['F_certificate']).positive('left endpoint F')
        decode(base['right']['F_certificate']).negative('right endpoint F')
        decode(base['uniform_numerator']['P_plus_one_certificate']).negative('M7 numerator')
        if base['phase_source_check']['source_pole_free'] is not True:
            raise ArithmeticError('missing source-pole exclusion')
        numerator = 1 + decode(row['P']['value'])
        derivative = decode(row['F']['derivative'])
        numerator.negative('M8 numerator')
        derivative.negative('M8 derivative')
        residue = -numerator / derivative
        residue.negative('W residue')
        row['residue_in_t'] = residue.record()
        row['N_cubed_residue'] = (row['index']**3 * residue).record()
        row['unique_simple_noncancelled_pole_in_bracket'] = True
    data['scope'] = ('Only the listed narrow rational brackets. No full-band '
                     'uniqueness or unlisted-index coverage is asserted.')
    data['existence_receipt_sha256'] = M7_PAYLOAD_SHA
    return data


def payload(indices=tuple(SEEDS)):
    if not __debug__:
        raise RuntimeError('Run without -O: inherited receipts use assertions')
    if hashlib.sha256((ROOT/'results/m7-finite-v1/payload.json').read_bytes()).hexdigest() != M7_PAYLOAD_SHA:
        raise ArithmeticError('M7 payload changed')
    old = receipt('m7-finite-v1')
    return combine(produce(indices), old)


def main():
    if not __debug__:
        raise RuntimeError('Run without -O')
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('experiment_id')
    args = parser.parse_args()
    sources = [
        'experiments/m8_finite_batch.py', 'proofs/m8_finite_derivatives.py',
        'proofs/M8_FINITE_DERIVATIVES.md', 'proofs/m7_finite_poles.py',
        'proofs/M7_FINITE_TAIL.md', 'proofs/check_m3.py',
        'proofs/W_NON_DFINITE.md', 'results/m7-finite-v1/payload.json',
        'results/m7-finite-v1/metadata.json', 'src/provenance.py',
        'requirements-lock.txt',
    ]
    command = f'.venv/bin/python -m experiments.m8_finite_batch {args.experiment_id}'
    print(run_record(args.experiment_id, command,
                     {'indices': list(SEEDS), 'bits': BITS,
                      'scope': 'finite narrow-bracket uniqueness and residues'},
                     sources, payload))


if __name__ == '__main__':
    main()
