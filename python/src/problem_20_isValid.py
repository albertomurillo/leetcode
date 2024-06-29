# https://leetcode.com/problems/valid-parentheses/


from collections import deque
from typing import Deque


class Solution:
    def isValid(self, s: str) -> bool:
        q: Deque[str] = deque()
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        for c in s:
            if c in pairs:
                q.append(pairs[c])
                continue

            if len(q) == 0:
                return False

            if q.pop() != c:
                return False

        return len(q) == 0
