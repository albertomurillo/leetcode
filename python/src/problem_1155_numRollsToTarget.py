# https://leetcode.com/problems/number-of-dice-rolls-with-target-sum

from functools import cache


class Solution:
    def numRollsToTarget(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        @cache
        def count(n: int, target: int) -> int:
            if n == 0:
                return 1 if target == 0 else 0

            res = 0
            for val in range(1, k + 1):
                res = (res + count(n - 1, target - val)) % MOD

            return res

        return count(n, target)

    def numRollsToTarget_dp(self, n: int, k: int, target: int) -> int:
        MOD = 10**9 + 7

        dp = [0] * (target + 1)
        dp[0] = 1

        for _dice in range(n):
            next_dp = [0] * (target + 1)

            for val in range(1, k + 1):
                for total in range(val, target + 1):
                    next_dp[total] = (next_dp[total] + dp[total - val]) % MOD

            dp = next_dp

        return dp[target]
