package straight

func Mult(x, y []byte) []byte {
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

	return res

}
