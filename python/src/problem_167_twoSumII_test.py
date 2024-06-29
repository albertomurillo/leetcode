import pytest
from problem_167_twoSumII import Solution


@pytest.mark.parametrize(
    "nums, target, want",
    (
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 3, 4, 5, 7, 10, 11], 9, [3, 4]),
        ([3, 3, 3], 5, []),
    ),
)
def test_twoSum(nums: list[int], target: int, want: list[int]) -> None:
    solution = Solution()
    got = solution.twoSum(nums, target)
    assert got == want
