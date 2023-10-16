# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        l = 0
        r = len(numbers) - 1
        while l < r:
            s = numbers[l] + numbers[r]
            if s < target:
                l += 1
                continue
            if s > target:
                r -= 1
                continue

            return [l + 1, r + 1]

        return []
