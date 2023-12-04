# https://leetcode.com/problems/k-closest-points-to-origin

import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        heap = [(p[0] ** 2 + p[1] ** 2, p) for p in points]
        heapq.heapify(heap)

        res = []
        for _ in range(k):
            _, point = heapq.heappop(heap)
            res.append(point)

        return res

    def kClosest_max_heap(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        space: O(k)
        """
        heap = []
        for x, y in points:
            d = (x * x) + (y * y)
            heapq.heappush(heap, (-d, x, y))
            if len(heap) > k:
                heapq.heappop(heap)
        return [[x, y] for _, x, y in heap]

    def kClosest_python(self, points: List[List[int]], k: int) -> List[List[int]]:
        return heapq.nsmallest(k, points, key=lambda p: p[0] * p[0] + p[1] * p[1])
