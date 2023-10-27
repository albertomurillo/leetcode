// https://leetcode.com/problems/trapping-rain-water

package leetcode

func trap(height []int) int {
	l := 0
	r := len(height) - 1
	lMax := height[l]
	rMax := height[r]
	res := 0

	for l < r {
		if lMax < rMax {
			l++
			lMax = max(lMax, height[l])
			res += lMax - height[l]
		} else {
			r--
			rMax = max(rMax, height[r])
			res += rMax - height[r]
		}
	}

	return res
}
