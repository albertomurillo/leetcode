from collections.abc import Callable

import pytest

from problem_46_permute import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    [
        (solution.permute),
        (solution.permute_python),
    ],
)
@pytest.mark.parametrize(
    ("given", "want"),
    [
        ([0, 1], [[0, 1], [1, 0]]),
        ([1], [[1]]),
        ([1, 2, 3], [[1, 2, 3], [1, 3, 2], [2, 1, 3], [2, 3, 1], [3, 1, 2], [3, 2, 1]]),
    ],
)
def test_permute(fn: Callable, given: list[int], want: list[list[int]]) -> None:
    got = fn(given)
    assert sorted(got) == sorted(want)
