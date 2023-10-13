// https://leetcode.com/problems/valid-palindrome

package leetcode

import (
	"unicode"
)

func isAlNum(r rune) bool {
	return unicode.IsLetter(r) || unicode.IsNumber(r)
}

func isPalindrome(s string) bool {
	left := 0
	right := len(s) - 1
	runes := []rune(s)

	for left < right {
		if !isAlNum(runes[left]) {
			left += 1
			continue
		}

		if !isAlNum(runes[right]) {
			right -= 1
			continue
		}

		if unicode.ToLower(runes[left]) != unicode.ToLower(runes[right]) {
			return false
		}

		left += 1
		right -= 1
	}

	return true
}
