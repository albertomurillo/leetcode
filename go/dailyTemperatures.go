// https://leetcode.com/problems/daily-temperatures

package leetcode

func dailyTemperatures(temperatures []int) []int {
	res := make([]int, len(temperatures))
	stack := []int{}

	for i, temp := range temperatures {
		for (len(stack) > 0) && (temp > temperatures[stack[len(stack)-1]]) {
			j := stack[len(stack)-1]
			stack = stack[:len(stack)-1]
			res[j] = i - j
		}
		stack = append(stack, i)
	}

	return res
}
