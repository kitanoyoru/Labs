package code

import (
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/constants"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/raw"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/pkg/utils"
)

func GetStraightCode(x int) []byte {
	ans := utils.FormatBitsWithBaseTwo(uint32(x), x < 0)
	return ans
}

func Straight2Additional(bytes []byte, length int) []byte {
	if bytes[0] == 0 {
		return bytes
	}

	res := []byte{bytes[0]}

	for i := 1; i < len(bytes); i++ {
		if bytes[i] == 1 {
			res = append(res, 0)
		} else {
			res = append(res, 1)
		}
	}

	return raw.RawSum(res, constants.One32InBytes[32-length:])
}

func Straight2Reverse(bytes []byte) []byte {
	if bytes[0] == 0 {
		return bytes
	}

	res := []byte{1}

	for i := 1; i < len(bytes); i++ {
		if bytes[i] == 1 {
			res = append(res, 0)
		} else {
			res = append(res, 1)
		}
	}

	return res
}
