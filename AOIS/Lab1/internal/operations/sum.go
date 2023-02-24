package operations

import (
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/code"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/raw"
)

// https://stackoverflow.com/questions/61748010/algorithms-add-two-n-bit-binary-numbers-what-is-a-loop-invariant-of-this-probl
func Sum(a, b int) []byte {
	x := code.GetAdditionalCode(a)
	y := code.GetAdditionalCode(b)

	res := raw.RawSum(x, y)

	return code.Reverse2Straight(code.Addition2Reverse(res))
}
