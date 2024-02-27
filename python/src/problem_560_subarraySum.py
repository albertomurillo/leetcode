# https://leetcode.com/problems/subarray-sum-equals-k

from collections import defaultdict
from itertools import accumulate
from typing import List


class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        prefix_count = defaultdict(int, {0: 1})
        res = 0
        for s in accumulate(nums):
            res += prefix_count[s - k]
            prefix_count[s] += 1
        return res
