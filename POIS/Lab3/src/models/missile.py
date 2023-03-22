import math

from typing import Iterable

from src.models.base import BaseGameModel

from src.utils import load_image_convert_alpha


class Missile(BaseGameModel):
    def __init__(self, position: Iterable[int], angle: int, speed: int = 15) -> None:
        super(Missile, self).__init__(position, load_image_convert_alpha("missile.png"))

        self.angle = angle
        self.speed = speed
        self.direction = [0, 0]

    def move(self) -> None:
        self.direction[0] = math.sin(-math.radians(self.angle))
        self.direction[1] = -math.cos(math.radians(self.angle))

        self.position[0] += self.direction[0] * self.speed
        self.position[1] += self.direction[1] * self.speed
