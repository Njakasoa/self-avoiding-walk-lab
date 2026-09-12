"""Independent falsification tests for the first SAW milestone.

The checks in this file deliberately use representations different from the
production routines: fixed-grid bit masks and direction-word exhaustion for
SAWs/bridges, an unreduced path-state construction for the D4 quotient, and
direct cyclotomic arithmetic for the honeycomb control.  The tests are small
enough to run as a regular pytest suite, while the report records the larger
standalone runs as well.
"""

from __future__ import annotations

from collections import Counter, defaultdict
from fractions import Fraction
from itertools import product
import copy
import json
from pathlib import Path
import shutil
import subprocess
import tempfile

import pytest
import sympy as sp

from src.automaton import check_certificate, certificate, memory_automaton
from src.bridges import enumerate_bridges, lower_certificate, renewal_inverse, renewal_points
from src.connectivity_tm import connectivity_counts
from src.reference_enumerator import counts, rectangle_counts
from src.transfer_matrix import transfer_counts


ROOT = Path(__file__).resolve().parents[1]
DATA = ROOT / "data" / "A001411.txt"
DIRS = ((0, 1), (1, 0), (0, -1), (-1, 0))


def _oeis_counts() -> list[int]:
    values: dict[int, int] = {}
    for line in DATA.read_text().splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        n, value = line.split()
        values[int(n)] = int(value)
    return [values[n] for n in range(max(values) + 1)]


def _word_counts(max_n: int) -> list[int]:
    """Exhaust all direction words, validating each word by a coordinate set."""

    result = [0] * (max_n + 1)
    result[0] = 1
    for length in range(1, max_n + 1):
        for word in product(range(4), repeat=length):
            x = y = 0
            occupied = {(0, 0)}
            valid = True
            for direction in word:
                dx, dy = DIRS[direction]
                x, y = x + dx, y + dy
                if (x, y) in occupied:
                    valid = False
                    break
                occupied.add((x, y))
            if valid:
                result[length] += 1
    return result


def _bitmask_counts(max_n: int) -> list[int]:
    """Count all prefixes with a fixed-grid integer occupation mask.

    Coordinates are bounded by [-max_n, max_n], so no coordinate dictionary
    or path tuple is needed.  This is independent of the reference DFS's set
    representation and also reaches n=12 quickly.
    """

    side = 2 * max_n + 1
    offset = max_n

    def bit(x: int, y: int) -> int:
        return 1 << ((y + offset) * side + x + offset)

    result = [0] * (max_n + 1)
    result[0] = 1

    def visit(x: int, y: int, depth: int, occupied: int) -> None:
        if depth == max_n:
            return
        for dx, dy in DIRS:
            nx, ny = x + dx, y + dy
            destination = bit(nx, ny)
            if occupied & destination:
                continue
            result[depth + 1] += 1
            visit(nx, ny, depth + 1, occupied | destination)

    visit(0, 0, 0, bit(0, 0))
    return result


def _word_paths(length: int):
    """Yield valid complete paths from every direction word of given length."""

    for word in product(range(4), repeat=length):
        x = y = 0
        path = [(0, 0)]
        occupied = {(0, 0)}
        for direction in word:
            dx, dy = DIRS[direction]
            x, y = x + dx, y + dy
            point = (x, y)
            if point in occupied:
                break
            occupied.add(point)
            path.append(point)
        else:
            yield tuple(path)


def _is_bridge(path: tuple[tuple[int, int], ...]) -> bool:
    if len(path) < 2:
        return False
    xs = [point[0] for point in path]
    return all(x > 0 for x in xs[1:]) and xs[-1] == max(xs)


def _is_renewal(path: tuple[tuple[int, int], ...], k: int) -> bool:
    """Apply the definition to a prefix and translated suffix directly."""

    prefix = path[: k + 1]
    anchor_x, anchor_y = path[k]
    suffix = tuple((x - anchor_x, y - anchor_y) for x, y in path[k:])
    return _is_bridge(prefix) and _is_bridge(suffix)


def _independent_bridge_data(max_n: int):
    bridge_counts = [0] * (max_n + 1)
    bridge_counts[0] = 1
    irreducible_counts = [0] * (max_n + 1)
    spans = [Counter() for _ in range(max_n + 1)]
    for length in range(1, max_n + 1):
        for path in _word_paths(length):
            if not _is_bridge(path):
                continue
            bridge_counts[length] += 1
            span = path[-1][0]
            spans[length][span] += 1
            if not any(_is_renewal(path, k) for k in range(1, length)):
                irreducible_counts[length] += 1
    return {
        "bridges": bridge_counts,
        "irreducibles": irreducible_counts,
        "span_counts": [dict(sorted(item.items())) for item in spans],
    }


