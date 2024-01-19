from typing import List, Tuple

import pytest

from problem_253_minMeetingRooms import Solution

solution = Solution()


@pytest.mark.parametrize(
    "meetings, want",
    (
        ([(0, 30), (5, 10), (15, 20)], 2),
        ([(2, 7)], 1),
        ([], 0),
    ),
)
def test_minMeetingRooms(meetings: List[Tuple[int, int]], want: int):
    got = solution.minMeetingRooms(meetings)
    assert got == want
