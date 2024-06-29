from typing import List

import pytest
from problem_53_maxSubArray import Solution

solution = Solution()


@pytest.mark.parametrize(
    "nums, want",
    (
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),
    ),
)
def test_maxSubArray(nums: List[int], want: int):
    got = solution.maxSubArray(nums)
    assert got == want
