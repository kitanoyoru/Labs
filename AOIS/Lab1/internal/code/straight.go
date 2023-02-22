package code

import "github.com/kitanoyoru/Labs/AOIS/Lab1/pkg/utils"

func GetStraightCode(x int64) []byte {
	ans := utils.FormatBitsWithBaseTwo(uint64(x), x < 0)
	return ans
}
