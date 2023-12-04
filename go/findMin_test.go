// https://leetcode.com/problems/find-minimum-in-rotated-sorted-array

package leetcode

import "testing"

func Test_findMin(t *testing.T) {
	type args struct {
		nums []int
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			"Example 1",
			args{[]int{3, 4, 5, 1, 2}},
			1,
		},
		{
			"Example 2",
			args{[]int{4, 5, 6, 7, 0, 1, 2}},
			0,
		},
		{
			"Example 3",
			args{[]int{11, 13, 15, 17}},
			11,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := findMin(tt.args.nums); got != tt.want {
				t.Errorf("findMin() = %v, want %v", got, tt.want)
			}
		})
	}
}
