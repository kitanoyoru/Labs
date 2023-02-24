package main

import (
	"flag"
	"os"

	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/code"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/operations"
	"github.com/sirupsen/logrus"
	easy "github.com/t-tomalak/logrus-easy-formatter"
)

func main() {
	log := &logrus.Logger{
		Out:   os.Stdout,
		Level: logrus.DebugLevel,
		Formatter: &easy.Formatter{
			TimestampFormat: "2006-01-02 15:04:05",
			LogFormat:       "%msg%",
		},
	}

	fistNumPtr := flag.Int("first", 0, "First number")
	secondNumPtr := flag.Int("second", 0, "Second number")

	flag.Parse()

	first := *fistNumPtr
	second := *secondNumPtr

	log.Infof("First:\n\tStraight:   %v\n\tReverse:    %v\n\tAdditional: %v\n", code.GetStraightCode(first), code.GetReverseCode(first), code.GetAdditionalCode(first))
	log.Infof("Second:\n\tStraight:   %v\n\tReverse:    %v\n\tAdditional: %v\n\n", code.GetStraightCode(second), code.GetReverseCode(second), code.GetAdditionalCode(second))

	log.Infof("X + Y   = %v\n", operations.Sum(first, second))
	log.Infof("X - Y   = %v\n", operations.Sum(first, -second))
	log.Infof("- X + Y = %v\n", operations.Sum(-first, second))
	log.Infof("- X - Y = %v\n", operations.Sum(-first, -second))
}
