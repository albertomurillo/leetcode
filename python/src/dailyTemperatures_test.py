from typing import List

import pytest

from dailyTemperatures import Solution

solution = Solution()


@pytest.mark.parametrize(
    "temperatures, want",
    (
        (
            [73, 74, 75, 71, 69, 72, 76, 73],
            [1, 1, 4, 2, 1, 1, 0, 0],
        ),
        (
            [30, 40, 50, 60],
            [1, 1, 1, 0],
        ),
        (
            [30, 60, 90],
            [1, 1, 0],
        ),
    ),
)
def test_dailyTemperatures(temperatures: List[int], want: List[int]):
    got = solution.dailyTemperatures(temperatures)
    assert got == want
