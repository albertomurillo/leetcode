// https://leetcode.com/problems/reverse-integer

package leetcode

import "math"

func reverse(x int) int {
	res := 0
	mul := 1
	if x < 0 {
		mul = -1
		x = -x
	}
	for x != 0 {
		digit := x % 10

		if res > math.MaxInt32/10 || res == math.MaxInt32/10 && digit > math.MaxInt32%10 {
			return 0
		}

		res = (res * 10) + digit
		x = x / 10
	}
	return mul * res
}
