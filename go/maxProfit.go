// https://leetcode.com/problems/best-time-to-buy-and-sell-stock

package leetcode

func maxProfit(prices []int) int {
	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}

	left := 0
	right := 1
	profit := 0

	for right < len(prices) {
		profit = max(profit, prices[right]-prices[left])
		if prices[left] > prices[right] {
			left = right
		}
		right++
	}

	return profit
}
