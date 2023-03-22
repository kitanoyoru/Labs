import random

from typing import Iterable

from src.models.base import BaseGameModel

from src.utils import load_image_convert_alpha


class Asteroid(BaseGameModel):
    def __init__(self, position: Iterable[int], size: str, speed: int = 4) -> None:
        if size in ("big", "normal", "small"):
            str_filename = "asteroid-" + str(size) + ".png"
            super(Asteroid, self).__init__(
                position, load_image_convert_alpha(str_filename)
            )
            self.size = size

        else:
            return None

        self.position = list(position)

        self.speed = speed

        if bool(random.getrandbits(1)):
            rand_x = random.random() * -1
        else:
            rand_x = random.random()

        if bool(random.getrandbits(1)):
            rand_y = random.random() * -1
        else:
            rand_y = random.random()

        self.direction = [rand_x, rand_y]

    def move(self) -> None:
        self.position[0] += self.direction[0] * self.speed
        self.position[1] += self.direction[1] * self.speed
