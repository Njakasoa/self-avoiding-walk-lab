"""Audit M7 frozen receipts, exact signs, reviews and unchanged legacy sources.

This integration audit does not replace the separate analytic review.
Full producer replay is optional because the six-row interval run is costly.
"""
import argparse
from fractions import Fraction as F
import hashlib
import json
from pathlib import Path
from proofs.check_m3 import receipt

ROOT = Path(__file__).resolve().parents[1]


def sha(path):
    return hashlib.sha256(path.read_bytes()).hexdigest()


def bounds(record):
    scale = 2 ** record['denominator_power_of_two']
    lo = F(int(record['lower_numerator']), scale)
    hi = F(int(record['upper_numerator']), scale)
    if lo > hi:
        raise ArithmeticError('reversed interval')
    return lo, hi


def main(replay=False):
    if not __debug__:
        raise RuntimeError('Run without -O: inherited receipt checks use assertions')
    names = ['m7-finite-v1', 'm7-effective-v1']
    finite, effective = [receipt(name) for name in names]
    expected = [32, 64, 128, 256, 512, 1024]
    assert finite['indices'] == expected
    assert [row['index'] for row in finite['rows']] == expected
    for row in finite['rows']:
        n = row['index']
        a, b = [bounds(row['phase_source_check'][key]) for key in ('a', 'b')]
        assert n+F(4,5) < a[0] <= a[1] < n+F(9,10)
        assert n < b[0] <= b[1] < n+1
        assert bounds(row['left']['F_certificate'])[0] > 0
        assert bounds(row['right']['F_certificate'])[1] < 0
        assert bounds(row['uniform_numerator']['P_plus_one_certificate'])[1] < 0
        lo, hi = map(F, row['t_bracket'])
        assert lo < hi
        assert hi-lo == 2*F(row['t_half_width'])
        for location in ('left', 'right', 'uniform_numerator'):
            tail = row[location]['tail']
            assert 0 < bounds(tail['R'])[0] <= bounds(tail['R'])[1] < 1
            assert 0 <= bounds(tail['tail_F'])[0] <= bounds(tail['tail_F'])[1] < F(1,10**27)
        for location in ('left', 'right'):
            directed = row[location]['directed']
            assert 0 < bounds(directed['D_I'])[0] <= bounds(directed['D_I'])[1] < 1
            assert 0 <= bounds(directed['tail'])[0] <= bounds(directed['tail'])[1] < F(1,10**30)
    from experiments.m7_effective_batch import payload
    assert effective == payload()
    assert effective['N_unique'] == '10^120'
    reviewed = {
        'proofs/m7_finite_poles.py': 'proofs/M7_FINITE_REVIEW.md',
        'proofs/M7_FINITE_TAIL.md': 'proofs/M7_FINITE_REVIEW.md',
    }
    for name in ['M7_EFFECTIVE_DERIVATIVE.md', 'M7_COMPLEX_SCALARS.md',
                 'M7_COMPLEX_KERNEL_SECTOR.md', 'M7_COMPLEX_PRODUCT_DOMINATION.md',
                 'M7_REAL_TO_DERIVATIVE.md', 'M7_UNIQUENESS_TRANSFER.md',
                 'm7_complex_boxes.py', 'm7_uniqueness_transfer.py']:
        reviewed['proofs/'+name] = 'proofs/M7_EFFECTIVE_REVIEW.md'
    hashes = {}
    for source, report in reviewed.items():
        hashes[source] = sha(ROOT/source)
        assert hashes[source] in (ROOT/report).read_text(), source
    legacy = {
        'proofs/W_NON_DFINITE.md': '351372992c252773a291f78b38a3521e68be7d60113145ff05087509c217780a',
        'proofs/M3_NON_DFINITE_CANDIDATE.md': 'e184726e834116e8eaf9d83926e571f40f4f2883eda1114b05c231872ec0a627',
        'publication/main.tex': 'd020e1c1d58e08bc642e74d7da5a1f02df33eb42defcfd6053d1a7bf250fd0e0',
        'proofs/M6_SHARP_KERNEL.md': '8717a3a191eb9f958f4b6a68d4066ae41bb8c13bc051985f3fe0791499158487',
    }
    for source, digest in legacy.items():
        assert sha(ROOT/source) == digest, source
    evidence = ROOT/'results/m7-independent-evidence'
    assert finite == json.loads((evidence/'m7-finite-six-exploratory.json').read_text())
    reviewed32 = json.loads((evidence/'m7-review-N32.json').read_text())
    assert reviewed32['rows'][0] == finite['rows'][0]
    comparison = json.loads((evidence/'m7-independent-N32.json').read_text())
    for moment in ('P', 'H'):
        old_lo, old_hi = bounds(comparison['original'][moment])
        new_lo, new_hi = bounds(comparison['regularized'][moment])
        tail_hi = bounds(comparison['regularized_tails']['tail_'+moment])[1]
        assert max(old_lo, new_lo-tail_hi) <= min(old_hi, new_hi+tail_hi)
    if replay:
        from proofs.m7_finite_poles import produce
        assert produce() == finite
    return {
        'status': 'PASS: provenance and exact integration arithmetic',
        'receipts': names, 'finite_indices': expected,
        'N_unique': '10^120', 'full_finite_producer_replayed': replay,
        'reviewed_source_hashes': hashes, 'legacy_sources_unchanged': legacy,
        'independent_evidence_hashes': {p.name: sha(p) for p in sorted(evidence.iterdir()) if p.is_file()},
        'scope': 'internal draft; finite existence only; effective uniqueness above threshold; intermediate bands remain open',
    }


if __name__ == '__main__':
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--replay', action='store_true')
    args = parser.parse_args()
    print(json.dumps(main(args.replay), indent=2, sort_keys=True))
