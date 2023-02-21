package straight

func makeBinaryLenEqual(x, y []byte) ([]byte, []byte, int) {
	xlen, ylen := len(x), len(y)
	if xlen < ylen {
		for i := 0; i < ylen-xlen; i++ {
			x = append([]byte{0}, x...)
		}
		return x, y, ylen
	} else if xlen > ylen {
		for i := 0; i < xlen-ylen; i++ {
			y = append([]byte{0}, y...)
		}
	}

	return x, y, xlen
}
