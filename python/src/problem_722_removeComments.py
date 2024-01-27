# https://leetcode.com/problems/remove-comments

from typing import List


class Solution:
    def removeComments(self, source: List[str]) -> List[str]:
        src = "\n".join(source)
        eof = len(src)
        buf = []

        i = 0
        while i < eof:
            sym = src[i : i + 2]
            if sym == "//":
                i += 2
                while i < eof and src[i] != "\n":
                    i += 1
                continue

            if sym == "/*":
                i += 2
                while src[i : i + 2] != "*/":
                    i += 1
                i += 2
                continue

            buf.append(src[i])
            i += 1

        return [line for line in "".join(buf).splitlines() if line]
