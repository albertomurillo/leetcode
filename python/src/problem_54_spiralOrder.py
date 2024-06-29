# https://leetcode.com/problems/spiral-matrix


class Solution:
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        n = len(matrix)
        m = len(matrix[0])
        size = n * m

        res = []
        visited = set()

        pos = complex(0, 0)
        dir = complex(0, 1)

        while len(visited) != size:
            res.append(matrix[int(pos.real)][int(pos.imag)])
            visited.add(pos)

            next_pos = pos + dir
            if next_pos in visited or not (
                0 <= next_pos.real < n and 0 <= next_pos.imag < m
            ):
                dir *= 1j**3
                next_pos = pos + dir
            pos = next_pos

        return res
