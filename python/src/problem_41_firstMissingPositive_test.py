import pytest
from problem_41_firstMissingPositive import Solution

solution = Solution()


@pytest.mark.parametrize(
    ("nums", "want"),
    [
        ([1, 2, 0], 3),
        ([3, 4, -1, 1], 2),
        ([7, 8, 9, 11, 12], 1),
        ([1], 2),
    ],
)
def test_firstMissingPositive(nums: list[int], want: int) -> None:
    got = solution.firstMissingPositive(nums)
    assert got == want
