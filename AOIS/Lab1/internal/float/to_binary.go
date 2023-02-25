package float

import (
	"math"
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

	var beforePoint, exp int
	var afterPoint float64
	for i, r := range fstr {
		if r == '.' {
			beforePoint, _ = strconv.Atoi(fstr[:i])
			afterPoint, _ = strconv.ParseFloat(fstr[i+1:], 32)
			exp = len(fstr) - i - 1
			break
		}
	}

	parsedBefore := utils.TrimLeftZero(code.GetStraightCode(beforePoint))
	parsedAfter := []byte{}

	afterPoint *= math.Pow10(-exp)
	for afterPoint != 0.0 {
		temp := afterPoint * 2.0
		if temp >= 1.0 {
			temp -= 1
			parsedAfter = append(parsedAfter, 1)
		} else {
			parsedAfter = append(parsedAfter, 0)
		}
		afterPoint = temp
	}

	expBytes := code.GetStraightCode(len(parsedBefore) - 1)[24:]

	mantBytes := append(parsedBefore[1:], parsedAfter...)
	if len(mantBytes) > 23 {
		mantBytes = mantBytes[:23]
	} else {
		for len(mantBytes) < 23 {
			mantBytes = append(mantBytes, 0)
		}
	}
	utils.ReverseSlice(&mantBytes)

	res := []byte{}
	if sign {
		res = append(res, 1)
	} else {
		res = append(res, 0)
	}

	res = append(res, expBytes...)
	res = append(res, mantBytes...)

	return res
}
