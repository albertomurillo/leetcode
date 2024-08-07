# https://leetcode.com/problems/subsets

from itertools import combinations


class Solution:
    def subsets(self, nums: list[int]) -> list[list[int]]:
        def dfs(i: int, result: list[list[int]], subset: list[int]) -> None:
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

    def subsets_python(self, nums: list[int]) -> list[list[int]]:
        r = [[]]
        for i in range(len(nums)):
            r.extend(list(c) for c in combinations(nums, i + 1))
        return r
