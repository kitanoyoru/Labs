package code

import "github.com/kitanoyoru/Labs/AOIS/Lab1/pkg/utils"

func GetReverseCode(x int) []byte {
	res := utils.FormatBitsWithBaseTwo(uint32(x), x < 0)
	return Straight2Reverse(res)
}

func Reverse2Straight(bytes []byte) []byte {
	return Straight2Reverse(bytes)
}
