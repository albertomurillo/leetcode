from typing import Callable, List, Optional

import pytest

from leetcode import build_tree
from problem_226_invertTree import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    (
        (solution.invertTree),
        (solution.invertTree_stack),
    ),
)
@pytest.mark.parametrize(
    "root, want",
    (
        ([4, 2, 7, 1, 3, 6, 9], [4, 7, 2, 9, 6, 3, 1]),
        ([2, 1, 3], [2, 3, 1]),
        ([], []),
    ),
)
def test_invertTree(fn: Callable, root: List[Optional[int]], want: bool):
    tree = build_tree(root)
    fn(tree)
    got = list(tree.level_order_traversal()) if tree else []
    assert got == want
