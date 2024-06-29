import pytest
from problem_378_kthSmallest import Solution

solution = Solution()


@pytest.mark.parametrize(
    ("matrix", "k", "want"),
    [
        ([[1, 5, 9], [10, 11, 13], [12, 13, 15]], 8, 13),
        ([[-5]], 1, -5),
    ],
)
def test_kthSmallest(matrix: list[list[int]], k: int, want: int) -> None:
    got = solution.kthSmallest(matrix, k)
    assert got == want
