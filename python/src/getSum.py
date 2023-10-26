# https://leetcode.com/problems/sum-of-two-integers


class Solution:
    def getSum(self, a: int, b: int) -> int:
        # 32 bit mask in hexadecimal
        mask = 0xFFFFFFFF

        while (b & mask) > 0:
            carry = (a & b) << 1
            a = a ^ b
            b = carry

        # handles overflow
        return (a & mask) if b > 0 else a
