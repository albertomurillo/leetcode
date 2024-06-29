# https://leetcode.com/problems/non-overlapping-intervals/


class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort()
        res = 0

        _, last_end = intervals[0]
        for start, end in intervals[1:]:
            if last_end <= start:
                last_end = end
                continue

            last_end = min(last_end, end)
            res += 1
        return res
