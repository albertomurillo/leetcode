# https://leetcode.com/problems/permutations

from itertools import permutations
from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        if len(nums) == 1:
            return [[nums[0]]]

        result = []
        for i, num in enumerate(nums):
            perms = self.permute(nums[:i] + nums[i + 1 :])

            for perm in perms:
                perm.append(num)

            result.extend(perms)

        return result

    def permute_python(self, nums: List[int]) -> List[List[int]]:
        return [list(x) for x in permutations(nums)]
