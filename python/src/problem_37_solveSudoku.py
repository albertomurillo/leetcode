# https://leetcode.com/problems/sudoku-solver/

from collections import deque


class Solution:
    board: list[list[str]]
    empty_cells: deque

    def solveSudoku(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        self.board = board
        self.empty_cells = deque()
        for row in range(9):
            for col in range(9):
                if self.board[row][col] == ".":
                    self.empty_cells.append((row, col))

        self.solve()

    def solve(self) -> bool:
        if len(self.empty_cells) == 0:
            return True

        row, col = self.empty_cells.popleft()
        for num in ["1", "2", "3", "4", "5", "6", "7", "8", "9"]:
            if not self.is_posible(num, row, col):
                continue

            self.board[row][col] = num
            if self.solve():
                return True

        self.empty_cells.appendleft((row, col))
        self.board[row][col] = "."
        return False

    def is_posible(self, num: str, row: int, col: int) -> bool:
        return (
            self.is_possible_row(num, row)
            and self.is_possible_col(num, col)
            and self.is_possible_square(num, row, col)
        )

    def is_possible_row(self, num: str, row: int) -> bool:
        return all(self.board[row][col] != num for col in range(9))

    def is_possible_col(self, num: str, col: int) -> bool:
        return all(self.board[row][col] != num for row in range(9))

    def is_possible_square(self, num: str, row: int, col: int) -> bool:
        row = 3 * (row // 3)
        col = 3 * (col // 3)
        for r in range(row, row + 3):
            for c in range(col, col + 3):
                if self.board[r][c] == num:
                    return False
        return True
