# https://leetcode.com/problems/kth-largest-element-in-a-stream/

import heapq


class KthLargest:
    def __init__(self, k: int, nums: list[int]):
        self._k = k
        self._heap = nums
        heapq.heapify(self._heap)
        while len(self._heap) > k:
            heapq.heappop(self._heap)

    def add(self, val: int) -> int:
        if len(self._heap) < self._k:
            heapq.heappush(self._heap, val)
        elif val > self._heap[0]:
            heapq.heappushpop(self._heap, val)
        return self._heap[0]


class KthLargest_sorted:
    def __init__(self, k: int, nums: list[int]):
        self._k = k
        self._nums = sorted(nums)

    def add(self, val: int) -> int:
        self._nums.append(val)
        self._nums = sorted(self._nums)
        return self._nums[-self._k]
