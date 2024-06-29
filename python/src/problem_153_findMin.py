# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array


class Solution:
    def findMin(self, nums: list[int]) -> int:
        left = 0
        right = len(nums) - 1

        # Array is sorted
        if nums[left] < nums[right]:
            return nums[0]

        # Array is rotated
        while left < right:
            mid = (left + right) // 2
            if nums[mid] > nums[right]:
                left = mid + 1
            else:
                right = mid

        return nums[left]
