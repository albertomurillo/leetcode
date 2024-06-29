import pytest
from leetcode import build_tree
from problem_1372_longestZigZag import Solution

solution = Solution()


@pytest.mark.parametrize(
    "root,want",
    (
        (
            [1, None, 1, 1, 1, None, None, 1, 1, None, 1, None, None, None, 1],
            3,
        ),
        (
            [1, 1, 1, None, 1, None, None, 1, 1, None, 1],
            4,
        ),
        (
            [1],
            0,
        ),
    ),
)
def test_longestZigZag(root, want):
    tree = build_tree(root)
    assert tree is not None
    got = solution.longestZigZag(tree)
    assert got == want
