package leetcode

import (
	"reflect"
	"sort"
	"testing"
)

func Test_groupAnagrams(t *testing.T) {
	type args struct {
		strs []string
	}
	tests := []struct {
		name string
		args args
		want [][]string
	}{
		{
			"Example 1",
			args{[]string{"eat", "tea", "tan", "ate", "nat", "bat"}},
			[][]string{{"bat"}, {"nat", "tan"}, {"ate", "eat", "tea"}},
		},
		{
			"Example 2",
			args{[]string{""}},
			[][]string{{""}},
		},
		{
			"Example 3",
			args{[]string{"a"}},
			[][]string{{"a"}},
		},
	}
	for _, tt := range tests {
		t.Run(tt.name, func(t *testing.T) {
			got := groupAnagrams(tt.args.strs)
			for _, val := range got {
				sort.Strings(val)
			}
			sort.Slice(got, func(i, j int) bool {
				for n := 0; (n < len(got[i])) && (n < len(got[j])); n++ {
					if got[i][n] < got[j][n] {
						return true
					}
					if got[i][n] > got[j][n] {
						return false
					}
				}
				return len(got[i]) < len(got[j])
			})

			for _, val := range tt.want {
				sort.Strings(val)
			}
			sort.Slice(tt.want, func(i, j int) bool {
				for n := 0; (n < len(tt.want[i])) && (n < len(tt.want[j])); n++ {
					if tt.want[i][n] < tt.want[j][n] {
						return true
					}
					if tt.want[i][n] > tt.want[j][n] {
						return false
					}
				}
				return len(tt.want[i]) < len(tt.want[j])
			})

			if !reflect.DeepEqual(got, tt.want) {
				t.Errorf("groupAnagrams() = %v, want %v", got, tt.want)
			}
		})
	}
}
