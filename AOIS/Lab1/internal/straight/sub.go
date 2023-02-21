package straight

func Sub(a, b int64) []byte {
	if (a > 0 && b < 0) || (a < 0 && b > 0) {
		return Sum(a, -b)
	}

	if a < 0 && b < 0 {
		return Sum(a, b)
	}

	return Sum(a, (^b)+1)
}
