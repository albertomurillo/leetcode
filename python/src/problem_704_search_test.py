import pytest
from problem_704_search import Solution

solution = Solution()


@pytest.mark.parametrize(
    "nums, target, want",
    (
        ([-1, 0, 3, 5, 9, 12], 9, 4),
        ([-1, 0, 3, 5, 9, 12], 2, -1),
    ),
)
def test_search(nums: list[int], target: int, want: int) -> None:
    got = solution.search(nums, target)
    assert got == want
