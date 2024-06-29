# https://leetcode.com/problems/minimum-interval-to-include-each-query

from heapq import heappop, heappush


class Solution:
    def minInterval(self, intervals: list[list[int]], queries: list[int]) -> list[int]:
        ranges = [range(x[0], x[1] + 1) for x in sorted(intervals)]
        results = {}

        min_heap = []
        range_idx = 0
        for query in sorted(queries):
            while range_idx < len(ranges) and ranges[range_idx][0] <= query:
                r = ranges[range_idx]
                heappush(min_heap, (len(r), r.stop))
                range_idx += 1

            while min_heap and min_heap[0][1] <= query:
                heappop(min_heap)

            results[query] = min_heap[0][0] if min_heap else -1

        return [results[q] for q in queries]
