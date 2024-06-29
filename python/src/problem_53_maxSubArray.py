# https://leetcode.com/problems/maximum-subarray


class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        max_sub = nums[0]
        cur_sum = 0

        for num in nums:
            cur_sum = max(cur_sum, 0)
            cur_sum += num
            max_sub = max(max_sub, cur_sum)
        return max_sub
