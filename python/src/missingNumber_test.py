from typing import Callable, List

import pytest

from missingNumber import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    (
        (solution.missingNumber),
        (solution.missingNumber_gauss),
    ),
)
@pytest.mark.parametrize(
    "given, want",
    (
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ),
)
def test_missingNumber(fn: Callable, given: List[int], want: int):
    got = fn(given)
    assert got == want
