package leetcode

import (
	"reflect"
	"testing"
)

func Test_twoSumII(t *testing.T) {
	type args struct {
		numbers []int
		target  int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			"Example 1",
			args{[]int{2, 7, 11, 15}, 9},
			[]int{1, 2},
		},
		{
			"Example 2",
			args{[]int{2, 3, 4}, 6},
			[]int{1, 3},
		},
		{
			"Example 3",
			args{[]int{-1, 0}, -1},
			[]int{1, 2},
		},
		{
			"Example 4",
			args{[]int{1, 3, 4, 5, 7, 10, 11}, 9},
			[]int{3, 4},
		},
		{
			name: "No Solution",
			args: args{[]int{3, 3, 3}, 5},
			want: []int{},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := twoSumII(tt.args.numbers, tt.args.target); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("twoSumII() = %v, want %v", got, tt.want)
			}
		})
	}
}
