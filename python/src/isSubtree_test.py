import pytest

from isSubtree import Solution
from leetcode import build_tree

solution = Solution()


@pytest.mark.parametrize(
    "root, subRoot, want",
    (
        (
            [3, 4, 5, 1, 2],
            [4, 1, 2],
            True,
        ),
        (
            [3, 4, 5, 1, 2, None, None, None, None, 0],
            [4, 1, 2],
            False,
        ),
    ),
)
def test_isSubtree(root, subRoot, want):
    root = build_tree(root)
    subRoot = build_tree(subRoot)
    got = solution.isSubtree(root, subRoot)
    assert got == want
