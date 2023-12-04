# https://leetcode.com/problems/jump-game/

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        goal = len(nums) - 1

        for index in reversed(range(len(nums))):
            if index + nums[index] >= goal:
                goal = index

        return goal == 0
