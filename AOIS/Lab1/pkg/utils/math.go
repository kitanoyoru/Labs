package utils

import "math"

func IntPow(x, y int) int {
	return int(math.Pow(float64(x), float64(y)))
}
