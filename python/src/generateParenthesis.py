# https://leetcode.com/problems/generate-parentheses

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        stack = []
        result = []

        def helper(open: int, closed: int) -> str:
            if open == closed == n:
                result.append("".join(stack))
                return

            if open < n:
                stack.append("(")
                helper(open + 1, closed)
                stack.pop()

            if closed < open:
                stack.append(")")
                helper(open, closed + 1)
                stack.pop()

        helper(0, 0)
        return result
