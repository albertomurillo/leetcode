// https://leetcode.com/problems/valid-sudoku

package leetcode

func isValidSudoku(board [][]byte) bool {
	rows := [9][9]bool{}
	columns := [9][9]bool{}
	squares := [3][3][9]bool{}

	for row := 0; row < 9; row++ {
		for col := 0; col < 9; col++ {
			cell := board[row][col]

			if cell == '.' {
				continue
			}

			digit := int(cell-'0') - 1

			if rows[row][digit] || columns[col][digit] || squares[row/3][col/3][digit] {
				return false
			}

			rows[row][digit] = true
			columns[col][digit] = true
			squares[row/3][col/3][digit] = true
		}
	}

	return true
}
