import pytest
from problem_1431_kidswithCandies import Solution

solution = Solution()


@pytest.mark.parametrize(
    "candies, extraCandies, want",
    (
        ([2, 3, 5, 1, 3], 3, [True, True, True, False, True]),
        ([4, 2, 1, 1, 2], 1, [True, False, False, False, False]),
        ([12, 1, 12], 10, [True, False, True]),
    ),
)
def test_kidsWithCandies(candies: list[int], extraCandies: int, want: list[bool]):
    got = solution.kidsWithCandies(candies, extraCandies)
    assert got == want
