# https://leetcode.com/problems/two-sum/

from typing import Dict, List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen: Dict[int, int] = {}
        for i, num in enumerate(nums):
            want = target - num
            if want in seen:
                return [seen[want], i]
            seen[num] = i
        return []
