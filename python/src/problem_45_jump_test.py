import pytest
from problem_45_jump import Solution

solution = Solution()


@pytest.mark.parametrize(
    "nums, want",
    (
        ([2, 3, 1, 1, 4], 2),
        ([2, 3, 0, 1, 4], 2),
    ),
)
def test_jump(nums: list[int], want: int) -> None:
    got = solution.jump(nums)
    assert got == want
