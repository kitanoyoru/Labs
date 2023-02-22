package operations

import "fmt"

func Sub(a, b int64) []byte {
	if (a > 0 && b < 0) || (a < 0 && b > 0) {
		fmt.Println(Sum(a, -b))
		return []byte{}
	}

	if a < 0 && b < 0 {
		return Sub(-b, -a)
	}

	fmt.Println(a + (^b + 1))

	return []byte{}
}
