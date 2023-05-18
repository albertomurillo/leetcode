# https://leetcode.com/problems/water-bottles/


class Solution:
    def numWaterBottles(self, numBottles: int, numExchange: int) -> int:
        full = numBottles
        empty = 0
        drank = 0

        while full:
            drank += full
            empty += full
            full = empty // numExchange
            empty = empty % numExchange

        return drank
