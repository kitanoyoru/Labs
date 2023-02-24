package code

import "github.com/kitanoyoru/Labs/AOIS/Lab1/pkg/utils"

func GetReverseCode(x int64) []byte {
	ans := utils.FormatBitsWithBaseTwo(uint64(x), x < 0)
	if x < 0 {
		for i := 1; i < len(ans); i++ {
			ans[i] ^= 1
		}
	}

	return ans
}
