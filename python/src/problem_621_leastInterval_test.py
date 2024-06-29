import pytest
from problem_621_leastInterval import Solution

solution = Solution()


@pytest.mark.parametrize(
    ("tasks", "n", "want"),
    [
        (["A", "A", "A", "B", "B", "B"], 2, 8),
        (["A", "A", "A", "B", "B", "B"], 0, 6),
        (["A", "A", "A", "A", "A", "A", "B", "C", "D", "E", "F", "G"], 2, 16),
    ],
)
def test_leastInterval(tasks: list[str], n: int, want: int) -> None:
    got = solution.leastInterval(tasks, n)
    assert got == want
