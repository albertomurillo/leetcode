package leetcode

import "testing"

func Test_singleNumber(t *testing.T) {
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
			args{[]int{2, 2, 1}},
			1,
		},
		{
			"Example 2",
			args{[]int{4, 1, 2, 1, 2}},
			4,
		},
		{
			"Example 3",
			args{[]int{1}},
			1,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := singleNumber(tt.args.nums); got != tt.want {
				t.Errorf("singleNumber() = %v, want %v", got, tt.want)
			}
		})
	}
}
