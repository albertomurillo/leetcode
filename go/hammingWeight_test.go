package leetcode

import (
	"strconv"
	"testing"
)

func Test_hammingWeight(t *testing.T) {
	type args struct {
		num string
	}
	tests := []struct {
		name string
		args args
		want int
	}{
		{
			"Exmaple 1",
			args{"00000000000000000000000000001011"},
			3,
		},
		{
			"Exmaple 2",
			args{"00000000000000000000000010000000"},
			1,
		},
		{
			"Exmaple 3",
			args{"11111111111111111111111111111101"},
			31,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			num, _ := strconv.ParseUint(tt.args.num, 2, 32)
			if got := hammingWeight(uint32(num)); got != tt.want {
				t.Errorf("hammingWeight() = %v, want %v", got, tt.want)
			}
		})
	}
}
