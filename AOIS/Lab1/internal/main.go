package main

import (
	"fmt"

	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/straight"
)

func main() {
	a, b := int64(-10), int64(6)

	fmt.Printf("%v\n", straight.Sum(a, b))
}
