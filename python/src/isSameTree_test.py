from typing import List, Optional

import pytest

from isSameTree import Solution
from leetcode import build_tree

solution = Solution()


@pytest.mark.parametrize(
    "p,q,want",
    (
        ([1, 2, 3], [1, 2, 3], True),
        ([1, 2], [1, None, 2], False),
        ([1, 2, 1], [1, 1, 2], False),
        ([], [0], False),
        ([10, 5, 15], [10, 5, None, None, 15], False),
    ),
)
def test_isSameTree(p: List[Optional[int]], q: List[Optional[int]], want: bool):
    p = build_tree(p)
    q = build_tree(q)
    got = solution.isSameTree(p, q)
    assert got == want
