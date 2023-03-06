package float

import (
	"fmt"

	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/code"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/raw"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/pkg/utils"
)

func FromBinary(x []byte) float32 {
	fmt.Println(x)
	first := (1 - 2*int(x[0])) * binaryFloatToInt(x[9:])
	s := raw.RawSum(x[1:9], code.GetStraightCode(127))
	fmt.Println(s)
	fmt.Println(binaryFloatToInt(s))
	second := utils.IntPow(10, binaryFloatToInt(s))
	return float32(first * second)
}

func binaryFloatToInt(x []byte) int {
	num := 0

	for i := len(x) - 1; i > 1; i-- {
		num += utils.IntPow(2, (len(x)-i)*int(x[i-1]))
	}

	if x[0] == 1 {
		return -num
	}

	return num
}
