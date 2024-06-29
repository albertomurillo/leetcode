# https://leetcode.com/problems/valid-parentheses/


from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        q: deque[str] = deque()
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
