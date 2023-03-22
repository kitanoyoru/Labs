import math

from typing import Iterable

from pygame import Surface

from src.models.base import BaseGameModel
from src.models.missile import Missile

from src.utils import load_image_convert_alpha, rotate_center, draw_centered


class Spaceship(BaseGameModel):
    def __init__(self, position: Iterable[int]):
        super(Spaceship, self).__init__(
            position, load_image_convert_alpha("spaceship-off.png")
        )

        self.image_on = load_image_convert_alpha("spaceship-on.png")
        self.direction = [0, -1]
        self.is_throttle_on = False
        self.angle = 0

        self.active_missiles = []

    def draw_on(self, screen: Surface) -> None:
        if self.is_throttle_on:
            new_image, _ = rotate_center(
                self.image_on, self.image_on.get_rect(), self.angle
            )
        else:
            new_image, _ = rotate_center(self.image, self.image.get_rect(), self.angle)

        draw_centered(new_image, screen, self.position)

    def move(self) -> None:
        self.direction[0] = math.sin(-math.radians(self.angle))
        self.direction[1] = -math.cos(math.radians(self.angle))

        self.position[0] += self.direction[0] * self.speed
        self.position[1] += self.direction[1] * self.speed

    def fire(self):
        adjust = [0, 0]
        adjust[0] = math.sin(-math.radians(self.angle)) * self.image.get_width()
        adjust[1] = -math.cos(math.radians(self.angle)) * self.image.get_height()

        new_missile = Missile(
            (self.position[0] + adjust[0], self.position[1] + adjust[1] / 2), self.angle
        )

        self.active_missiles.append(new_missile)
