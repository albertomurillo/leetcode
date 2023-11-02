from typing import Callable, List, Optional

import pytest

from leetcode import build_tree
from maxDepth import Solution

solution = Solution()


@pytest.mark.parametrize(
    "fn",
    (
        (solution.maxDepth),
        (solution.maxDepth_stack),
    ),
)
@pytest.mark.parametrize(
    "root, want",
    (
        ([3, 9, 20, None, None, 15, 7], 3),
        ([1, None, 2], 2),
    ),
)
def test_maxDepth(fn: Callable, root: List[Optional[int]], want: int):
    tree = build_tree(root)
    got = fn(tree)
    assert got == want
