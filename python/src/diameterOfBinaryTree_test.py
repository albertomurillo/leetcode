from typing import List

import pytest

from diameterOfBinaryTree import Solution
from leetcode import build_tree

solution = Solution()


@pytest.mark.parametrize(
    "root, want",
    (
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1),
    ),
)
def test_diameterOfBinaryTree(root: List[int], want: int):
    tree = build_tree(root)
    got = solution.diameterOfBinaryTree(tree)
    assert got == want
