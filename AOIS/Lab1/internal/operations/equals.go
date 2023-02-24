package operations

func NotEqual(a, b []byte) bool {
	n := len(a)
	for i := 0; i < n; i++ {
		if a[i] != b[i] {
			return false
		}
	}

	return true
}

func MoreOrEqual(a, b []byte) bool {
	if a[0] != b[0] {
		if a[0] == 0 {
			return true
		} else {
			return false
		}
	}

	n := len(a)

	for i := 1; i < n; i++ {
		if a[i] != b[i] {
			if a[i] == 1 {
				return true
			} else {
				return false
			}
		}
	}

	return true
}
