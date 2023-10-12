package leetcode

import (
	"reflect"
	"slices"
	"testing"
)

func Test_twoSum(t *testing.T) {
	type args struct {
		nums   []int
		target int
	}
	tests := []struct {
		name string
		args args
		want []int
	}{
		{
			name: "Exmaple 1",
			args: args{nums: []int{2, 7, 11, 15}, target: 9},
			want: []int{0, 1},
		},
		{
			name: "Exmaple 2",
			args: args{nums: []int{3, 2, 4}, target: 6},
			want: []int{1, 2},
		},
		{
			name: "Exmaple 3",
			args: args{nums: []int{3, 3}, target: 6},
			want: []int{0, 1},
		},
		{
			name: "No Solution",
			args: args{nums: []int{3, 3, 3}, target: 5},
			want: []int{},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := twoSum(tt.args.nums, tt.args.target)
			slices.Sort(got)
			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("twoSum() = %v, want %v", got, tt.want)
			}
		})
	}
}
