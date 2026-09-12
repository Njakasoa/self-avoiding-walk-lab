"""A small exact occupation-state transfer matrix for finite rectangles.

This is deliberately a simple baseline.  A state stores the complete set of
vertices occupied so far as a Python integer bitmask, together with the current
endpoint.  Equal ``(occupied_mask, endpoint)`` states are merged by summing
their exact integer multiplicities.  Keeping all occupied vertices makes the
state representation easy to audit, at the cost of the exponential growth
that a production frontier/connectivity transfer matrix avoids.
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
    if isinstance(value, bool) or not isinstance(value, int) or value < 0:
        raise ValueError(f"{name} must be a nonnegative integer")
    return value


def _require_positive_integer(name: str, value: int) -> int:
    if isinstance(value, bool) or not isinstance(value, int) or value <= 0:
        raise ValueError(f"{name} must be a positive integer")
    return value


def _neighbors(width: int, height: int) -> tuple[tuple[int, ...], ...]:
    """Return lattice-neighbor indices in deterministic direction order."""

    result: list[tuple[int, ...]] = []
    for endpoint in range(width * height):
        x, y = endpoint % width, endpoint // width
        destinations: list[int] = []
        for dx, dy in _DIRECTIONS:
            nx, ny = x + dx, y + dy
            if 0 <= nx < width and 0 <= ny < height:
                destinations.append(ny * width + nx)
        result.append(tuple(destinations))
    return tuple(result)


def transfer_counts(width: int, height: int, max_n: int) -> list[int]:
    """Count rooted oriented SAWs in a finite rectangular vertex set.

    The rectangle is ``{0, ..., width - 1} × {0, ..., height - 1}``, with
    root ``(0, 0)``.  ``width`` and ``height`` count vertices.  The returned
    list contains one exact integer per length from zero through ``max_n``;
    lengths beyond the ``width * height - 1`` edge maximum are zero.

    At layer ``n``, ``states[(mask, endpoint)]`` is the number of length-
    ``n`` walks having exactly that occupied set and endpoint.  Extending only
    to an unoccupied lattice neighbor preserves self-avoidance, and merging
    equal destination states is the transfer step.
    """

    width = _require_positive_integer("width", width)
    height = _require_positive_integer("height", height)
    max_n = _require_nonnegative_integer("max_n", max_n)

    result = [1]
    if max_n == 0 or width * height == 1:
        result.extend([0] * max_n)
        return result

    neighbors = _neighbors(width, height)
    # Bit i represents the vertex with index y * width + x.  The corner root
    # is therefore bit zero and endpoint zero.
    states: dict[tuple[int, int], int] = {(1, 0): 1}

    for _length in range(1, max_n + 1):
        next_states: dict[tuple[int, int], int] = {}
        for (occupied, endpoint), ways in states.items():
            for destination in neighbors[endpoint]:
                bit = 1 << destination
                if occupied & bit:
                    continue
                state = (occupied | bit, destination)
                next_states[state] = next_states.get(state, 0) + ways
        states = next_states
        result.append(sum(states.values()))
        if not states:
            # No longer path can exist; fill the requested tail without
            # repeatedly constructing empty dictionaries.
            result.extend([0] * (max_n - _length))
            break

    return result


__all__ = ["transfer_counts"]
