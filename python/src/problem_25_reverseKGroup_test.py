import pytest
from leetcode import build_list, iter_list
from problem_25_reverseKGroup import Solution

solution = Solution()


@pytest.mark.parametrize(
    "head, k, want",
    (
        (
            [1, 2, 3, 4, 5],
            2,
            [2, 1, 4, 3, 5],
        ),
        (
            [1, 2, 3, 4, 5],
            3,
            [3, 2, 1, 4, 5],
        ),
    ),
)
def test_reverseKGroup(head, k, want):
    ll = build_list(head)
    got_ll = solution.reverseKGroup(ll, k)
    got = list(iter_list(got_ll))
    assert got == want
