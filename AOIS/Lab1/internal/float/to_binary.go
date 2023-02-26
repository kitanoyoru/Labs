package float

import (
	"fmt"
	"strconv"

	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/code"
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
			exp = len(fstr) - i - 1
			break
		}
	}

	res := []byte{}
	if sign {
		res = append(res, 1)
	} else {
		res = append(res, 0)
	}

	mantissa, _ := strconv.Atoi(fmt.Sprintf("%v%v", beforePoint, afterPoint))

	res = append(res, code.GetStraightCode(exp)[23:]...)
	res = append(res, code.GetStraightCode(mantissa)[9:]...)

	return res
}
