package operations

import (
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/code"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/constants"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/raw"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/pkg/utils"
)

func Div(a, b int) []byte {
	x := code.GetStraightCode(a)
	y := code.GetStraightCode(b)

	var sign bool
	if (a < 0 && b > 0) || (a > 0 && b < 0) {
		sign = true
	}

	x[0], y[0] = 0, 0

	res := constants.Zero32InBytes
	for utils.GreaterOrEqual(x, y) {
		y[0] = 1
		x = raw.RawSum(x, code.Straight2Additional(y, 32))
		res = raw.RawSum(res, constants.One32InBytes)
		y[0] = 0
	}

	if sign {
		res = append([]byte{1}, res...)
	} else {
		res = append([]byte{0}, res...)
	}

	return res
}
