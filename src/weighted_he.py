"""Independent exact reproduction of He's square-lattice ``m=1`` matrices.

The implementation deliberately does not build on the finite-memory engine.
For each fixed first step (east or north), it enumerates the full ``n``-step
walks, classifies the final step as horizontal or vertical, sums the exact
monomial weights, and divides each row by the weight of its fixed one-step
prefix.  The resulting two by two SymPy matrix is He's ``G^P(1,n)`` for the
sign-flip classes.  ``mode='saw'`` forbids repeated vertices; ``mode='sat'``
forbids repeated undirected edges and therefore permits vertex revisits.

Only strictly positive weights belong to He's theorem.  The symbolic default
uses positive SymPy symbols, while explicit nonpositive axes are rejected by
this module and handled separately by the E3 experiment's direct axis check.
"""

from __future__ import annotations

from fractions import Fraction
from typing import Any

import sympy as sp


DIRECTIONS = ((1, 0), (0, 1), (-1, 0), (0, -1))
DEFAULT_X, DEFAULT_Y = sp.symbols("x y", positive=True)

__all__ = [
    "DEFAULT_X",
    "DEFAULT_Y",
    "build_he_matrix",
    "enumerate_he_matrix",
    "he_matrix",
    "table1_bound",
    "table1_invariants",
    "matrix_invariants",
    "compare_table1",
    "validate_table1",
]


def _mode(mode: str, trail: bool | None = None) -> str:
    """Normalize the public SAW/SAT spelling and optional trail flag."""

    if trail is not None:
        if type(trail) is not bool:
            raise TypeError("trail must be a bool when supplied")
        mode = "sat" if trail else "saw"
    if not isinstance(mode, str):
        raise TypeError("mode must be 'saw' or 'sat'")
    normalized = mode.lower()
    if normalized in {"saw", "walk", "self_avoiding_walk"}:
        return "saw"
    if normalized in {"sat", "trail", "self_avoiding_trail"}:
        return "sat"
    raise ValueError("mode must be 'saw' or 'sat'")


def _positive_exact(value: Any, name: str) -> sp.Expr:
    """Sympify an exact positive weight, rejecting floats and known axes."""

    if isinstance(value, (bool, float, complex)):
        raise TypeError(f"{name} must be an exact positive weight")
    try:
        expression = sp.sympify(value)
    except (TypeError, ValueError) as exc:
        raise TypeError(f"{name} must be an exact SymPy-compatible weight") from exc
    if expression.is_Float:
        raise TypeError(f"{name} must not be a floating-point value")
    if expression.is_real is False:
        raise ValueError(f"{name} must be real")
    if expression.is_zero is True or expression.is_negative is True:
        raise ValueError(f"{name} must be strictly positive")
    # A formal symbol with no positivity assumption is accepted for exact
    # symbolic reproduction; numerical theorem use must substitute a positive
    # rational value.
    return expression


def _edge(a: tuple[int, int], b: tuple[int, int]) -> tuple[tuple[int, int], tuple[int, int]]:
    """Canonical undirected edge key for trail self-avoidance."""

    return (a, b) if a <= b else (b, a)


def _step_weight(direction: tuple[int, int], x: sp.Expr, y: sp.Expr) -> sp.Expr:
    return x if direction[0] else y


