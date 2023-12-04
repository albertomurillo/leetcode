# https://leetcode.com/problems/roman-to-integer


class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I": 1,
            "V": 5,
            "X": 10,
            "L": 50,
            "C": 100,
            "D": 500,
            "M": 1000,
        }

        total = 0
        for i, c in enumerate(s):
            if i < len(s) - 1 and roman[c] < roman[s[i + 1]]:
                total -= roman[c]
            else:
                total += roman[c]

        return total
