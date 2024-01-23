# https://leetcode.com/problems/subsets

from itertools import combinations
from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        def dfs(i: int, result: List[List[int]], subset: List[int]):
            if i >= len(nums):
                result.append(subset.copy())
                return

            # left branch
            subset.append(nums[i])
            dfs(i + 1, result, subset)

            # right branch
            subset.pop()
            dfs(i + 1, result, subset)

        result = []
        dfs(0, result, [])
        return result

    def subsets_python(self, nums: List[int]) -> List[List[int]]:
        r = [[]]
        for i in range(len(nums)):
            r.extend(list(c) for c in combinations(nums, i + 1))
        return r
