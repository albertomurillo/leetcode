// https://leetcode.com/problems/valid-anagram

package leetcode

import "testing"

func Test_isAnagram(t *testing.T) {
	type args struct {
		s string
		t string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			name: "Example 1",
			args: args{"anagram", "nagaram"},
			want: true,
		},
		{
			name: "Example 2",
			args: args{"rat", "car"},
			want: false,
		},
		{
			name: "Not same length",
			args: args{"horse", "sore"},
			want: false,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isAnagram(tt.args.s, tt.args.t); got != tt.want {
				t.Errorf("isAnagram() = %v, want %v", got, tt.want)
			}
		})
	}
}
