# https://leetcode.com/problems/can-place-flowers/

from typing import List


class Solution:
    def canPlaceFlowers(self, flowerbed: List[int], n: int) -> bool:
        last_index = len(flowerbed) - 1
        i = 0
        while i <= last_index:
            if n == 0:
                return True

            if flowerbed[i]:
                i += 2
                continue

            if i < last_index and flowerbed[i + 1]:
                i += 3
                continue

            if i > 0 and flowerbed[i - 1]:
                i += 1
                continue

            n -= 1
            i += 2

        return n <= 0
