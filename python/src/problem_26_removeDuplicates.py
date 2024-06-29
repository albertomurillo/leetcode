# https://leetcode.com/problems/remove-duplicates-from-sorted-array


class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        curr = nums[0]
        offset = -1

        for i, e in enumerate(nums):
            if e == curr:
                offset += 1
                continue

            curr = e
            nums[i - offset] = e

        return len(nums) - offset
