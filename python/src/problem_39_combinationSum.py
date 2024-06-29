# https://leetcode.com/problems/combination-sum

from collections import deque

type Subset = tuple[int, ...]
type State = tuple[Subset, int, int]


class Solution:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        r = []
        subset = []
        candidates.sort()

        def dfs(i: int, s: int):
            if s == target:
                r.append(subset.copy())
                return

            if i < len(candidates) and s + candidates[i] <= target:
                subset.append(candidates[i])
                dfs(i, s + candidates[i])
                subset.pop()

            i += 1
            if i < len(candidates) and s + candidates[i] <= target:
                dfs(i, s)

        dfs(i=0, s=0)
        return r

    def combinationSum_2(self, candidates: list[int], target: int) -> list[list[int]]:
        candidates.sort()
        res = []

        states: deque[State] = deque([((), 0, 0)])
        while states:
            subset, s, idx = states.popleft()

            if s == target:
                res.append(subset)
                continue

            n = candidates[idx]
            if s + n <= target:
                states.append(((*subset, n), s + n, idx))

            for i, n in enumerate(candidates[idx + 1 :], start=idx + 1):
                if s + n > target:
                    break
                states.append(((*subset, n), s + n, i))

        return res
