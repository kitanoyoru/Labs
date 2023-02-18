// https://cs.opensource.google/go/go/+/refs/tags/go1.20:src/strconv/itoa.go;drc=fb79da299127b3ff85e14f37e4616a26e6c2a720;l=88

package main

import "fmt"

const deBruijn32 = 0x077CB531

const digits = "0123456789abcdefghijklmnopqrstuvwxyz"

var deBruijn32tab = [32]byte{
	0, 1, 28, 2, 29, 14, 24, 3, 30, 22, 20, 15, 25, 17, 4, 8,
	31, 27, 13, 23, 21, 19, 16, 7, 26, 12, 18, 6, 11, 5, 10, 9,
}

func FormatBitsWithBaseTwo(num uint64, sign bool) []byte {
	var a [64 + 1]byte // 64bits + 1 for sign

	i := len(a)

	if sign {
		num = -num
	}

	shift := uint(getTrailingZeros(uint(2))) & 7
	base := uint64(2)
	mask := uint(base) - 1 // == 1 << shift - 1

	for num >= base {
		i--
		a[i] = digits[uint(num)&mask] - 48
		num >>= shift
	}

	i--
	a[i] = digits[uint(num)] - 48

	if sign {
		i--
		a[i] = '1' - 48
	}

	return a[i:]
}

func getTrailingZeros(x uint) int {
	return int(deBruijn32tab[(x&-x)*deBruijn32>>(32-5)])
}

func main() {
	a := 30
	fmt.Printf("%v\n", FormatBitsWithBaseTwo(uint64(a), a < 0))
}
