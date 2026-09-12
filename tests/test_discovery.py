"""Independent small-case checks for the discovery engine.

The path and bridge enumerators in this file intentionally do not call the
corresponding production constructors.  They use direction words and direct
coordinate predicates so that a shared implementation mistake is less likely
to make both sides agree.
"""

from __future__ import annotations

from collections import Counter
from fractions import Fraction
from itertools import product
import random

import pytest

from src.bridge_spans import enumerate_bridge_spans
from src.discovery_engine import memory_case
from src.discovery_memory import SQUARE, TRIANGULAR, build_memory, exact_certificate, verify_bound
from src.equitable import (
    equitable_partition,
    lift_vector,
    quotient,
    verify_equitable,
)


def _word_for_path(path, directions):
    direction_index = {step: index for index, step in enumerate(directions)}
    return tuple(
        direction_index[(b[0] - a[0], b[1] - a[1])]
        for a, b in zip(path, path[1:])
    )


def _ends_with_forbidden(path, directions, forbidden_words):
    word = _word_for_path(path, directions)
    return any(len(bad) <= len(word) and word[-len(bad) :] == bad for bad in forbidden_words)


def _independent_memory_states(
    memory,
    directions,
    *,
    roots=((0, 0),),
    width=None,
    forbidden_words=(),
):
    """Enumerate exact length-memory states without symmetry reduction."""

    forbidden_words = tuple(tuple(word) for word in forbidden_words)
    layer = {(root,) for root in roots}
    for _ in range(memory):
        next_layer = set()
        for path in layer:
            x, y = path[-1]
            for dx, dy in directions:
                point = (x + dx, y + dy)
                if point in path:
                    continue
                if width is not None and not 0 <= point[1] < width:
                    continue
                candidate = path + (point,)
                if _ends_with_forbidden(candidate, directions, forbidden_words):
                    continue
                next_layer.add(candidate)
        layer = next_layer
    return sorted(layer)


def _independent_memory_rows(
    states,
    directions,
    weights,
    *,
    width=None,
    forbidden_words=(),
):
    forbidden_words = tuple(tuple(word) for word in forbidden_words)
    index = {state: position for position, state in enumerate(states)}
    rows = []
    for path in states:
        x, y = path[-1]
        row = Counter()
        for direction, (dx, dy) in enumerate(directions):
            point = (x + dx, y + dy)
            if point in path:
                continue
            if width is not None and not 0 <= point[1] < width:
                continue
            candidate = path[1:] + (point,)
            if _ends_with_forbidden(path + (point,), directions, forbidden_words):
                continue
            # Production states are rooted after each shift.  Plane states
            # translate both coordinates; strip states translate only x and
            # retain their absolute row.
            x0, y0 = candidate[0]
            if width is None:
                candidate = tuple((px - x0, py - y0) for px, py in candidate)
            else:
                candidate = tuple((px - x0, py) for px, py in candidate)
            assert candidate in index
            if weights[direction]:
                row[index[candidate]] += weights[direction]
        rows.append(dict(sorted(row.items())))
    return rows


@pytest.mark.parametrize(
    "memory,directions,roots,width,weights,forbidden_words",
    [
        (
            2,
            SQUARE,
            ((0, 0),),
            None,
            (Fraction(1, 2), Fraction(2), Fraction(3, 2), Fraction(5, 2)),
            (),
        ),
        (
            2,
            TRIANGULAR,
            ((0, 0),),
            None,
            (Fraction(1), Fraction(3, 2), Fraction(2), Fraction(5, 2), Fraction(3), Fraction(7, 2)),
            (),
        ),
        (
            2,
            SQUARE,
            ((0, 0), (0, 1)),
            2,
            (Fraction(1), Fraction(3, 2), Fraction(2), Fraction(5, 2)),
            (),
        ),
        (
            3,
            SQUARE,
            ((0, 0),),
            None,
            (Fraction(1), Fraction(4, 3), Fraction(2), Fraction(5, 3)),
            ((0, 1), (3, 2)),
        ),
    ],
    ids=["square-weighted", "triangular-weighted", "strip-weighted", "motif-weighted"],
)
def test_unreduced_memory_continuations_match_direction_word_enumeration(
    memory, directions, roots, width, weights, forbidden_words
):
    kwargs = {
        "memory": memory,
        "lattice": "triangular" if directions == TRIANGULAR else "square",
        "boundary": "strip" if width is not None else "plane",
        "width": width,
        "weights": weights,
        "forbidden_words": forbidden_words,
        "symmetry": "none",
        "max_seconds": 30,
    }
    model = build_memory(**kwargs)
    expected_states = _independent_memory_states(
        memory,
        directions,
        roots=roots,
        width=width,
        forbidden_words=forbidden_words,
    )
    expected_rows = _independent_memory_rows(
        expected_states,
        directions,
        weights,
        width=width,
        forbidden_words=forbidden_words,
    )
    assert model["states"] == expected_states
    assert model["rows"] == expected_rows
    assert model["symmetry_order"] == 1


