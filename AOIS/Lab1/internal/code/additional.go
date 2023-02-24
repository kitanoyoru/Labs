package code

import (
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/constants"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/raw"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/pkg/utils"
)

func GetAdditionalCode(x int) []byte {
	ans := utils.FormatBitsWithBaseTwo(uint32(x), x < 0)
	return Straight2Additional(ans)
}

func Addition2Reverse(bytes []byte) []byte {
	if bytes[0] == 0 {
		return bytes
	}

	return raw.RawSum(bytes, constants.Max32InBytes)
}
