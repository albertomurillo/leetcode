// https://leetcode.com/problems/valid-parentheses

package leetcode

func isValid(s string) bool {
	if len(s)%2 == 1 {
		return false
	}

	var stack []rune
	closingParentheses := map[rune]rune{
		'(': ')',
		'{': '}',
		'[': ']',
	}

	for _, val := range s {
		if closing, ok := closingParentheses[val]; ok {
			stack = append(stack, closing)
			continue
		}

		if len(stack) == 0 {
			return false
		}

		if val != stack[len(stack)-1] {
			return false
		}

		stack = stack[:len(stack)-1]
	}

	return len(stack) == 0
}
