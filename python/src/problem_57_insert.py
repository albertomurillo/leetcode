# https://leetcode.com/problems/insert-interval


class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list:
        res = []

        start = 0
        end = 1
        # insert and merge in O(n) with O(n) extra space
        for i, curInterval in enumerate(intervals):
            #              newInterval
            # curInterval
            # time------------------->
            if curInterval[end] < newInterval[start]:
                res.append(curInterval)
                continue

            # newInterval
            #              curInterval
            # time------------------->
            if newInterval[end] < curInterval[start]:
                res.append(newInterval)
                res.extend(intervals[i:])
                return res

            # newInterval
            #    curInterval
            # newNewInterval
            # time------------------->
            newInterval = [
                min(newInterval[start], curInterval[start]),
                max(newInterval[end], curInterval[end]),
            ]

        res.append(newInterval)
        return res
