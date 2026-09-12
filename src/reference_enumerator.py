"""Clear exact reference enumerators for square-lattice self-avoiding walks.

The canonical object is an oriented walk ``(omega_0, ..., omega_n)`` with
``omega_0 == (0, 0)`` and pairwise distinct vertices.  Rotations and
reflections are counted separately.  ``counts`` uses a single depth-first
traversal, recording every prefix, so the returned entry at index ``n`` is
the exact integer ``c_n``.

``rectangle_counts`` is an independent finite-box variant.  Its allowed
vertices are ``{0, ..., width - 1} x {0, ..., height - 1}`` and its root is
the lower-left corner ``(0, 0)``.  The dimensions count vertices, rather than
edges.  A finite-box result is a finite exact count and is not an estimate of
the infinite-lattice connective constant.
"""

from __future__ import annotations

from typing import Final

_DIRECTIONS: Final[tuple[tuple[int, int], ...]] = (
    (1, 0),
    (0, 1),
    (-1, 0),
    (0, -1),
)


def _require_nonnegative_integer(name: str, value: int) -> int:
    """Validate an integer parameter without silently accepting booleans."""

    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


def _require_positive_integer(name: str, value: int) -> int:
    """Validate a positive integer parameter without silently accepting booleans."""

    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def counts(max_n: int) -> list[int]:
    """Return the exact square-lattice counts ``[c_0, ..., c_max_n]``.

    A path is rooted at the origin and oriented by its order of traversal;
    no symmetry quotient is applied.  The DFS counts a path when it reaches
    each depth and then extends that same path, which means all requested
    lengths are obtained in one traversal.

    Parameters
    ----------
    max_n:
        Largest number of edges to enumerate.  It must be a nonnegative
        integer.

    Returns
    -------
    list[int]
        Exact counts, with ``result[0] == 1``.
    """

    max_n = _require_nonnegative_integer("max_n", max_n)
    result = [0] * (max_n + 1)
    result[0] = 1

    # The path and set are mutated in place.  The recursive function is kept
    # deliberately direct so this file remains an auditable reference rather
    # than a performance implementation.
    path = [(0, 0)]
    visited = {(0, 0)}

    def visit(x: int, y: int, depth: int) -> None:
        if depth == max_n:
            return
        for dx, dy in _DIRECTIONS:
            nxt = (x + dx, y + dy)
            if nxt in visited:
                continue
            visited.add(nxt)
            path.append(nxt)
            result[depth + 1] += 1
            visit(nxt[0], nxt[1], depth + 1)
            path.pop()
            visited.remove(nxt)

    visit(0, 0, 0)
    return result


def rectangle_counts(width: int, height: int, max_n: int) -> list[int]:
    """Return exact rooted SAW counts inside a finite rectangular vertex set.

    The allowed set is ``0 <= x < width`` and ``0 <= y < height``; the root
    is ``(0, 0)``.  Every walk is oriented, and no rotations or reflections
    are identified.  Counts after the maximum possible simple-walk length
    are zero, while the returned list always has length ``max_n + 1``.

    This intentionally mirrors :func:`counts` with only the boundary check
    added.  :mod:`src.transfer_matrix` provides a separate dynamic-programming
    implementation for cross-validation.
    """

    width = _require_positive_integer("width", width)
    height = _require_positive_integer("height", height)
    max_n = _require_nonnegative_integer("max_n", max_n)

    result = [0] * (max_n + 1)
    result[0] = 1

    path = [(0, 0)]
    visited = {(0, 0)}

    def visit(x: int, y: int, depth: int) -> None:
        if depth == max_n:
            return
        for dx, dy in _DIRECTIONS:
            nx, ny = x + dx, y + dy
            if not (0 <= nx < width and 0 <= ny < height):
                continue
            nxt = (nx, ny)
            if nxt in visited:
                continue
            visited.add(nxt)
            path.append(nxt)
            result[depth + 1] += 1
            visit(nx, ny, depth + 1)
            path.pop()
            visited.remove(nxt)

    visit(0, 0, 0)
    return result


__all__ = ["counts", "rectangle_counts"]
