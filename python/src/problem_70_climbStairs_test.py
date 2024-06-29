from collections.abc import Callable

import pytest
from problem_70_climbStairs import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    (
        (solution.climbStairs_dp),
        (solution.climbStairs_memo),
    ),
)
@pytest.mark.parametrize(
    "n,want",
    (
        (1, 1),
        (2, 2),
        (3, 3),
        (4, 5),
        (5, 8),
        (45, 1836311903),
    ),
)
def test_climbStairs(fn: Callable, n: int, want: int) -> None:
    got = fn(n)
    assert got == want
