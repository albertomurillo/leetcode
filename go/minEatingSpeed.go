// https://leetcode.com/problems/koko-eating-bananas

package leetcode

import "math"

func minEatingSpeed(piles []int, h int) int {
	min_k := 1
	max_k := piles[0]
	for _, i := range piles {
		if i > max_k {
			max_k = i
		}
	}
	result := max_k

	for min_k <= max_k {
		k := (min_k + max_k) / 2
		total_h := 0
		for _, bananas := range piles {
			total_h += int(math.Ceil(float64(bananas) / float64(k)))
		}
		if total_h > h {
			min_k = k + 1
			continue
		}
		result = k
		max_k = k - 1
	}
	return result
}
