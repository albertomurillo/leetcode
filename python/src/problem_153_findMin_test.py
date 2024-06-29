import pytest
from problem_153_findMin import Solution

solution = Solution()


@pytest.mark.parametrize(
    ("nums", "want"),
    [
        ([3, 4, 5, 1, 2], 1),
        ([4, 5, 6, 7, 0, 1, 2], 0),
        ([11, 13, 15, 17], 11),
    ],
)
def test_findMin(nums: list[int], want: int) -> None:
    got = solution.findMin(nums)
    assert got == want
