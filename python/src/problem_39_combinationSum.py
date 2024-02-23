# https://leetcode.com/problems/combination-sum

from collections import deque
from typing import Deque, List, Tuple

type Subset = Tuple[int, ...]
type State = Tuple[Subset, int, int]


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        r = []
        subset = []
        candidates.sort()

        def dfs(i: int, s: int):
            if s == target:
                r.append(subset.copy())
                return

            if i < len(candidates):
                if s + candidates[i] <= target:
                    subset.append(candidates[i])
                    dfs(i, s + candidates[i])
                    subset.pop()

            i += 1
            if i < len(candidates):
                if s + candidates[i] <= target:
                    dfs(i, s)

        dfs(i=0, s=0)
        return r

    def combinationSum_2(self, candidates: List[int], target: int) -> List[List[int]]:
        candidates.sort()
        res = []

        states: Deque[State] = deque([((), 0, 0)])
        while states:
            subset, s, i = states.popleft()

            if s == target:
                res.append(subset)
                continue

            n = candidates[i]
            if s + n <= target:
                states.append((subset + (n,), s + n, i))

            for i, n in enumerate(candidates[i + 1 :], start=i + 1):
                if s + n > target:
                    break
                states.append((subset + (n,), s + n, i))

        return res
