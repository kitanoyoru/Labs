package constants

var Max32InBytes []byte
var Zero32InBytes []byte
var One32InBytes []byte

func init() {
	for i := 0; i < 32; i++ {
		Max32InBytes = append(Max32InBytes, 1)
		Zero32InBytes = append(Zero32InBytes, 0)
		One32InBytes = append(One32InBytes, 0)
	}
	One32InBytes[31] = 1
}
