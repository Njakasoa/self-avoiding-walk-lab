"""Independent geometry/spectral and algebra checks of frozen M3 receipts.

The prudent interval replay intentionally uses the reviewed exact enclosure
engine; its formulas, rounding and mathematical argument have separate Astra
review. Deadline geometry and ladder series here do not import their producers.
"""
import argparse
from collections import Counter
from fractions import Fraction
from math import comb
from pathlib import Path
import hashlib
import json
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def receipt(name):
    folder = ROOT/'results'/name
    meta = json.loads((folder/'metadata.json').read_text())
    for rel, wanted in meta['input_hashes'].items():
        frozen = subprocess.check_output(['git', 'show', f"{meta['git_commit']}:{rel}"], cwd=ROOT)
        assert hashlib.sha256(frozen).hexdigest() == wanted
        assert hashlib.sha256((ROOT/rel).read_bytes()).hexdigest() == wanted, rel
    for rel, wanted in meta['output_hashes'].items():
        assert hashlib.sha256((folder/rel).read_bytes()).hexdigest() == wanted
    return json.loads((folder/'payload.json').read_text())


def canonical(points):
    matrices = [(a, 0, 0, b) for a in (-1, 1) for b in (-1, 1)]
    matrices += [(0, a, b, 0) for a in (-1, 1) for b in (-1, 1)]
    return min(tuple(sorted((a*x+b*y, c*x+d*y, age) for x, y, age in points))
               for a, b, c, d in matrices)


def successors(state, memory):
    occupied = {(x, y) for x, y, _ in state}
    result = Counter()
    for dx, dy in ((0, 1), (0, -1), (1, 0), (-1, 0)):
        if (dx, dy) in occupied:
            continue
        moved = [(0, 0, memory+1)]
        for x, y, age in state:
            if age >= 2 and abs(x-dx)+abs(y-dy) < age:
                moved.append((x-dx, y-dy, age-1))
        result[canonical(moved)] += 1
    return result


def deadline(data):
    for case in data['cases']:
        m = case['memory']
        states = [tuple(map(tuple, state)) for state in case['states']]
        assert len(set(states)) == len(states) == case['state_count']
        index = {s: i for i, s in enumerate(states)}
        layer = {((0, 0, m+1),)}
        for _ in range(m):
            layer = {nxt for state in layer for nxt in successors(state, m)}
        assert layer == set(states), m
        rows = [{int(j): w for j, w in row.items()} for row in case['rows']]
        assert len(rows) == len(states)
        for state, row in zip(states, rows):
            actual = {index[s]: weight for s, weight in successors(state, m).items()}
            assert row == actual, m
        cert = case['certificate']
        vector, upper = cert['vector'], Fraction(cert['upper'])
        assert len(vector) == len(rows) and all(v > 0 for v in vector)
        assert all(sum(w*vector[j] for j, w in row.items()) <= upper*vector[i]
                   for i, row in enumerate(rows))
    return len(data['cases'])


def ladder_coefficients(max_n):
    # Expand the displayed rational expression by u-degree, independently
    # of the producer's geometric endpoint factors or fitted recurrence.
    rows = {}
    for r in range(max_n//2):
        h, shift, power = 4+2*r, 2+2*r, 4+2*r
        values = {}
        for v in range(max_n-h+1):
            coefficient = 0
            for s, c in enumerate((1, 2, 3, 2, 1)):
                k = v-shift-s
                if k >= 0:
                    coefficient += 2*c*sum(comb(power+a-1, a)*(-1)**(k-a)*(k-a+1)
                                             for a in range(k+1))
            if coefficient:
                values[v] = coefficient
        if values:
            rows[h] = values
    return rows


def span(data):
    values = [0]*(data['max_n']+1)
    for h, row in ladder_coefficients(data['max_n']).items():
        for v, c in row.items():
            values[h+v] += c
    assert values == data['i_span2']
    weighted = {int(h): {int(v): c for v, c in row.items()}
                for h, row in data['weighted_i_span2'].items()}
    assert weighted == ladder_coefficients(data['weighted_max_n'])
    return len(values)


def weight_witnesses(data):
    count = 0
    for case in data['cases']:
        witness = case['counterexample']
        if witness is None:
            continue
        totals = []
        for key in ('first_path', 'second_path'):
            path = [tuple(p) for p in witness[key]]
            assert len(set(path)) == len(path) == case['memory']+1
            assert all(abs(a[0]-b[0])+abs(a[1]-b[1]) == 1 for a, b in zip(path, path[1:]))
            x, y = path[-1]
            totals.append([sum((x+dx, y+dy) not in path for dx, dy in directions)
                           for directions in (((1,0),(-1,0)),((0,1),(0,-1)))])
        assert totals == [witness['first_HV_out_counts'], witness['second_HV_out_counts']]
        # Some later witnesses may differ only after more steps. The memory-9
        # explicit falsifier is the one whose one-step counts prove failure.
        if case['memory'] == 9:
            assert totals[0] != totals[1]
        count += 1
    return count


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--suffix', default='v1')
    args = parser.parse_args()
    data = {kind: receipt(f'm3-{kind}-{args.suffix}') for kind in ('span','weights','prudent','deadline')}
    result = {'deadline_cases': deadline(data['deadline']),
              'ladder_coefficients': span(data['span']),
              'weighted_witnesses': weight_witnesses(data['weights'])}
    from proofs.m3_prudent_intervals import produce
    assert produce() == data['prudent']['interval_certificate']
    assert data['prudent']['independent_geometry']['ramp_counts'] == [0,1,2,4,9,20,46,108,257,615,1478,3567,8641]
    assert data['prudent']['independent_geometry']['hook_counts'] == [0,0,0,0,1,3,8,20,49,120,294,721,1768]
    result['prudent_singularities'] = data['prudent']['interval_certificate']['count']
    result['status'] = 'PASS; finite checkpoint, M3 theorem open'
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
