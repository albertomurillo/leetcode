# https://leetcode.com/problems/meeting-rooms-ii

from heapq import heappop, heappush
from typing import List, Tuple


class Solution:
    def minMeetingRooms(self, meetings: List[Tuple[int, int]]) -> int:
        if len(meetings) == 0:
            return 0

        meetings.sort()
        q = [meetings[0][1]]
        for starts, ends in meetings[1:]:
            if starts >= q[0]:
                heappop(q)

            heappush(q, ends)

        return len(q)
