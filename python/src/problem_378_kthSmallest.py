# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

from heapq import heappop, heappush
from typing import Generator, List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        new = iter(self.merge(matrix))
        r = matrix[0][0]
        for _ in range(k):
            r = next(new)
        return r

    def merge(self, rows: List[List[int]]) -> Generator[int, None, None]:
        q = []
        for row in rows:
            heappush(q, row)
        while q:
            row = heappop(q)
            yield row[0]
            row = row[1:]
            if row:
                heappush(q, row)
