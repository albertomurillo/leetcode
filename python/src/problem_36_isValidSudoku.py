# https://leetcode.com/problems/valid-sudoku

from collections import defaultdict


class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        rows: dict[int, set[str]] = defaultdict(set)
        cols: dict[int, set[str]] = defaultdict(set)
        boxs: dict[tuple[int, int], set[str]] = defaultdict(set)

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
