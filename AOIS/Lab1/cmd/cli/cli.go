package cli

import (
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/code"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/float"
	"github.com/kitanoyoru/Labs/AOIS/Lab1/internal/operations"
	"github.com/sirupsen/logrus"
)

func ForInt(first, second int, log *logrus.Logger) {
	log.Infof("First:\n\tStraight:   %v\n\tReverse:    %v\n\tAdditional: %v\n", code.GetStraightCode(first), code.GetReverseCode(first), code.GetAdditionalCode(first))
	log.Infof("Second:\n\tStraight:   %v\n\tReverse:    %v\n\tAdditional: %v\n\n", code.GetStraightCode(second), code.GetReverseCode(second), code.GetAdditionalCode(second))

	log.Infof("X + Y   = %v\n", operations.Sum(first, second))
	log.Infof("X - Y   = %v\n", operations.Sum(first, -second))
	log.Infof("- X + Y = %v\n", operations.Sum(-first, second))
	log.Infof("- X - Y = %v\n\n", operations.Sum(-first, -second))

	log.Infof("X * Y       = %v\n", operations.Mul(first, second))
	log.Infof("X * (-Y)    = %v\n", operations.Mul(first, -second))
	log.Infof("(-X) + Y    = %v\n", operations.Mul(-first, second))
	log.Infof("(-X) * (-Y) = %v\n\n", operations.Mul(-first, -second))

	log.Infof("X / Y       = %v\n", operations.Div(first, second))
	log.Infof("X / (-Y)    = %v\n", operations.Div(first, -second))
	log.Infof("(-X) / Y    = %v\n", operations.Div(-first, second))
	log.Infof("(-X) / (-Y) = %v\n\n", operations.Div(-first, -second))
}

func ForFloat(first, second float32, log *logrus.Logger) {
	log.Infof("First:  %v\n", float.ToBinary(float32(first)))
	log.Infof("Second: %v\n\n", float.ToBinary(float32(second)))

	log.Infof("X + Y   = %v\n", float.Sum(first, second))
	log.Infof("X - Y   = %v\n", float.Sum(first, -second))
	log.Infof("- X + Y = %v\n", float.Sum(-first, second))
	log.Infof("- X - Y = %v\n\n", float.Sum(-first, -second))

}
