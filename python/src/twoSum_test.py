from typing import List

import pytest

from twoSum import Solution


@pytest.mark.parametrize(
    "nums, target, want",
    (
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ),
)
def test_twoSum(nums: List[int], target: int, want: List[int]):
    solution = Solution()
    got = solution.twoSum(nums, target)
    assert got == want
