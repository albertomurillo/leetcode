# https://leetcode.com/problems/remove-duplicates-from-sorted-array

from typing import List


class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        curr = nums[0]
        offset = -1

        for i, e in enumerate(nums):
            if e == curr:
                offset += 1
                continue

            curr = e
            nums[i - offset] = nums[i]

        return len(nums) - offset
