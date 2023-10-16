// https://leetcode.com/problems/two-sum-ii-input-array-is-sorted

package leetcode

func twoSumII(numbers []int, target int) []int {
	left := 0
	right := len(numbers) - 1

	for left < right {
		sum := numbers[left] + numbers[right]

		if sum < target {
			left++
			continue
		}

		if sum > target {
			right--
			continue
		}

		return []int{left + 1, right + 1}
	}

	return []int{}
}
