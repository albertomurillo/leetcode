// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

package leetcode

import (
	"math"
)

func kidsWithCandies(candies []int, extraCandies int) []bool {
	result := make([]bool, len(candies))

	max := math.MinInt
	for _, c := range candies {
		if c > max {
			max = c
		}
	}

	for i, c := range candies {
		if c+extraCandies >= max {
			result[i] = true
		}
	}

	return result
}
