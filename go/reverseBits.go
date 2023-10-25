// https://leetcode.com/problems/reverse-bits

package leetcode

func reverseBits(num uint32) uint32 {
	var res uint32 = 0
	for i := 0; i < 32; i++ {
		bit := (num >> i) & uint32(1)
		res |= bit << (31 - i)
	}
	return res
}
