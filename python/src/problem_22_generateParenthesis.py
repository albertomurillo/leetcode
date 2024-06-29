# https://leetcode.com/problems/generate-parentheses


class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        stack: list[str] = []
        result: list[str] = []

        def helper(open: int, closed: int) -> None:
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
