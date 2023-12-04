# https://leetcode.com/problems/best-time-to-buy-and-sell-stock

from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        left = 0
        right = 1
        profit = 0

        while right < len(prices):
            profit = max(profit, prices[right] - prices[left])
            if prices[left] > prices[right]:
                left = right
            right += 1

        return profit
