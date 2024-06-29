import pytest
from leetcode import build_tree
from problem_100_isSameTree import Solution

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
def test_isSameTree(p: list[int | None], q: list[int | None], want: bool):
    _p = build_tree(p)
    _q = build_tree(q)
    got = solution.isSameTree(_p, _q)
    assert got == want
