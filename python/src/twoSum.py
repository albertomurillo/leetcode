# https://leetcode.com/problems/two-sum/

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i in range(0, len(nums)):
            num = nums[i]
            want = target - num
            if want in seen:
                return [seen[want], i]
            seen[num] = i
        return []
