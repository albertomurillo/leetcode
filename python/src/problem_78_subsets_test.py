from collections.abc import Callable

import pytest

from problem_78_subsets import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    [
        (solution.subsets),
        (solution.subsets_python),
    ],
)
@pytest.mark.parametrize(
    ("nums", "want"),
    [
        ([1, 2, 3], [[], [1], [2], [1, 2], [3], [1, 3], [2, 3], [1, 2, 3]]),
        ([0], [[], [0]]),
    ],
)
def test_subsets(fn: Callable, nums: list[int], want: list[int]) -> None:
    got = fn(nums)
    assert sorted(got) == sorted(want)
