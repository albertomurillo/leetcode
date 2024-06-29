import pytest
from problem_1046_lastStoneWeight import Solution

solution = Solution()


@pytest.mark.parametrize(
    "stones, want",
    (
        ([2, 7, 4, 1, 8, 1], 1),
        ([1], 1),
    ),
)
def test_lastStoneWeight(stones: list[int], want: int) -> None:
    got = solution.lastStoneWeight(stones)
    assert got == want
