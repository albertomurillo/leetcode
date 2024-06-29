# https://leetcode.com/problems/jump-game-ii


class Solution:
    def jump(self, nums: list[int]) -> int:
        goal = len(nums) - 1
        left = 0
        right = 0
        jumps = 0

        while right < goal:
            far = 0
            for i in range(left, right + 1):
                far = max(far, i + nums[i])

            left = right + 1
            right = far
            jumps += 1

        return jumps
