# https://leetcode.com/problems/longest-consecutive-sequence

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        result = 0
        num_set = set(nums)

        for start in num_set:
            if start - 1 in num_set:
                continue

            end = start + 1
            while end in num_set:
                end += 1

            result = max(result, end - start)

        return result
