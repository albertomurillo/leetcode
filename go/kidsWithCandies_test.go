// https://leetcode.com/problems/kids-with-the-greatest-number-of-candies

package leetcode

import (
	"reflect"
	"testing"
)

func Test_kidsWithCandies(t *testing.T) {
	type args struct {
		candies      []int
		extraCandies int
	}
	tests := []struct {
		name string
		args args
		want []bool
	}{
		{
			name: "Example 1",
			args: args{[]int{2, 3, 5, 1, 3}, 3},
			want: []bool{true, true, true, false, true},
		},
		{
			name: "Example 2",
			args: args{[]int{4, 2, 1, 1, 2}, 1},
			want: []bool{true, false, false, false, false},
		},
		{
			name: "Example 3",
			args: args{[]int{12, 1, 12}, 10},
			want: []bool{true, false, true},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := kidsWithCandies(tt.args.candies, tt.args.extraCandies); !reflect.DeepEqual(got, tt.want) {
				t.Errorf("kidsWithCandies() = %v, want %v", got, tt.want)
			}
		})
	}
}