def _row_for_prefix(
    first: tuple[int, int],
    n: int,
    *,
    mode: str,
    x: sp.Expr,
    y: sp.Expr,
) -> list[sp.Expr]:
    """Enumerate one fixed east/north-prefix row independently."""

    origin = (0, 0)
    endpoint = first
    initial_weight = _step_weight(first, x, y)
    vertices = {origin, endpoint}
    edges = {_edge(origin, endpoint)}
    totals = [sp.Integer(0), sp.Integer(0)]  # final horizontal, final vertical

    def visit(
        current: tuple[int, int],
        depth: int,
        weight: sp.Expr,
        seen_vertices: set[tuple[int, int]],
        seen_edges: set[tuple[tuple[int, int], tuple[int, int]]],
        last_direction: tuple[int, int],
    ) -> None:
        if depth == n:
            totals[0 if last_direction[0] else 1] += weight
            return
        for direction in DIRECTIONS:
            destination = (current[0] + direction[0], current[1] + direction[1])
            edge = _edge(current, destination)
            if mode == "saw":
                if destination in seen_vertices:
                    continue
            elif edge in seen_edges:
                continue
            next_vertices = seen_vertices
            next_edges = seen_edges
            if mode == "saw":
                next_vertices = seen_vertices | {destination}
            else:
                next_edges = seen_edges | {edge}
            visit(
                destination,
                depth + 1,
                weight * _step_weight(direction, x, y),
                next_vertices,
                next_edges,
                direction,
            )

    visit(endpoint, 1, initial_weight, vertices, edges, first)
    return [sp.expand(value) for value in totals]


def build_he_matrix(
    m: int,
    n: int,
    *,
    mode: str = "saw",
    kind: str | None = None,
    trail: bool | None = None,
    x: Any = DEFAULT_X,
    y: Any = DEFAULT_Y,
) -> sp.Matrix:
    """Build He's exact two-class matrix for ``m=1`` and ``n=2,3,4``.

    The two rows use fixed prefixes ``+e_x`` and ``+e_y``.  The two columns
    classify the final one-step tail by its horizontal or vertical direction,
    including both signs.  Each row is divided by its initial prefix weight.
    For ``n=4``, SAW and SAT differ; for ``n=2,3`` their matrices coincide.
    """

    if type(m) is not int or m != 1:
        raise ValueError("this independent reproduction supports m=1 only")
    if type(n) is not int or n not in {2, 3, 4}:
        raise ValueError("n must be one of 2, 3, or 4")
    if kind is not None:
        if mode != "saw" and _mode(mode) != _mode(kind):
            raise ValueError("mode and kind request different walk objects")
        mode = kind
    normalized_mode = _mode(mode, trail)
    x_expr = _positive_exact(x, "x")
    y_expr = _positive_exact(y, "y")
    rows = [
        _row_for_prefix(DIRECTIONS[0], n, mode=normalized_mode, x=x_expr, y=y_expr),
        _row_for_prefix(DIRECTIONS[1], n, mode=normalized_mode, x=x_expr, y=y_expr),
    ]
    prefixes = (x_expr, y_expr)
    return sp.Matrix(
        [
            [sp.cancel(value / prefix) for value in row]
            for row, prefix in zip(rows, prefixes)
        ]
    )


def he_matrix(
    m_or_n: int,
    n: int | None = None,
    *,
    mode: str = "saw",
    kind: str | None = None,
    trail: bool | None = None,
    x: Any = DEFAULT_X,
    y: Any = DEFAULT_Y,
) -> sp.Matrix:
    """Convenience wrapper accepting ``he_matrix(n)`` or ``he_matrix(1,n)``."""

    if n is None:
        return build_he_matrix(1, m_or_n, mode=mode, kind=kind, trail=trail, x=x, y=y)
    return build_he_matrix(m_or_n, n, mode=mode, kind=kind, trail=trail, x=x, y=y)


def _table1_trace_discriminant(
    n: int, mode: str, x: sp.Expr, y: sp.Expr
) -> tuple[sp.Expr, sp.Expr]:
    """Return Table 1's exact trace and characteristic discriminant."""

    r = x**2 + 14 * x * y + y**2
    if n == 2:
        return x + y, r
    if n == 3:
        trace = x**2 + 8 * x * y + y**2
        return trace, (x + y) ** 2 * r
    if n == 4:
        trace = x**3 + 12 * x * y * (x + y) + y**3
        if mode == "saw":
            discriminant = (
                x**6
                + 24 * x**5 * y
                + 136 * x**4 * y**2
                + 254 * x**3 * y**3
                + 136 * x**2 * y**4
                + 24 * x * y**5
                + y**6
            )
        else:
            discriminant = (x**2 + 5 * x * y + y**2) ** 2 * r
        return trace, discriminant
    raise ValueError("n must be one of 2, 3, or 4")


