// https://leetcode.com/problems/merge-strings-alternately

func mergeAlternately(word1 string, word2 string) string {
	solution := strings.Builder{}

	i := 0
	j := 0
	for i < len(word1) && j < len(word2) {
		solution.WriteByte(word1[i])
		solution.WriteByte(word2[j])
		i++
		j++
	}
	solution.WriteString(word1[i:])
	solution.WriteString(word2[j:])
	return solution.String()
}
