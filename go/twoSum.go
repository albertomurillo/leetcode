//  https://leetcode.com/problems/two-sum/

func twoSum(nums []int, target int) []int {
	seen := make(map[int]int, len(nums))
	for i := range nums {
		if val, ok := seen[target-nums[i]]; ok {
			return []int{val, i}
		}
		seen[nums[i]] = i
	}
	return []int{}
}
