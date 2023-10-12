// https://leetcode.com/problems/greatest-common-divisor-of-strings/

package leetcode

import "testing"

func Test_gcdOfStrings(t *testing.T) {
	type args struct {
		str1 string
		str2 string
	}
	tests := []struct {
		name string
		args args
		want string
	}{
		{
			name: "Example 1",
			args: args{"ABCABC", "ABC"},
			want: "ABC",
		},
		{
			name: "Example 2",
			args: args{"ABABAB", "ABAB"},
			want: "AB",
		},
		{
			name: "Example 3",
			args: args{"LEET", "CODE"},
			want: "",
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := gcdOfStrings(tt.args.str1, tt.args.str2); got != tt.want {
				t.Errorf("gcdOfStrings() = %v, want %v", got, tt.want)
			}
		})
	}
}
