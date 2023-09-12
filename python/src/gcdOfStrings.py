# https://leetcode.com/problems/greatest-common-divisor-of-strings/

import math


class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def is_common_divisor(str1: str, str2: str, divisor: int) -> bool:
            if len(str1) % divisor != 0:
                return False

            if len(str2) % divisor != 0:
                return False

            factor1 = len(str1) // divisor
            if str1 != str1[:divisor] * factor1:
                return False

            factor2 = len(str2) // divisor
            if str2 != str1[:divisor] * factor2:
                return False

            return True

        for divisor in range(min(len(str1), len(str2)), 0, -1):
            if is_common_divisor(str1, str2, divisor):
                return str1[:divisor]

        return ""

    def gcdOfStrings_python(self, str1: str, str2: str) -> str:
        if str1 + str2 != str2 + str1:
            return ""

        n = math.gcd(len(str1), len(str2))
        return str1[:n]
