package operations

import (
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/code"
)

// https://stackoverflow.com/questions/61748010/algorithms-add-two-n-bit-binary-numbers-what-is-a-loop-invariant-of-this-probl
func Sum(a, b int64) []byte {
	if a < 0 && b > 0 {
		return Sub(b, -a)
	} else if a > 0 && b < 0 {
		return Sub(a, -b)
	}

	x := code.GetStraightCode(a)
	y := code.GetStraightCode(b)

	var sign bool
	if a < 0 && b < 0 {
		sign = true
		x, y = x[1:], y[1:]
	}

	res := baseSum(x, y, sign)

	return res
}

func baseSum(x, y []byte, sign bool) []byte {
	var res []byte
	var carry byte

	x, y, n := makeBinaryLenEqual(x, y)

	for i := n - 1; i >= 0; i-- {
		fb, sb := x[i], y[i]

		sum := fb ^ sb ^ carry
		res = append([]byte{sum}, res...)

		carry = (fb & sb) | (sb & carry) | (fb & carry)
	}

	if carry != 0 {
		res = append([]byte{1}, res...)
	}

	if sign {
		res = append([]byte{1}, res...)
	}

	return res
}