def _d4_canonical(path: tuple[tuple[int, int], ...]):
    """Canonicalize by explicitly applying the eight signed coordinate maps."""

    x0, y0 = path[0]
    translated = [(x - x0, y - y0) for x, y in path]
    variants = []
    for swap in (False, True):
        for sx in (-1, 1):
            for sy in (-1, 1):
                transformed = []
                for x, y in translated:
                    a, b = (y, x) if swap else (x, y)
                    transformed.append((sx * a, sy * b))
                variants.append(tuple(transformed))
    return min(variants)


def _unreduced_states(memory: int):
    """Generate all length-memory SAW paths without any symmetry quotient."""

    layer = {((0, 0),)}
    for _ in range(memory):
        next_layer = set()
        for path in layer:
            x, y = path[-1]
            for dx, dy in DIRS:
                point = (x + dx, y + dy)
                if point not in path:
                    next_layer.add(path + (point,))
        layer = next_layer
    return layer


def _row_from_path(path, quotient_index):
    x, y = path[-1]
    row = Counter()
    for dx, dy in DIRS:
        point = (x + dx, y + dy)
        if point in path:
            continue
        destination = _d4_canonical(path[1:] + (point,))
        row[quotient_index[destination]] += 1
    return dict(sorted(row.items()))


def test_independent_enumeration_matches_a001411_through_n12():
    expected = _oeis_counts()
    assert _word_counts(8) == expected[:9]
    assert _bitmask_counts(12) == expected[:13]
    assert counts(12) == expected[:13]


def test_unreduced_and_d4_automata_have_complete_equitable_rows():
    for memory in range(1, 9):
        unreduced = _unreduced_states(memory)
        assert len(unreduced) == _oeis_counts()[memory]

        full_states, full_rows = memory_automaton(memory, symmetry=False)
        assert set(full_states) == unreduced

        quotient_states, quotient_rows = memory_automaton(memory, symmetry=True)
        quotient_index = {state: index for index, state in enumerate(quotient_states)}
        expected_orbits = {_d4_canonical(path) for path in unreduced}
        assert expected_orbits == set(quotient_states)

        continuation_rows = defaultdict(set)
        for path in unreduced:
            row = _row_from_path(path, quotient_index)
            continuation_rows[_d4_canonical(path)].add(tuple(row.items()))
        assert all(len(rows) == 1 for rows in continuation_rows.values())
        for state, row in zip(quotient_states, quotient_rows):
            assert row == dict(next(iter(continuation_rows[state])))


def test_square_lattice_return_parity_explains_memory_plateaus():
    # A proposed return to an older path vertex closes a cycle.  The square
    # lattice is bipartite, so the cycle length is even and the backward
    # distance from the endpoint is odd.  Therefore the extra oldest vertex
    # when memory m grows to m+1 cannot matter for odd m.
    for max_length in (6, 8):
        for length in range(2, max_length + 1):
            for path in _word_paths(length):
                endpoint = path[-1]
                for old_index, old in enumerate(path[:-1]):
                    dx = abs(endpoint[0] - old[0])
                    dy = abs(endpoint[1] - old[1])
                    if dx + dy != 1:
                        continue
                    backward_distance = len(path) - 1 - old_index
                    assert backward_distance % 2 == 1

    # The actual quotient rates exhibit the predicted odd/even plateaus at
    # the first two pairs (the equality is exact rational certificate text).
    certs = [certificate(memory_automaton(m)[1], iterations=20)["upper"] for m in range(1, 7)]
    assert certs[0] == certs[1]
    assert certs[2] == certs[3]
    assert Fraction(certs[4]) <= Fraction(certs[2])


def test_integer_certificate_mutations_are_rejected():
    _states, rows = memory_automaton(3)
    cert = certificate(rows, iterations=24)
    assert check_certificate(rows, cert)

    lower_upper = copy.deepcopy(cert)
    lower_upper["upper"] = str(Fraction(cert["upper"]) - Fraction(1, 10**6))
    assert not check_certificate(rows, lower_upper)

    zero_vector = copy.deepcopy(cert)
    zero_vector["vector"][0] = "0"
    assert not check_certificate(rows, zero_vector)

    wrong_length = copy.deepcopy(cert)
    wrong_length["vector"] = wrong_length["vector"][:-1]
    assert not check_certificate(rows, wrong_length)

    negative_edge = [dict(row) for row in rows]
    negative_edge[0] = dict(negative_edge[0])
    destination = next(iter(negative_edge[0]))
    negative_edge[0][destination] = -1
    assert not check_certificate(negative_edge, cert)

    out_of_range = [dict(row) for row in rows]
    out_of_range[0] = dict(out_of_range[0])
    destination = next(iter(out_of_range[0]))
    weight = out_of_range[0].pop(destination)
    out_of_range[0][len(out_of_range)] = weight
    assert not check_certificate(out_of_range, cert)


