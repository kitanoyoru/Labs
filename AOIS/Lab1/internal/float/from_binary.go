package float

import (
	"math"

	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/code"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/operations"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/pkg/utils"
)

func FromBinary(x []byte) float32 {
	first := float32((1 - 2*int(x[0])) * binaryFloatToInt(x[9:]))
	s := operations.SumStraightBin(x[1:9], code.GetStraightCode(127)[16:], 8)
	second := float32(math.Pow10(binaryFloatToInt(s)))
	return float32(first * second)
}

func binaryFloatToInt(x []byte) int {
	num := 0

	for i := len(x); i > 1; i-- {
		num += utils.IntPow(2, (len(x)-i)) * int(x[i-1])
	}

	if x[0] == 1 {
		return -num
	}

	return num
}
