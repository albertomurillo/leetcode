// https://leetcode.com/problems/3sum

package leetcode

import "sort"

func threeSum(nums []int) [][]int {
	result := [][]int{}
	sort.Ints(nums)

	for idx, num := range nums {
		if num > 0 {
			break
		}

		if (idx > 0) && (num == nums[idx-1]) {
			continue
		}

		left := idx + 1
		right := len(nums) - 1

		for left < right {
			total := num + nums[left] + nums[right]

			if total > 0 {
				right--
				continue
			}

			if total < 0 {
				left++
				continue
			}

			triplet := []int{num, nums[left], nums[right]}
			result = append(result, triplet)

			for (left < right) && (nums[left] == triplet[1]) {
				left++
			}

			for (left < right) && (nums[right] == triplet[2]) {
				right--
			}
		}
	}
	return result
}
