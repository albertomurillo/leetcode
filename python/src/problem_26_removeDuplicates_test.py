import pytest
from problem_26_removeDuplicates import Solution

solution = Solution()


@pytest.mark.parametrize(
    ("nums", "expected", "want"),
    [
        ([1, 1, 2], [1, 2], 2),
        ([0, 0, 1, 1, 1, 2, 2, 3, 3, 4], [0, 1, 2, 3, 4], 5),
    ],
)
def test_removeDuplicates(nums: list[int], expected: list[int], want: int) -> None:
    k = solution.removeDuplicates(nums)
    assert k == want
    assert nums[0:k] == expected
