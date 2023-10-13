package leetcode

import "testing"

func Test_isPalindrome(t *testing.T) {
	type args struct {
		s string
	}
	tests := []struct {
		name string
		args args
		want bool
	}{
		{
			"Example 1",
			args{"A man, a plan, a canal: Panama"},
			true,
		},
		{
			"Example 2",
			args{"race a car"},
			false,
		},
		{
			"Example 3",
			args{" "},
			true,
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			if got := isPalindrome(tt.args.s); got != tt.want {
				t.Errorf("isPalindrome() = %v, want %v", got, tt.want)
			}
		})
	}
}
