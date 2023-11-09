from typing import List, Tuple

import pytest

from canAttendMeetings import Solution
from leetcode import Interval

solution = Solution()


@pytest.mark.parametrize(
    "intervals, want",
    (
        ([(0, 30), (5, 10), (15, 20)], False),
        ([(5, 8), (9, 15)], True),
    ),
)
def test_canAttendMeetings(intervals: List[Tuple[int, int]], want: bool):
    intervals = [Interval(start, end) for start, end in intervals]
    got = solution.canAttendMeetings(intervals)
    assert got == want
