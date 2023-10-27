# https://leetcode.com/problems/koko-eating-bananas

import math
from typing import List


class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        min_k = 1
        max_k = max(piles)
        result = max_k

        while min_k <= max_k:
            k = (min_k + max_k) // 2
            would_take_h = sum([math.ceil(bananas / k) for bananas in piles])
            if would_take_h > h:
                min_k = k + 1
                continue

            result = k
            max_k = k - 1

        return result
