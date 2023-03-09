package operations

import (
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/code"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/raw"
)

func Sum(a, b int) []byte {
	x := code.GetAdditionalCode(a)
	y := code.GetAdditionalCode(b)

	res := raw.RawSum(x, y)

	return code.Reverse2Straight(code.Addition2Reverse(res))
}

func SumStraightBin(a, b []byte, length int) []byte {
	x := code.Straight2Additional(a, length)
	y := code.Straight2Additional(b, length)

	res := raw.RawSum(x, y)

	return code.Reverse2Straight(code.Addition2Reverse(res))
}
