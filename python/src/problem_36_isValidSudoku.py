# https://leetcode.com/problems/valid-sudoku

from collections import defaultdict
from typing import Dict, List, Set, Tuple


class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows: Dict[int, Set[str]] = defaultdict(set)
        cols: Dict[int, Set[str]] = defaultdict(set)
        boxs: Dict[Tuple[int, int], Set[str]] = defaultdict(set)

        for row in range(9):
            for col in range(9):
                box = (row // 3, col // 3)
                cell = board[row][col]
                if cell == ".":
                    continue

                if cell in rows[row] or cell in cols[col] or cell in boxs[box]:
                    return False

                rows[row].add(cell)
                cols[col].add(cell)
                boxs[box].add(cell)

        return True
