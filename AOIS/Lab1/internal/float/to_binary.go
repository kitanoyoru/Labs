package float

import (
	"fmt"
	"strconv"

	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/code"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/pkg/utils"
)

func ToBinary(num float32) []byte {
	var sign bool
	if num < 0 {
		sign = true
		num *= -1

	}

	fstr := strconv.FormatFloat(float64(num), 'f', -1, 32)

	var beforePoint, afterPoint, exp int
	for i, r := range fstr {
		if r == '.' {
			beforePoint, _ = strconv.Atoi(fstr[:i])
			afterPoint, _ = strconv.Atoi(fstr[i+1:])
			exp = i - (len(fstr) - 1)
			break
		}
	}

	mantissa_int, _ := strconv.Atoi(fmt.Sprintf("%v%v", beforePoint, afterPoint))

	mantissa_bin := []byte{}

	for mantissa_int > 0 {
		b := byte(mantissa_int % 2)
		mantissa_int = mantissa_int / 2
		mantissa_bin = append(mantissa_bin, b)
	}

	for len(mantissa_bin) < 23 {
		mantissa_bin = append(mantissa_bin, 0)
	}

	res := []byte{}

	res = append(res, mantissa_bin...)

	raw_exp := code.GetStraightCode(exp)
	bin_exp := append([]byte{raw_exp[0]}, raw_exp[25:]...)
	utils.ReverseSlice(&bin_exp)

	res = append(res, bin_exp...)

	if sign {
		res = append(res, 1)
	} else {
		res = append(res, 0)
	}

	utils.ReverseSlice(&res)

	return res
}
