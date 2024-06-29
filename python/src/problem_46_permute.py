# https://leetcode.com/problems/permutations

from itertools import permutations


class Solution:
    def permute(self, nums: list[int]) -> list[list[int]]:
        if len(nums) == 1:
            return [[nums[0]]]

        result = []
        for i, num in enumerate(nums):
            perms = self.permute(nums[:i] + nums[i + 1 :])

            for perm in perms:
                perm.append(num)

            result.extend(perms)

        return result

    def permute_python(self, nums: list[int]) -> list[list[int]]:
        return [list(x) for x in permutations(nums)]
