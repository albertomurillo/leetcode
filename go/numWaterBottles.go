// https://leetcode.com/problems/water-bottles/

func numWaterBottles(numBottles int, numExchange int) int {
	full := numBottles
	empty := 0
	drank := 0

	for full > 0 {
		drank += full
		empty += full
		full = empty / numExchange
		empty = empty % numExchange
	}

	return drank
}
