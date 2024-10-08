from collections.abc import Callable

import pytest

from problem_1155_numRollsToTarget import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    [
        (solution.numRollsToTarget),
        (solution.numRollsToTarget_dp),
    ],
)
@pytest.mark.parametrize(
    ("n", "k", "target", "want"),
    [
        (1, 6, 3, 1),
        (2, 6, 7, 6),
        (30, 30, 500, 222616187),
    ],
)
def test_numRollsToTarget(fn: Callable, n: int, k: int, target: int, want: int) -> None:
    got = fn(n, k, target)
    assert got == want