def _d4_matrices():
    return tuple(
        sorted(
            {
                (sx, 0, 0, sy)
                for sx in (-1, 1)
                for sy in (-1, 1)
            }
            | {
                (0, sx, sy, 0)
                for sx in (-1, 1)
                for sy in (-1, 1)
            }
        )
    )


def _transform(point, matrix):
    a, b, c, d = matrix
    x, y = point
    return (a * x + b * y, c * x + d * y)


def _canonical_d4(path):
    variants = []
    for matrix in _d4_matrices():
        transformed = tuple(_transform(point, matrix) for point in path)
        x0, y0 = transformed[0]
        variants.append(tuple((x - x0, y - y0) for x, y in transformed))
    return min(variants)


def _independent_d4_model(memory):
    raw_states = _independent_memory_states(memory, SQUARE)
    states = sorted({_canonical_d4(path) for path in raw_states})
    index = {state: position for position, state in enumerate(states)}
    rows = []
    for path in states:
        x, y = path[-1]
        row = Counter()
        for dx, dy in SQUARE:
            point = (x + dx, y + dy)
            if point in path:
                continue
            destination = path[1:] + (point,)
            row[index[_canonical_d4(destination)]] += 1
        rows.append(dict(sorted(row.items())))
    return states, rows


def test_valid_square_d4_quotient_matches_independent_orbit_rows():
    observed = build_memory(3, symmetry="d4", max_seconds=30)
    expected_states, expected_rows = _independent_d4_model(3)
    assert observed["symmetry_order"] == 8
    assert observed["states"] == expected_states
    assert observed["rows"] == expected_rows


def test_anisotropic_weights_reject_d4_and_expose_the_mutant():
    weights = (Fraction(2), Fraction(3), Fraction(2), Fraction(3))
    observed = build_memory(1, weights=weights, symmetry="auto")
    assert observed["symmetry_order"] == 4
    with pytest.raises(ValueError):
        build_memory(1, weights=weights, symmetry="d4")

    # A D4 mutant would merge the one-edge east and north states.  Their
    # corresponding north/east continuations are in the same D4 orbit, but
    # carry weights 3 and 2 respectively.
    east = ((0, 0), (1, 0))
    north = ((0, 0), (0, 1))
    east_then_north = east[1:] + ((1, 1),)
    north_then_east = north[1:] + ((1, 1),)
    assert _canonical_d4(east) == _canonical_d4(north)
    assert _canonical_d4(east_then_north) == _canonical_d4(north_then_east)
    assert weights[1] != weights[0]


def _multiply(rows, vector):
    return [
        sum(Fraction(weight) * vector[destination] for destination, weight in row.items())
        for row in rows
    ]


def _rational_rows():
    return [
        {0: Fraction(1, 2), 1: Fraction(1, 3)},
        {0: Fraction(1, 2), 1: Fraction(1, 3)},
        {2: Fraction(2)},
        {},
    ]


