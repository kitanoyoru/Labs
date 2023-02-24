package operations

import (
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/code"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/constants"
)

func Div(a, b int64) []byte {
	x := code.GetStraightCode(a)
	y := code.GetStraightCode(b)

	res := constants.Zero64InBytes

	var sign bool
	if (a < 0 && b < 0) || (a > 0 && b > 0) {
		sign = false
	} else {
		sign = true
	}

	x, y = x[1:], y[1:]

	for MoreOrEqual(x, y) {
		y[0] = 1
		x = RawSum(x, code.Straight2Additional(y))
		res = RawSum(res, constants.One64InBytes)
		y[0] = 0
	}

	if sign {
		res = append([]byte{1}, res...)
	} else {
		res = append([]byte{0}, res...)
	}

	return res
}
