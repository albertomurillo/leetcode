# https://leetcode.com/problems/best-time-to-buy-and-sell-stock


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        cheapest = prices[0]
        profit = 0
        for price in prices:
            if price < cheapest:
                cheapest = price
                continue
            profit = max(profit, price - cheapest)

        return profit

    def maxProfit_two_ptrs(self, prices: list[int]) -> int:
        left = 0
        right = 1
        profit = 0

        while right < len(prices):
            profit = max(profit, prices[right] - prices[left])
            if prices[left] > prices[right]:
                left = right
            right += 1

        return profit
