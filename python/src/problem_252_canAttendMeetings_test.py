import pytest
from leetcode import Interval
from problem_252_canAttendMeetings import Solution

solution = Solution()


@pytest.mark.parametrize(
    "intervals, want",
    (
        ([(0, 30), (5, 10), (15, 20)], False),
        ([(5, 8), (9, 15)], True),
    ),
)
def test_canAttendMeetings(intervals: list[tuple[int, int]], want: bool) -> None:
    _intervals = [Interval(start, end) for start, end in intervals]
    got = solution.canAttendMeetings(_intervals)
    assert got == want
