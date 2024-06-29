import pytest
from leetcode import build_tree
from problem_543_diameterOfBinaryTree import Solution

solution = Solution()


@pytest.mark.parametrize(
    "root, want",
    (
        ([1, 2, 3, 4, 5], 3),
        ([1, 2], 1),
    ),
)
def test_diameterOfBinaryTree(root: list[int | None], want: int) -> None:
    tree = build_tree(root)
    got = solution.diameterOfBinaryTree(tree)
    assert got == want
