import os
import math

import pygame

from typing import Iterable, Tuple


from pygame import Surface, Rect
from pygame.mixer import Sound


def load_image_convert_alpha(filename: str) -> Surface:
    return pygame.image.load(os.path.join("assets", "images", filename)).convert_alpha()


def load_sound(filename: str) -> Sound:
    return pygame.mixer.Sound(os.path.join("assets", "sounds", filename))


def draw_centered(
    surface1: Surface, surface2: Surface, position: Iterable[int]
) -> None:
    rect = surface1.get_rect()
    rect = rect.move(position[0] - rect.width // 2, position[1] - rect.height // 2)
    surface2.blit(surface1, rect)


def rotate_center(image: Surface, rect: Rect, angle: float) -> Tuple[Surface, Rect]:
    rotate_image = pygame.transform.rotate(image, angle)
    rotate_rect = rotate_image.get_rect(center=rect.center)
    return rotate_image, rotate_rect


def distance(p: Iterable[int], q: Iterable[int]) -> float:
    return math.sqrt((p[0] - q[0]) ** 2 + (p[1] - q[1]) ** 2)
