import pytest
from problem_1207_uniqueOccurrences import Solution

solution = Solution()


@pytest.mark.parametrize(
    "arr, want",
    (
        ([1, 2, 2, 1, 1, 3], True),
        ([1, 2], False),
        ([-3, 0, 1, -3, 1, 1, 1, -3, 10, 0], True),
    ),
)
def test_uniqueOccurrences(arr, want):
    got = solution.uniqueOccurrences(arr)
    assert got == want
