# https://leetcode.com/problems/kth-largest-element-in-an-array

import heapq


class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        heap = [-n for n in nums]
        heapq.heapify(heap)
        for _ in range(k - 1):
            heapq.heappop(heap)
        return -heapq.heappop(heap)

    def findKthLargest_python(self, nums: list[int], k: int) -> int:
        return heapq.nlargest(k, nums)[-1]
