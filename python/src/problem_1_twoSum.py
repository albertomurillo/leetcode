# https://leetcode.com/problems/two-sum/


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        seen: dict[int, int] = {}
        for i, num in enumerate(nums):
            want = target - num
            if want in seen:
                return [seen[want], i]
            seen[num] = i
        return []
