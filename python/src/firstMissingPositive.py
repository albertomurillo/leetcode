# https://leetcode.com/problems/first-missing-positive

from typing import List


class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)

        # move positive numbers into position
        for i in range(n):
            while (
                nums[i] >= 1  # is positive
                and nums[i] <= n  # has a position in the array
                and nums[i] != nums[(num := nums[i] - 1)]  # is not in position
            ):
                nums[i], nums[num] = nums[num], nums[i]

        # find the first numbers not in position
        for i in range(n):
            num = i + 1
            if nums[i] != num:
                return num

        # all numbers are in position, return the next one
        return n + 1
