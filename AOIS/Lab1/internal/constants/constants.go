package constants

var Zero64InBytes []byte
var One64InBytes []byte

func init() {
	patternZero := []byte{0, 0, 0, 0}
	patternOne := []byte{1, 1, 1, 1}

	copy(Zero64InBytes, patternZero)
	copy(One64InBytes, patternOne)

	for i := 0; i < 64; i *= 2 {
		copy(Zero64InBytes[i:], Zero64InBytes[:i])
		copy(One64InBytes[i:], One64InBytes[:i])
	}
}
