package code

import (
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/constants"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/raw"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/pkg/utils"
)

func GetStraightCode(x int64) []byte {
	ans := utils.FormatBitsWithBaseTwo(uint64(x), x < 0)
	return ans
}

func Straight2Additional(bytes []byte) []byte {
	var sign bool
	if bytes[0] != 0 {
		sign = true
	}

	if !sign {
		return bytes
	}

	ans := []byte{0}

	for i := 1; i < len(bytes); i++ {
		if bytes[i] == 1 {
			ans = append(ans, 0)
		} else {
			ans = append(ans, 1)
		}
	}

	ans = raw.RawSum(ans, constants.One64InBytes)

	return ans
}

func Straight2Reverse(bytes []byte) []byte {
	var sign bool
	if bytes[0] != 0 {
		sign = true
	}

	if !sign {
		return bytes
	}

	ans := []byte{}

	for _, byte := range bytes {
		ans = append(ans, ^byte)
	}

	ans[0] ^= 1

	return ans
}
