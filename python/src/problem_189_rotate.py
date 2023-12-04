# https://leetcode.com/problems/rotate-array

from collections import deque
from typing import Deque, List


class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        self.rotate_inplace(nums, k)

    def rotate_inplace(self, nums: List[int], k: int) -> None:
        def reverse_inplace(nums: List[int], left: int, right: int) -> None:
            while left < right:
                nums[left], nums[right] = nums[right], nums[left]
                left += 1
                right -= 1

        n = len(nums)
        k = k % n
        reverse_inplace(nums, 0, n - 1)
        reverse_inplace(nums, 0, k - 1)
        reverse_inplace(nums, k, n - 1)

    def rotate_array(self, nums: List[int], k: int) -> None:
        n = len(nums)
        tmp = [0 for _ in range(n)]

        for i, num in enumerate(nums):
            tmp[(i + k) % n] = num

        for i, num in enumerate(tmp):
            nums[i] = num

    def rotate_deque(self, nums: List[int], k: int) -> None:
        q: Deque[int] = deque()

        for num in nums:
            q.append(num)

        for _ in range(k):
            q.appendleft(q.pop())

        for i, _ in enumerate(nums):
            nums[i] = q.popleft()
