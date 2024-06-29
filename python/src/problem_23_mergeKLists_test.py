from collections.abc import Callable

import pytest
from leetcode import build_list, iter_list
from problem_23_mergeKLists import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    [
        (solution.mergeKLists),
        (solution.mergeKLists_heap),
    ],
)
@pytest.mark.parametrize(
    ("lists", "want"),
    [
        ([[1, 4, 5], [1, 3, 4], [2, 6]], [1, 1, 2, 3, 4, 4, 5, 6]),
        ([], []),
        ([[]], []),
        ([[1], [0]], [0, 1]),
    ],
)
def test_mergeKLists(fn: Callable, lists: list[list[int]], want: list[int]) -> None:
    lls = [build_list(x) for x in lists]
    got_lls = fn(lls)
    got = list(iter_list(got_lls))
    assert got == want
