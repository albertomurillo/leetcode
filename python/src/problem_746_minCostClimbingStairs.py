# https://leetcode.com/problems/min-cost-climbing-stairs

from typing import List


class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = (0, 0)
        for i in range(len(cost) - 1, -1, -1):
            dp = (cost[i] + min(dp), dp[0])
        return min(dp)
