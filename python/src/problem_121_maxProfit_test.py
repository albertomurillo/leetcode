from collections.abc import Callable

import pytest

from problem_121_maxProfit import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    [
        (solution.maxProfit),
        (solution.maxProfit_two_ptrs),
    ],
)
@pytest.mark.parametrize(
    ("prices", "want"),
    [
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ],
)
def test_maxProfit(fn: Callable, prices: list[int], want: int) -> None:
    got = fn(prices)
    assert got == want
