# https://leetcode.com/problems/missing-number

from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        res = 0
        for num in nums:
            res ^= num
        for num in range(len(nums) + 1):
            res ^= num
        return res

    def missingNumber_gauss(self, nums: List[int]) -> int:
        # res = sum(range(len(nums) + 1))         # O(n)
        res = (len(nums) * (len(nums) + 1)) // 2  # O(1)
        res -= sum(nums)
        return res
