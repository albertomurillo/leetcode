import pytest
from problem_54_spiralOrder import Solution

solution = Solution()


@pytest.mark.parametrize(
    ("matrix", "want"),
    [
        (
            [
                [1, 2, 3],
                [4, 5, 6],
                [7, 8, 9],
            ],
            [1, 2, 3, 6, 9, 8, 7, 4, 5],
        ),
        (
            [
                [1, 2, 3, 4],
                [5, 6, 7, 8],
                [9, 10, 11, 12],
            ],
            [1, 2, 3, 4, 8, 12, 11, 10, 9, 5, 6, 7],
        ),
    ],
)
def test_spiralOrder(matrix: list[list[int]], want: list[int]) -> None:
    got = solution.spiralOrder(matrix)
    assert got == want
