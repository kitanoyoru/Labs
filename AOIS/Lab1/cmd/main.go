package main

import (
	"flag"
	"os"
	"strconv"

	"github.com/kitanoyoru/Labs/AOIS/Lab1/cmd/cli"
	"github.com/sirupsen/logrus"
	easy "github.com/t-tomalak/logrus-easy-formatter"
)

func main() {
	log := &logrus.Logger{
		Out:   os.Stdout,
		Level: logrus.DebugLevel,
		Formatter: &easy.Formatter{
			LogFormat: "%msg%",
		},
	}

	firstNumPtr := flag.String("first", "0", "First number")
	secondNumPtr := flag.String("second", "0", "Second number")
	intModePtr := flag.Bool("float-mode", false, "Usage mode")

	flag.Parse()

	mode := *intModePtr

	if mode {
		first, _ := strconv.ParseFloat(*firstNumPtr, 32)
		second, _ := strconv.ParseFloat(*secondNumPtr, 32)

		cli.ForFloat(float32(first), float32(second), log)
	} else {
		first, _ := strconv.Atoi(*firstNumPtr)
		second, _ := strconv.Atoi(*secondNumPtr)

		cli.ForInt(first, second, log)
	}
}
