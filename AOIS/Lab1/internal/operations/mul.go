package operations

import (
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/code"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/constants"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/raw"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/pkg/utils"
)

func Mul(a, b int) []byte {
	x := code.GetStraightCode(a)
	y := code.GetStraightCode(b)

	var sign bool
	if (a < 0 && b > 0) || (a > 0 && b < 0) {
		sign = true
	}

	return RawMul(x, y, sign)

}

func RawMul(x, y []byte, sign bool) []byte {
	x[0], y[0] = 0, 0

	res := constants.Zero32InBytes
	for utils.NotEqual(y, constants.Zero32InBytes) {
		res = raw.RawSum(res, x)
		y = raw.RawSum(y, constants.Max32InBytes)
	}

	if sign {
		res[0] = 1
	} else {
		res[0] = 0
	}

	return res
}
