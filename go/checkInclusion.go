// https://leetcode.com/problems/permutation-in-string

package leetcode

import "reflect"

func checkInclusion(s1 string, s2 string) bool {
	if len(s1) > len(s2) {
		return false
	}

	left := 0
	right := len(s1) - 1

	c1 := make(map[rune]int)
	for _, c := range s1 {
		c1[c] += 1
	}

	c2 := make(map[rune]int)
	for _, c := range s2[left:right] {
		c2[c] += 1
	}

	for right < len(s2) {
		c2[rune(s2[right])] += 1

		if reflect.DeepEqual(c1, c2) {
			return true
		}

		c := rune(s2[left])
		c2[c] -= 1
		if c2[c] == 0 {
			delete(c2, c)
		}

		left++
		right++
	}

	return false
}
