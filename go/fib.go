// https://leetcode.com/problems/fibonacci-number/

func fib(n int) int {
	cache := make(map[int]int)

	var helper func(int) int
	helper = func(n int) int {
		if n < 2 {
			return n
		}

		if val, ok := cache[n]; ok {
			return val
		}

		cache[n] = helper(n-1) + helper(n-2)
		return cache[n]
	}

	return helper(n)
}
