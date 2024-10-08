from collections.abc import Callable

import pytest

from problem_268_missingNumber import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    [
        (solution.missingNumber),
        (solution.missingNumber_gauss),
    ],
)
@pytest.mark.parametrize(
    ("given", "want"),
    [
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
    ],
)
def test_missingNumber(fn: Callable, given: list[int], want: int) -> None:
    got = fn(given)
    assert got == want
