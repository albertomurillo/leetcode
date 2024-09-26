import pytest

from problem_56_merge import Solution

type Interval = list[int]
solution = Solution()


@pytest.mark.parametrize(
    ("intervals", "want"),
    [
        (
            [[1, 3], [2, 6], [8, 10], [15, 18]],
            [[1, 6], [8, 10], [15, 18]],
        ),
        (
            [[1, 4], [4, 5]],
            [[1, 5]],
        ),
    ],
)
def test_merge(intervals: list[Interval], want: Interval) -> None:
    got = solution.merge(intervals)
    assert got == want
