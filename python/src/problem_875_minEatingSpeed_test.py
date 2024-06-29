import pytest
from problem_875_minEatingSpeed import Solution

solution = Solution()


@pytest.mark.parametrize(
    ("piles", "h", "want"),
    [
        ([3, 6, 7, 11], 8, 4),
        ([30, 11, 23, 4, 20], 5, 30),
        ([30, 11, 23, 4, 20], 6, 23),
    ],
)
def test_minEatingSpeed(piles: list[int], h: int, want: int) -> None:
    got = solution.minEatingSpeed(piles, h)
    assert got == want
