package operations

import (
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/code"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/constants"
)

func Mult(a, b int64) []byte {
	x := code.GetStraightCode(a)
	y := code.GetStraightCode(b)

	res := constants.Zero64InBytes

	var sign bool
	if (a < 0 && b < 0) || (a > 0 && b > 0) {
		sign = false
	} else {
		sign = true
	}

	x[0], y[0] = 0, 0

	for NotEqual(y, constants.Zero64InBytes) {
		res = RawSum(x, res)
		y = RawSum(y, constants.One64InBytes)
	}

	if sign {
		res = append([]byte{1}, res...)
	}

	return res
}
