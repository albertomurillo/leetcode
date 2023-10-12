//  https://leetcode.com/problems/two-sum/

package leetcode

func twoSum(nums []int, target int) []int {
	seen := make(map[int]int, len(nums))

	for idx, val := range nums {
		want := target - val

		if idx2, ok := seen[want]; ok {
			return []int{idx, idx2}
		}

		seen[val] = idx
	}

	return []int{}
}
