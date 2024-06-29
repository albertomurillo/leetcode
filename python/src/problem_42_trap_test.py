from collections.abc import Callable

import pytest
from problem_42_trap import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    (
        (solution.trap),
        (solution.trap_array),
        (solution.trap_naive),
    ),
)
@pytest.mark.parametrize(
    "given, want",
    (
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
    ),
)
def test_majorityElement(fn: Callable, given: list[int], want: int) -> None:
    got = fn(given)
    assert got == want
