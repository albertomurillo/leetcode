from typing import Callable, List

import pytest

from findKthLargest import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    (
        (solution.findKthLargest),
        (solution.findKthLargest_python),
    ),
)
@pytest.mark.parametrize(
    "nums, k, want",
    (
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ),
)
def test_findKthLargest(fn: Callable, nums: List[int], k: int, want: int):
    got = fn(nums, k)
    assert got == want
