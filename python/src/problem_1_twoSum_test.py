import pytest
from problem_1_twoSum import Solution


@pytest.mark.parametrize(
    ("nums", "target", "want"),
    [
        ([2, 7, 11, 15], 9, [0, 1]),
        ([3, 2, 4], 6, [1, 2]),
        ([3, 3], 6, [0, 1]),
    ],
)
def test_twoSum(nums: list[int], target: int, want: list[int]) -> None:
    solution = Solution()
    got = solution.twoSum(nums, target)
    assert got == want
