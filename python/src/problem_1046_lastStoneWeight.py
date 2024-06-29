# https://leetcode.com/problems/last-stone-weight

import heapq


class Solution:
    def lastStoneWeight(self, stones: list[int]) -> int:
        q = [-x for x in stones]
        heapq.heapify(q)

        while len(q) != 1:
            s1 = heapq.heappop(q)
            s2 = heapq.heappop(q)
            s3 = s1 - s2
            heapq.heappush(q, s3)

        return -heapq.heappop(q)
