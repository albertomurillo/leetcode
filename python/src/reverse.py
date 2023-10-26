# https://leetcode.com/problems/reverse-integer


class Solution:
    def reverse(self, x: int) -> int:
        MAX = 2147483647  #  2**31 - 1
        mul = -1 if x < 0 else 1
        x = abs(x)
        res = 0

        while x:
            digit = x % 10

            if (res > MAX // 10) or (res == MAX // 10 and digit > MAX % 10):
                return 0

            res = (res * 10) + digit
            x = x // 10

        return mul * res
