from collections.abc import Callable

import pytest
from problem_287_findDuplicate import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    (
        (solution.findDuplicate),
        (solution.findDuplicate_floyd),
    ),
)
@pytest.mark.parametrize(
    "nums, want",
    (
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
    ),
)
def test_findDuplicate(fn: Callable, nums: list[int], want: int):
    got = fn(nums)
    assert got == want
