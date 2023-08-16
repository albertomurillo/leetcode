import copy
from typing import List

import pytest

from rotate import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    (
        (solution.rotate),
        (solution.rotate_inplace),
        (solution.rotate_array),
        (solution.rotate_deque),
    ),
)
@pytest.mark.parametrize(
    "nums, k, want",
    (
        ([1, 2, 3, 4, 5, 6, 7], 3, [5, 6, 7, 1, 2, 3, 4]),
        ([-1, -100, 3, 99], 2, [3, 99, -1, -100]),
        ([1, 2, 3], 4, [3, 1, 2]),
        ([1, 2], 0, [1, 2]),
        ([1, 2, 3, 4, 5, 6], 4, [3, 4, 5, 6, 1, 2]),
    ),
)
def test_rotate(fn: callable, nums: List[int], k: int, want: List[int]):
    nums_copy = copy.deepcopy(nums)
    fn(nums_copy, k)
    assert nums_copy == want