def test_bridge_geometry_and_renewal_inverse_independent_through_n10():
    expected = _independent_bridge_data(10)
    observed = enumerate_bridges(10)
    assert observed == expected
    assert observed["irreducibles"] == renewal_inverse(observed["bridges"])
    certificate_data = lower_certificate(observed["irreducibles"], bits=40)
    lo = Fraction(certificate_data["root_low"])
    hi = Fraction(certificate_data["root_high"])
    polynomial = lambda z: sum(value * z**index for index, value in enumerate(observed["irreducibles"]))
    assert polynomial(lo) <= 1 <= polynomial(hi)
    assert Fraction(certificate_data["lower"]) == 1 / hi

    # Compare every geometric cut, rather than only the aggregate coefficient
    # sequence, against the production renewal-point predicate.
    for length in range(1, 11):
        for path in _word_paths(length):
            if _is_bridge(path):
                direct = [k for k in range(1, length) if _is_renewal(path, k)]
                assert renewal_points(list(path)) == direct

    # Terminal maximum is weak: the span may be reached before the endpoint.
    plateau = ((0, 0), (1, 0), (1, 1), (1, 2))
    assert _is_bridge(plateau)
    assert plateau[-1][0] == max(x for x, _ in plateau)
    assert not any(_is_renewal(plateau, k) for k in range(1, len(plateau) - 1))

    # An actual internal cut has a bridge prefix and a translated bridge suffix.
    cut = ((0, 0), (1, 0), (1, 1), (2, 1))
    assert _is_bridge(cut)
    assert _is_renewal(cut, 2)
    assert 1 <= cut[-1][0]

    # Strict initial minimum rejects a path that stays on x=0 after the root.
    assert not _is_bridge(((0, 0), (0, 1), (1, 1)))


def test_honeycomb_cyclotomic_control_and_wrong_phase():
    t = sp.Symbol("t")
    phi = sp.cyclotomic_poly(48, t)

    def remainder(expr):
        return sp.rem(sp.Poly(sp.expand(expr), t), sp.Poly(phi, t)).as_expr()

    mu = t**3 + t**45
    assert remainder(t**36 + t**12) == 0
    assert remainder(mu + t**21 + t**27) == 0
    assert remainder(mu**4 - 4 * mu**2 + 2) == 0
    assert remainder(mu + t**20 + t**28) != 0

    physical = sp.sqrt(2 + sp.sqrt(2))
    assert sp.simplify(2 * sp.cos(sp.pi / 8) - physical) == 0


def test_rectangle_reference_and_transfer_matrix_agree_on_small_boxes():
    for width in range(1, 6):
        for height in range(1, 6):
            max_n = width * height + 2
            assert transfer_counts(width, height, max_n) == rectangle_counts(width, height, max_n)

    assert rectangle_counts(1, 5, 8) == [1, 1, 1, 1, 1, 0, 0, 0, 0]
    assert transfer_counts(2, 2, 5) == [1, 2, 2, 2, 0, 0]


def test_connectivity_edge_transfer_agrees_with_occupation_transfer():
    # The edge-subset transfer is a third representation: it processes every
    # undirected edge, tracks degrees/components, and accepts completed paths.
    # These cases include the two requested nontrivial rectangles and
    # degenerate one-row/one-column boxes.
    for width, height in ((2, 3), (3, 2), (3, 3), (1, 1), (1, 4), (4, 1)):
        max_n = width * height + 1
        connectivity = connectivity_counts(width, height, max_n)
        occupation = transfer_counts(width, height, max_n)
        reference = rectangle_counts(width, height, max_n)
        assert connectivity["counts"] == occupation == reference
        assert connectivity["edge_count"] == width * (height - 1) + height * (width - 1)
        assert connectivity["peak_states"] >= 1

    for args in ((0, 2, 3), (2, 0, 3), (2, 2, -1), (True, 2, 3), (2, True, 3), (2, 2, True)):
        with pytest.raises(ValueError):
            connectivity_counts(*args)


def test_cplusplus_enumerator_matches_known_counts_through_n12():
    compiler = shutil.which("g++")
    if compiler is None:
        pytest.skip("g++ unavailable")
    expected = _oeis_counts()[:13]
    with tempfile.TemporaryDirectory(prefix="saw-enumerator-") as directory:
        executable = Path(directory) / "saw_enum"
        subprocess.run(
            [compiler, "-std=c++20", "-O2", "-DNDEBUG", "src/optimized_enumerator.cpp", "-o", str(executable)],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        completed = subprocess.run(
            [str(executable), "--json", "12"],
            cwd=ROOT,
            check=True,
            capture_output=True,
            text=True,
        )
        assert json.loads(completed.stdout) == expected


def test_public_count_apis_reject_negative_values_and_booleans_consistently():
    calls = (
        lambda value: counts(value),
        lambda value: rectangle_counts(2, 2, value),
        lambda value: transfer_counts(2, 2, value),
        lambda value: memory_automaton(value),
        lambda value: enumerate_bridges(value),
    )
    for call in calls:
        with pytest.raises(ValueError):
            call(-1)
        with pytest.raises(ValueError):
            call(True)
