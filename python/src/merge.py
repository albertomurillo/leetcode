# https://leetcode.com/problems/merge-intervals

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        res = [intervals[0]]
        for start, end in intervals[1:]:
            last_start, last_end = res[-1]
            if last_end >= start:
                res[-1] = [last_start, max(last_end, end)]
            else:
                res.append([start, end])
        return res
