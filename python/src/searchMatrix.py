# https://leetcode.com/problems/search-a-2d-matrix

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix) - 1
        n = len(matrix[0]) - 1

        # find row
        top = 0
        bottom = m
        row = -1
        while top <= bottom:
            mid = (top + bottom) // 2
            if target < matrix[mid][0]:
                bottom = mid - 1
                continue
            if target > matrix[mid][n]:
                top = mid + 1
                continue
            row = mid
            break
        if row == -1:
            return False

        # find target
        left = 0
        right = n
        while left <= right:
            mid = (left + right) // 2
            if target < matrix[row][mid]:
                right = mid - 1
                continue
            if target > matrix[row][mid]:
                left = mid + 1
                continue
            return True
        return False
