from typing import List, Optional

import pytest
from leetcode import build_tree
from problem_230_kthSmallest import Solution

solution = Solution()


@pytest.mark.parametrize(
    "root, k, want",
    (
        ([3, 1, 4, None, 2], 1, 1),
        ([5, 3, 6, 2, 4, None, None, 1], 3, 3),
    ),
)
def test_kthSmallest(root: List[Optional[int]], k: int, want: int):
    tree = build_tree(root)
    assert tree
    got = solution.kthSmallest(tree, k)
    assert got == want
