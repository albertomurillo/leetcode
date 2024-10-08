from collections.abc import Callable

import pytest

from problem_215_findKthLargest import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    [
        (solution.findKthLargest),
        (solution.findKthLargest_python),
    ],
)
@pytest.mark.parametrize(
    ("nums", "k", "want"),
    [
        ([3, 2, 1, 5, 6, 4], 2, 5),
        ([3, 2, 3, 1, 2, 4, 5, 5, 6], 4, 4),
    ],
)
def test_findKthLargest(fn: Callable, nums: list[int], k: int, want: int) -> None:
    got = fn(nums, k)
    assert got == want
