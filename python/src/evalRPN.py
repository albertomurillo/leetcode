# https://leetcode.com/problems/evaluate-reverse-polish-notation

import operator
from types import List


class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = []
        operators = {
            "+": operator.add,
            "-": operator.sub,
            "*": operator.mul,
            "/": operator.truediv,  # int(a / b) trunks towards zero
        }
        for token in tokens:
            if token not in operators:
                stack.append(int(token))
                continue

            y = stack.pop()
            x = stack.pop()
            stack.append(int(operators[token](x, y)))

        return stack.pop()
