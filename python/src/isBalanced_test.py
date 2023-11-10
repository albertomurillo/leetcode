from typing import List, Optional

import pytest

from isBalanced import Solution
from leetcode import build_tree

solution = Solution()


@pytest.mark.parametrize(
    "root, want",
    (
        ([3, 9, 20, None, None, 15, 7], True),
        ([1, 2, 2, 3, 3, None, None, 4, 4], False),
        ([], True),
    ),
)
def test_isBalanced(root: List[Optional[int]], want: bool):
    _root = build_tree(root)
    got = solution.isBalanced(_root)
    assert got == want
