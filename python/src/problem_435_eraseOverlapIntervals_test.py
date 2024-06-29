from typing import List

import pytest
from problem_435_eraseOverlapIntervals import Solution

solution = Solution()


@pytest.mark.parametrize(
    "intervals, want",
    (
        ([[1, 2], [2, 3], [3, 4], [1, 3]], 1),
        ([[1, 2], [1, 2], [1, 2]], 2),
        ([[1, 2], [2, 3]], 0),
    ),
)
def test_eraseOverlapIntervals(intervals: List[List[int]], want: bool):
    got = solution.eraseOverlapIntervals(intervals)
    assert got == want
