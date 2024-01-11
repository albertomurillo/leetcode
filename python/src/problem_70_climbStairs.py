# https://leetcode.com/problems/climbing-stairs

from functools import cache


@cache
def _climbStairs_memo(n: int) -> int:
    if n == -1:
        return 0

    if n == 0:
        return 1

    return _climbStairs_memo(n - 1) + _climbStairs_memo(n - 2)


class Solution:
    def climbStairs_dp(self, n: int) -> int:
        dp = (1, 0)
        for _ in range(n):
            dp = (sum(dp), dp[0])

        return dp[0]

    def climbStairs_memo(self, n: int) -> int:
        return _climbStairs_memo(n)