def test_equitable_ap_pb_exact_for_rational_reducible_sinks_and_long_continuations():
    rows = _rational_rows()
    mapping = equitable_partition(rows)
    assert mapping[0] == mapping[1]
    assert len({mapping[0], mapping[2], mapping[3]}) == 3
    reduced = quotient(rows, mapping)
    assert reduced[mapping[0]] == {mapping[0]: Fraction(5, 6)}
    assert reduced[mapping[2]] == {mapping[2]: Fraction(2)}
    assert reduced[mapping[3]] == {}
    assert verify_equitable(rows, mapping, reduced)

    full = lift_vector(mapping, [Fraction(3, 2), Fraction(5, 4), Fraction(7, 3)])
    small = [Fraction(3, 2), Fraction(5, 4), Fraction(7, 3)]
    # The partition stabilizes before this loop; these checks deliberately run
    # far beyond the refinement depth used to construct it.
    for _ in range(24):
        assert _multiply(rows, full) == lift_vector(mapping, _multiply(reduced, small))
        full = _multiply(rows, full)
        small = _multiply(reduced, small)

    certificate = exact_certificate(rows, iterations=7)
    assert verify_bound(rows, certificate)
    empty_certificate = exact_certificate([], iterations=9)
    assert empty_certificate["upper"] == "0"
    assert verify_bound([], empty_certificate)
    assert verify_equitable([], [], [])


def test_random_wrong_partitions_are_rejected_instead_of_defining_a_representative_quotient():
    rows = _rational_rows()
    wrong_partitions = [
        [0, 0, 1, 1],
        [0, 1, 0, 2],
        [0, 1, 2, 0],
    ]
    rng = random.Random(20260912)
    for _ in range(64):
        candidate = [rng.randrange(3) for _ in rows]
        if sorted(set(candidate)) == [0, 1, 2]:
            wrong_partitions.append(candidate)

    rejected = 0
    for mapping in wrong_partitions:
        try:
            quotient(rows, mapping)
        except ValueError:
            rejected += 1
        else:
            # A random partition can accidentally be equitable; the fixed
            # controls above are the required rejection cases.
            assert mapping not in wrong_partitions[:3]
    assert rejected >= 3


def test_discovery_engine_equitable_case_and_resource_limit_have_explicit_status():
    result = memory_case(
        {
            "memory": 2,
            "symmetry": "none",
            "state_representation": "equitable",
            "iterations": 12,
            "max_seconds": 30,
        }
    )
    assert result["status"] == "CERTIFIED"
    assert result["certificate"]["classification"] == "CERTIFIED SPECTRAL BOUND"
    assert result["original_state_count"] >= result["state_count"]

    limited = memory_case(
        {"memory": 1, "symmetry": "none", "max_states": 1, "max_seconds": 30}
    )
    assert limited["status"] == "RESOURCE_LIMIT"
    assert limited["certificate"] is None


def _all_saw_paths(length):
    for word in product(range(4), repeat=length):
        path = [(0, 0)]
        occupied = {(0, 0)}
        x = y = 0
        for direction in word:
            dx, dy = SQUARE[direction]
            x, y = x + dx, y + dy
            point = (x, y)
            if point in occupied:
                break
            occupied.add(point)
            path.append(point)
        else:
            yield tuple(path)


def _is_bridge(path):
    if len(path) < 2:
        return False
    xs = [point[0] for point in path]
    return all(x > 0 for x in xs[1:]) and xs[-1] == max(xs)


def _renewal_cut(path, cut):
    if not 1 <= cut < len(path) - 1:
        return False
    anchor_x, anchor_y = path[cut]
    suffix = tuple((x - anchor_x, y - anchor_y) for x, y in path[cut:])
    return _is_bridge(path[: cut + 1]) and _is_bridge(suffix)


def _independent_bridge_spans(max_n):
    bridges = [{} for _ in range(max_n + 1)]
    irreducibles = [{} for _ in range(max_n + 1)]
    bridges[0] = {0: 1}
    for length in range(1, max_n + 1):
        bridge_row = Counter()
        irreducible_row = Counter()
        for path in _all_saw_paths(length):
            if not _is_bridge(path):
                continue
            span = path[-1][0]
            bridge_row[span] += 1
            if not any(_renewal_cut(path, cut) for cut in range(1, length)):
                irreducible_row[span] += 1
        bridges[length] = dict(sorted(bridge_row.items()))
        irreducibles[length] = dict(sorted(irreducible_row.items()))
    return bridges, irreducibles


