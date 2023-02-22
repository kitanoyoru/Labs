package main

import (
	"fmt"

	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/operations"
)

func main() {
	a, b := int64(10), int64(6)

	fmt.Printf("%v\n", operations.Sub(a, b))
}