def table1_invariants(
    n: int,
    *,
    mode: str = "saw",
    trail: bool | None = None,
    x: Any = DEFAULT_X,
    y: Any = DEFAULT_Y,
) -> dict[str, sp.Expr]:
    """Return Table 1's exact trace/discriminant for the requested case."""

    normalized_mode = _mode(mode, trail)
    x_expr = _positive_exact(x, "x")
    y_expr = _positive_exact(y, "y")
    trace, discriminant = _table1_trace_discriminant(n, normalized_mode, x_expr, y_expr)
    return {"trace": sp.expand(trace), "discriminant": sp.expand(discriminant)}


def matrix_invariants(matrix: sp.Matrix) -> dict[str, sp.Expr]:
    """Return exact trace and ``trace**2 - 4*det`` for a two by two matrix."""

    if not isinstance(matrix, sp.MatrixBase) or matrix.shape != (2, 2):
        raise ValueError("matrix must be a two by two SymPy matrix")
    trace = sp.expand(sp.trace(matrix))
    discriminant = sp.factor(trace**2 - 4 * matrix.det())
    return {"trace": trace, "discriminant": discriminant}


def compare_table1(
    n: int,
    *,
    mode: str = "saw",
    trail: bool | None = None,
    x: Any = DEFAULT_X,
    y: Any = DEFAULT_Y,
) -> dict[str, object]:
    """Compare independently enumerated invariants with Table 1 exactly."""

    normalized_mode = _mode(mode, trail)
    matrix = build_he_matrix(1, n, mode=normalized_mode, x=x, y=y)
    actual = matrix_invariants(matrix)
    expected = table1_invariants(n, mode=normalized_mode, x=x, y=y)
    trace_difference = sp.simplify(actual["trace"] - expected["trace"])
    discriminant_difference = sp.simplify(
        actual["discriminant"] - expected["discriminant"]
    )
    return {
        "matrix": matrix,
        "actual": actual,
        "expected": expected,
        "trace_difference": trace_difference,
        "discriminant_difference": discriminant_difference,
        "trace_ok": trace_difference == 0,
        "discriminant_ok": discriminant_difference == 0,
        "ok": trace_difference == 0 and discriminant_difference == 0,
    }


def validate_table1(
    n: int,
    *,
    mode: str = "saw",
    trail: bool | None = None,
    x: Any = DEFAULT_X,
    y: Any = DEFAULT_Y,
) -> dict[str, object]:
    """Run an exact Table 1 comparison and raise if either invariant differs."""

    result = compare_table1(n, mode=mode, trail=trail, x=x, y=y)
    if not result["ok"]:
        raise AssertionError(
            f"Table 1 mismatch for mode={_mode(mode, trail)!r}, n={n}: "
            f"trace diff={result['trace_difference']}, "
            f"discriminant diff={result['discriminant_difference']}"
        )
    return result


def table1_bound(
    n: int,
    *,
    mode: str = "saw",
    trail: bool | None = None,
    x: Any = DEFAULT_X,
    y: Any = DEFAULT_Y,
) -> sp.Expr:
    """Return the exact Table 1 expression ``((tr+sqrt(D))/2)**(1/(n-1))``."""

    normalized_mode = _mode(mode, trail)
    invariants = table1_invariants(n, mode=normalized_mode, x=x, y=y)
    degree = sp.Rational(1, n - 1)
    return sp.Pow(
        sp.Rational(1, 2)
        * (invariants["trace"] + sp.sqrt(invariants["discriminant"])),
        degree,
    )


# Descriptive alias for callers that want to emphasize independent
# enumeration rather than the matrix formula itself.
enumerate_he_matrix = build_he_matrix
