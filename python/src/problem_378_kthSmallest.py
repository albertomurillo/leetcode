# https://leetcode.com/problems/kth-smallest-element-in-a-sorted-matrix

from heapq import heappop, heappush
from typing import Generator, List


class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        items = self.merge(matrix)
        for _ in range(k - 1):
            next(items)
        return next(items)

    def merge(self, matrix: List[List[int]]) -> Generator[int, None, None]:
        q: list[tuple[int, int, int]]
        q = [(items[0], row, 0) for row, items in enumerate(matrix)]

        while q:
            (item, row, col) = heappop(q)
            yield item
            col += 1
            if col < len(matrix[row]):
                heappush(q, (matrix[row][col], row, col))
