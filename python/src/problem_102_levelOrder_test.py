import pytest
from leetcode import build_tree
from problem_102_levelOrder import Solution

solution = Solution()


@pytest.mark.parametrize(
    "root, want",
    (
        ([3, 9, 20, None, None, 15, 7], [[3], [9, 20], [15, 7]]),
        ([1], [[1]]),
        ([], []),
    ),
)
def test_levelOrder(root: list[int | None], want: list[list[int]]):
    tree = build_tree(root)
    got = solution.levelOrder(tree)
    assert got == want
