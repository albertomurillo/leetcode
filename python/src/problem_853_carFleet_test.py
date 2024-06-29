import pytest
from problem_853_carFleet import Solution

solution = Solution()


@pytest.mark.parametrize(
    "target, position, speed, want",
    (
        (
            12,
            [10, 8, 0, 5, 3],
            [2, 4, 1, 1, 3],
            3,
        ),
        (
            10,
            [3],
            [3],
            1,
        ),
        (
            100,
            [0, 2, 4],
            [4, 2, 1],
            1,
        ),
        (
            31,
            [5, 26, 18, 25, 29, 21, 22, 12, 19, 6],
            [7, 6, 6, 4, 3, 4, 9, 7, 6, 4],
            6,
        ),
    ),
)
def test_carFleet(target, position, speed, want):
    got = solution.carFleet(target, position, speed)
    assert got == want
