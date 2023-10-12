//  https://leetcode.com/problems/can-place-flowers/

package leetcode

func canPlaceFlowers(flowerbed []int, n int) bool {
	lastIndex := len(flowerbed) - 1
	for i := 0; i <= lastIndex; {
		if n == 0 {
			return true
		}

		if flowerbed[i] == 1 {
			i += 2
			continue
		}

		if i < lastIndex && flowerbed[i+1] == 1 {
			i += 3
			continue
		}

		if i > 0 && flowerbed[i-1] == 1 {
			i += 1
			continue
		}

		n -= 1
		i += 2
	}

	return n <= 0
}
