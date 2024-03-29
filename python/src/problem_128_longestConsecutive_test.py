from typing import List

import pytest

from problem_128_longestConsecutive import Solution

solution = Solution()


@pytest.mark.parametrize(
    "nums, want",
    (
        ([100, 4, 200, 1, 3, 2], 4),
        ([0, 3, 7, 2, 5, 8, 4, 6, 0, 1], 9),
    ),
)
def test_longestConsecutive(nums: List[int], want: int):
    got = solution.longestConsecutive(nums)
    assert got == want
