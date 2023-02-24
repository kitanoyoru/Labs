package raw

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

	x, y, n := MakeBinaryLenEqual(x, y)

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

func MakeBinaryLenEqual(x, y []byte) ([]byte, []byte, int) {
	xlen, ylen := len(x), len(y)
	if xlen < ylen {
		for i := 0; i < ylen-xlen; i++ {
			x = append([]byte{0}, x...)
		}
		return x, y, ylen
	} else if xlen > ylen {
		for i := 0; i < xlen-ylen; i++ {
			y = append([]byte{0}, y...)
		}
	}

	return x, y, xlen
}
