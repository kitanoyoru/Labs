package float

import (
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/code"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/constants"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/operations"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/raw"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/pkg/utils"
)

func Sum(a, b float32) []byte {
	x := ToBinary(a)
	y := ToBinary(b)

	if utils.GreaterOrEqual(y[1:9], x[1:9]) {
		x, y = y, x
	}

	for utils.NotEqual(x[1:9], y[1:9]) {
		copy(x[1:9], raw.RawSum(x[1:9], constants.MinusOne8InBytes))
		copy(x[9:], operations.RawMul(x[9:], code.GetStraightCode(10)[9:], false))
	}

	signedMantissaX := append([]byte{x[0]}, x[9:]...)
	signedMantissaY := append([]byte{y[0]}, y[9:]...)

	out := raw.RawSum(signedMantissaX, signedMantissaY)

	res := []byte{out[0]}
	res = append(res, x[1:9]...)
	res = append(res, out[9:]...)

	return res
}
