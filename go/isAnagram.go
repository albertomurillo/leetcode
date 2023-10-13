// https://leetcode.com/problems/valid-anagram

package leetcode

func isAnagram(s string, t string) bool {
	seen := make([]int, 26)

	if len(s) != len(t) {
		return false
	}

	for _, val := range s {
		seen[val-'a']++
	}

	for _, val := range t {
		seen[val-'a']--
	}

	for _, val := range seen {
		if val != 0 {
			return false
		}
	}

	return true
}
