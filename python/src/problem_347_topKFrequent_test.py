from collections.abc import Callable

import pytest

from problem_347_topKFrequent import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    [
        (solution.topKFrequent),
        (solution.topKFrequent_python),
    ],
)
@pytest.mark.parametrize(
    ("nums", "k", "want"),
    [
        ([1, 1, 1, 2, 2, 3], 2, [1, 2]),
        ([1], 1, [1]),
        ([3, 0, 1, 0], 1, [0]),
    ],
)
def test_topKFrequent(fn: Callable, nums: list[int], k: int, want: list[int]) -> None:
    got = fn(nums, k)
    assert got == want
