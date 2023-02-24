package operations

import (
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/code"
)

// https://stackoverflow.com/questions/61748010/algorithms-add-two-n-bit-binary-numbers-what-is-a-loop-invariant-of-this-probl
func Sum(a, b int64) []byte {
	x := code.GetStraightCode(a)
	y := code.GetStraightCode(b)

	res := RawSum(x, y)

	return res
}

func RawSum(a, b []byte) []byte {
	var sign bool
	if a[0] == 0 && b[0] == 0 {
		sign = false
		a, b = a[1:], b[1:]
	}

	res := baseSum(a, b, sign)

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