def _independent_renewal_inverse(bridges):
    irreducibles = [{} for _ in bridges]
    for length in range(1, len(bridges)):
        row = {}
        for span, bridge_count in bridges[length].items():
            residual = bridge_count
            for piece_length in range(1, length):
                for piece_span, piece_count in irreducibles[piece_length].items():
                    residual -= piece_count * bridges[length - piece_length].get(
                        span - piece_span, 0
                    )
            assert residual >= 0
            if residual:
                row[span] = residual
        irreducibles[length] = row
    return irreducibles


def test_bivariate_bridges_and_geometric_renewal_cuts_match_independent_words_through_n8():
    expected_bridges, expected_irreducibles = _independent_bridge_spans(8)
    observed = enumerate_bridge_spans(8, max_seconds=30)
    assert observed["b_n_s"] == expected_bridges
    assert observed["i_n_s"] == expected_irreducibles
    assert observed["i_n_s"] == _independent_renewal_inverse(expected_bridges)
    assert observed["stats"]["direct_inversion_match"] is True


def test_span_caps_are_exact_filters_of_the_uncapped_dictionary():
    full = enumerate_bridge_spans(8, max_seconds=30)
    for cap in (0, 1, 2, 3, 8):
        capped = enumerate_bridge_spans(8, max_span=cap, max_seconds=30)
        expected_b = [
            {span: count for span, count in row.items() if span <= cap}
            for row in full["b_n_s"]
        ]
        expected_i = [
            {span: count for span, count in row.items() if span <= cap}
            for row in full["i_n_s"]
        ]
        assert capped["b_n_s"] == expected_b
        assert capped["i_n_s"] == expected_i
    assert enumerate_bridge_spans(8, max_span=8, max_seconds=30)["b_n_s"] == full["b_n_s"]


def _concatenate(first, second):
    end_x, end_y = first[-1]
    translated = tuple((end_x + x, end_y + y) for x, y in second[1:])
    return first + translated


def test_strict_initial_minimum_weak_terminal_maximum_and_collision_free_concatenation():
    plateau = ((0, 0), (1, 0), (1, 1), (1, 2))
    assert _is_bridge(plateau)
    assert not all(x < plateau[-1][0] for x, _ in plateau[1:-1])
    assert not _is_bridge(((0, 0), (0, 1), (1, 1)))

    pieces = []
    for length in range(1, 5):
        for path in _all_saw_paths(length):
            if _is_bridge(path) and not any(_renewal_cut(path, cut) for cut in range(1, length)):
                pieces.append(path)
    for first in pieces:
        for second in pieces:
            joined = _concatenate(first, second)
            assert len(set(joined)) == len(joined)
            assert _is_bridge(joined)

    # A suffix that merely stays on the joining x-coordinate is not a bridge;
    # allowing it would permit a translated continuation to collide with the
    # earlier walk.
    first = ((0, 0), (1, 0), (1, 1))
    bad_suffix = ((0, 0), (0, -1))
    joined = _concatenate(first, bad_suffix)
    assert not _is_bridge(bad_suffix)
    assert len(set(joined)) < len(joined)


@pytest.mark.parametrize("value", [float("nan"), float("inf"), -float("inf"), 0, -1, True])
def test_memory_rejects_nonfinite_or_invalid_time_caps(value):
    with pytest.raises(ValueError):
        build_memory(1, max_seconds=value)


@pytest.mark.parametrize("value", [0, -1, True, 1.0])
def test_memory_rejects_invalid_state_caps(value):
    with pytest.raises(ValueError):
        build_memory(1, max_states=value)


@pytest.mark.parametrize("value", [float("nan"), float("inf"), -float("inf"), 0, -1, True])
def test_bridge_spans_rejects_nonfinite_or_invalid_time_caps(value):
    with pytest.raises(ValueError):
        enumerate_bridge_spans(2, max_seconds=value)


@pytest.mark.parametrize("value", [-1, True])
def test_bridge_spans_rejects_invalid_integer_bounds(value):
    with pytest.raises(ValueError):
        enumerate_bridge_spans(value)
    with pytest.raises(ValueError):
        enumerate_bridge_spans(2, max_span=value)
