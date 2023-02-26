package raw

import (
	"github.com/kitanoyoru/Labs/AOIS/Lab1/pkg/utils"
)

func RawSum(a, b []byte) []byte {
	res := []byte{}
	carry := false

	for i := len(a); i > 0; i-- {
		if (!carry && a[i-1] == 0 && b[i-1] == 0) || (carry && ((a[i-1] == 1 && b[i-1] == 0) || (a[i-1] == 0 && b[i-1] == 1))) {
			res = append(res, 0)
		}
		if (carry && a[i-1] == 1 && b[i-1] == 1) || (!carry && ((a[i-1] == 1 && b[i-1] == 0) || (a[i-1] == 0 && b[i-1] == 1))) {
			res = append(res, 1)
		}
		if (carry && a[i-1] == 0 && b[i-1] == 0) || (!carry && a[i-1] == 1 && b[i-1] == 1) {
			if carry {
				res = append(res, 1)
			} else {
				res = append(res, 0)
			}

			carry = !carry
		}
	}

	utils.ReverseSlice(&res)

	return res
}
