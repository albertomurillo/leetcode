// https://leetcode.com/problems/container-with-most-water/

package leetcode

func maxArea(height []int) int {
	min := func(a, b int) int {
		if a < b {
			return a
		}
		return b
	}

	max := func(a, b int) int {
		if a > b {
			return a
		}
		return b
	}

	l := 0
	r := len(height) - 1
	res := 0

	for l < r {
		area := min(height[l], height[r]) * (r - l)
		res = max(res, area)

		if height[l] < height[r] {
			l++
			continue
		}
		r--
	}

	return res
}
