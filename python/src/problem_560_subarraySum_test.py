import pytest

from problem_560_subarraySum import Solution

solution = Solution()


@pytest.mark.parametrize(
    "nums, k, want",
    (
        ([1, 1, 1], 2, 2),
        ([1, 2, 3], 3, 2),
        ([-1, -1, 1], 1, 1),
    ),
)
def test_subarraySum(nums, k, want):
    got = solution.subarraySum(nums, k)
    assert got == want
