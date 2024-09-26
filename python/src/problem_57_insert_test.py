import pytest

from problem_57_insert import Solution

type Interval = list[int]

solution = Solution()


@pytest.mark.parametrize(
    ("intervals", "newInterval", "want"),
    [
        (
            [[1, 3], [6, 9]],
            [2, 5],
            [[1, 5], [6, 9]],
        ),
        (
            [[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]],
            [4, 8],
            [[1, 2], [3, 10], [12, 16]],
        ),
        (
            [],
            [5, 7],
            [[5, 7]],
        ),
    ],
)
def test_insert(
    intervals: list[Interval], newInterval: Interval, want: list[Interval]
) -> None:
    got = solution.insert(intervals, newInterval)
    assert got == want
