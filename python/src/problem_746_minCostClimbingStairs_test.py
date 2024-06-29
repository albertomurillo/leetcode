import pytest
from problem_746_minCostClimbingStairs import Solution

solution = Solution()


@pytest.mark.parametrize(
    "cost, want",
    (
        ([10, 15, 20], 15),
        ([1, 100, 1, 1, 1, 100, 1, 1, 100, 1], 6),
    ),
)
def test_minCostClimbingStairs(cost: list[int], want: int):
    got = solution.minCostClimbingStairs(cost)
    assert got == want
