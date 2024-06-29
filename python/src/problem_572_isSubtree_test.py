from typing import NamedTuple

import pytest
from leetcode import build_tree
from problem_572_isSubtree import Solution

solution = Solution()


class T(NamedTuple):
    tree1: list[int | None]
    tree2: list[int | None]
    want: bool


@pytest.mark.parametrize(
    "t",
    [
        T(
            [3, 4, 5, 1, 2],
            [4, 1, 2],
            True,
        ),
        T(
            [3, 4, 5, 1, 2, None, None, None, None, 0],
            [4, 1, 2],
            False,
        ),
    ],
)
def test_isSubtree(t: T) -> None:
    root = build_tree(t.tree1)
    subRoot = build_tree(t.tree2)
    got = solution.isSubtree(root, subRoot)
    assert got == t.want
