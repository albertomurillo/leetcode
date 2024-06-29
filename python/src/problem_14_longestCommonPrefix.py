# https://leetcode.com/problems/longest-common-prefix


class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        res = []
        for i in range(min(len(s) for s in strs)):
            c = strs[0][i]
            if not all(s[i] == c for s in strs[1:]):
                break

            res.append(c)

        return "".join(res)
