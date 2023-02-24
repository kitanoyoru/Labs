package raw

import (
	"github.com/kitanoyoru/Labs/AOIS/Lab1/pkg/utils"
)

func RawSum(a, b []byte) []byte {
	res := []byte{}
	flag := false

	for i := len(a); i > 0; i-- {
		if (!flag && a[i-1] == 0 && b[i-1] == 0) || (flag && ((a[i-1] == 1 && b[i-1] == 0) || (a[i-1] == 0 && b[i-1] == 1))) {
			res = append(res, 0)
		}
		if (flag && a[i-1] == 1 && b[i-1] == 1) || (!flag && ((a[i-1] == 1 && b[i-1] == 0) || (a[i-1] == 0 && b[i-1] == 1))) {
			res = append(res, 1)
		}
		if (flag && a[i-1] == 0 && b[i-1] == 0) || (!flag && a[i-1] == 1 && b[i-1] == 1) {
			if flag {
				res = append(res, 1)
			} else {
				res = append(res, 0)
			}

			flag = !flag
		}
	}

	utils.ReverseSlice(&res)

	return res
}
