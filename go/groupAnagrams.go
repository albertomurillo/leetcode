// https://leetcode.com/problems/group-anagrams

package leetcode

func groupAnagrams(strs []string) [][]string {
	anagrams := make(map[[26]int][]string)

	for _, str := range strs {
		var key [26]int
		for _, c := range str {
			key[c-'a']++
		}
		anagrams[key] = append(anagrams[key], str)
	}

	res := make([][]string, 0, len(anagrams))
	for _, val := range anagrams {
		res = append(res, val)
	}

	return res
}
