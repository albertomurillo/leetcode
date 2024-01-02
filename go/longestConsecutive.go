// https://leetcode.com/problems/longest-consecutive-sequence

package leetcode

func longestConsecutive(nums []int) int {
	result := 0

	numSet := make(map[int]struct{})
	for _, num := range nums {
		numSet[num] = struct{}{}
	}

	for start := range numSet {
		if _, ok := numSet[start-1]; ok {
			continue
		}

		end := start + 1
		for ; ; end++ {
			if _, ok := numSet[end]; !ok {
				break
			}
		}

		result = max(result, end-start)
	}

	return result
}
