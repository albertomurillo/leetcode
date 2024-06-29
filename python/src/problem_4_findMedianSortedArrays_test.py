from collections.abc import Callable

import pytest
from problem_4_findMedianSortedArrays import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    [
        (solution.findMedianSortedArrays),
        (solution.findMedianSortedArrays_ptrs),
        (solution.findMedianSortedArrays_naive),
    ],
)
@pytest.mark.parametrize(
    ("nums1", "nums2", "want"),
    [
        ([1, 3], [2], 2.0),
        ([1, 2], [3, 4], 2.5),
    ],
)
def test_findMedianSortedArrays(
    fn: Callable, nums1: list[int], nums2: list[int], want: float
) -> None:
    got = fn(nums1, nums2)
    assert got == want
