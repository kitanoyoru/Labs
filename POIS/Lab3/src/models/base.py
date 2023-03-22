from typing import Iterable

from pygame import Surface

from src.utils import draw_centered


class BaseGameModel:
    def __init__(self, position: Iterable[int], image: Surface, speed: int = 0) -> None:
        self.image = image
        self.position = list(position[:])
        self.speed = speed

    def draw_on(self, screen):
        draw_centered(self.image, screen, self.position)

    def size(self):
        return max(self.image.get_height(), self.image.get_width())

    def radius(self):
        return self.image.get_width() / 2
