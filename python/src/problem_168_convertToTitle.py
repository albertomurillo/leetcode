# https://leetcode.com/problems/excel-sheet-column-title


class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        A = ord("A")

        res = []
        n = columnNumber

        while n:
            n, m = divmod(n - 1, 26)
            res.append(chr(A + m))

        return "".join(reversed(res))
