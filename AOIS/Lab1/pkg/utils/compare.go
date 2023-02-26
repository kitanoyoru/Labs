package utils

func Equal(a, b []byte) bool {
	if len(b) != len(a) {
		return false
	}

	n := len(a)

	for i := 0; i < n; i++ {
		if a[i] != b[i] {
			return false
		}
	}

	return true
}

func NotEqual(a, b []byte) bool {
	return !Equal(a, b)

}

func GreaterOrEqual(a, b []byte) bool {
	if a[0] != b[0] {
		if a[0] == 0 {
			return true
		} else {
			return false
		}
	}

	if a[0] == 1 {
		for i := 0; i < len(a); i++ {
			if a[i] != b[i] {
				if a[i] == 0 {
					return true
				} else {
					return false
				}
			}
		}
	} else {
		for i := 0; i < len(a); i++ {
			if a[i] != b[i] {
				if a[i] == 1 {
					return true
				} else {
					return false
				}
			}
		}
	}

	return true
}
