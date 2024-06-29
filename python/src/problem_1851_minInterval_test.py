from typing import List

import pytest
from problem_1851_minInterval import Solution

solution = Solution()


@pytest.mark.parametrize(
    "intervals, queries, want",
    (
        (
            [[1, 4], [2, 4], [3, 6], [4, 4]],
            [2, 3, 4, 5],
            [3, 3, 1, 4],
        ),
        (
            [[2, 3], [2, 5], [1, 8], [20, 25]],
            [2, 19, 5, 22],
            [2, -1, 4, 6],
        ),
    ),
)
def test_minInterval(intervals: List[List[int]], queries: List[int], want: List[int]):
    got = solution.minInterval(intervals, queries)
    assert got == want
