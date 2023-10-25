package leetcode

import (
	"strconv"
	"testing"
)

func Test_reverseBits(t *testing.T) {
	type args struct {
		num string
	}
	tests := []struct {
		name string
		args args
		want uint32
	}{
		{
			"Example 1",
			args{"00000010100101000001111010011100"},
			964176192,
		},
		{
			"Example 2",
			args{"11111111111111111111111111111101"},
			3221225471,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			num, _ := strconv.ParseUint(tt.args.num, 2, 32)
			if got := reverseBits(uint32(num)); got != tt.want {
				t.Errorf("reverseBits() = %v, want %v", got, tt.want)
			}
		})
	}
}
