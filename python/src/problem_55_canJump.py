# https://leetcode.com/problems/jump-game/


class Solution:
    def canJump(self, nums: list[int]) -> bool:
        goal = len(nums) - 1

        for index in reversed(range(len(nums))):
            if index + nums[index] >= goal:
                goal = index

        return goal == 0
