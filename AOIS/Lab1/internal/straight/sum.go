package straight

import (
	"github.com/kitanoyoru/Labs/AOIS/Lab1/pkg/utils"
)

// https://stackoverflow.com/questions/61748010/algorithms-add-two-n-bit-binary-numbers-what-is-a-loop-invariant-of-this-probl
func Sum(a, b int64) []byte {
	if a < 0 && b > 0 {
		return Sub(b, -a)
	} else if a > 0 && b < 0 {
		return Sub(a, -b)
	}

	x := utils.FormatBitsWithBaseTwo(uint64(a), a < 0)
	y := utils.FormatBitsWithBaseTwo(uint64(b), b < 0)

	var sign bool
	if a < 0 && b < 0 {
		sign = true
		x, y = x[1:], y[1:]
	}

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
