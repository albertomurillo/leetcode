# https://leetcode.com/problems/sudoku-solver/


from typing import List

import pytest

from problem_136_singleNumber import Solution

solution = Solution()


@pytest.mark.parametrize(
    "nums, want",
    (
        ([2, 2, 1], 1),
        ([4, 1, 2, 1, 2], 4),
        ([1], 1),
    ),
)
def test_singleNumber(nums: List[int], want: int):
    got = solution.singleNumber(nums)
    assert got == want
