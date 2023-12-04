from typing import List

import pytest

from problem_121_maxProfit import Solution

solution = Solution()


@pytest.mark.parametrize(
    "prices, want",
    (
        ([7, 1, 5, 3, 6, 4], 5),
        ([7, 6, 4, 3, 1], 0),
    ),
)
def test_maxProfit(prices: List[int], want: int):
    got = solution.maxProfit(prices)
    assert got == want
