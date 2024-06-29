from collections.abc import Callable

import pytest
from problem_238_productExceptSelf import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    (
        (solution.productExceptSelf),
        (solution.productExceptSelf_naive),
    ),
)
@pytest.mark.parametrize(
    "nums, want",
    (
        ([1, 2, 3, 4], [24, 12, 8, 6]),
        ([-1, 1, 0, -3, 3], [0, 0, 9, 0, 0]),
    ),
)
def test_productExceptSelf(fn: Callable, nums: list[int], want: list[int]) -> None:
    got = fn(nums)
    assert got == want
