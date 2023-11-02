from typing import List

import pytest

from diameterOfBinaryTree import Solution
from leetcode import TreeNode

solution = Solution()


@pytest.mark.parametrize(
    "given, want",
    (
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1),
    ),
)
def test_diameterOfBinaryTree(given: List[int], want: int):
    tree = TreeNode(given[0])
    for val in given[1:]:
        tree.level_order_insert(val)

    got = solution.diameterOfBinaryTree(tree)
    assert got == want
