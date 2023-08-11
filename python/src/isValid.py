# https://leetcode.com/problems/valid-parentheses/


from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        q = deque()
        pairs = {
            "(": ")",
            "[": "]",
            "{": "}",
        }

        for c in s:
            if c in pairs.keys():
                q.append(pairs[c])
                continue

            if len(q) == 0:
                return False

            if q.pop() != c:
                return False

        if len(q) != 0:
            return False

        return True
