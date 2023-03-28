import math
import random
import datetime

import pygame

from enum import Enum
from typing import Iterable, Optional

from src.models.asteroid import Asteroid
from src.models.missile import Missile
from src.models.spaceship import Spaceship

from src.repository import StateRepository

from src.utils import load_sound, load_image_convert_alpha, distance, draw_centered


class GameState(Enum):
    PLAYING = 1
    DYING = 2
    GAME_OVER = 3
    STARTING = 4
    WELCOME = 5


class EventType(Enum):
    REFRESH = pygame.USEREVENT
    START = pygame.USEREVENT + 1
    RESTART = pygame.USEREVENT + 2


class Game:
    def __init__(self, repository: StateRepository) -> None:
        pygame.mixer.init()
        pygame.mixer.pre_init(44100, -16, 2, 2048)
        pygame.init()

        self.width = 1280
        self.height = 720
        self.screen = pygame.display.set_mode((self.width, self.height))

        self.bg_color = 0, 0, 0

        self.soundtrack = load_sound("soundtrack.wav")
        self.soundtrack.set_volume(0.3)

        self.die_sound = load_sound("die.wav")
        self.gameover_sound = load_sound("game_over.wav")
        self.missile_sound = load_sound("fire.wav")

        self.big_font = pygame.font.SysFont(None, 100)
        self.medium_font = pygame.font.SysFont(None, 50)
        self.small_font = pygame.font.SysFont(None, 25)

        self.repository = repository

        self.gameover_text = self.big_font.render("GAME OVER", True, (255, 0, 0))

        self.lives_image = load_image_convert_alpha("spaceship-off.png")

        self.FPS = 30
        pygame.time.set_timer(EventType.REFRESH.value, 1000 // self.FPS)

        self.death_distances = {"big": 90, "normal": 65, "small": 40}

        self.do_welcome()

        self.fire_time = datetime.datetime.now()

    def do_welcome(self) -> None:
        self.state = GameState.WELCOME
        
        score = 0
        state = self.repository.read_last_record()
        if state is not None:
            score = state["score"]

        self.welcome_asteroids = self.big_font.render("Asteroids", True, (255, 215, 0))
        self.welcome_desc = self.medium_font.render(
            f"[Click anywhere/press Enter] to begin! You're last record was {score}", True, (35, 107, 142)
        )

    def do_init(self) -> None:
        self.asteroids = []

        self.min_asteroid_distance = 350

        self.start()

        for i in range(4):
            self.make_asteroid()

        self.lives = 3
        self.score = 0

        self.counter = 0

    def make_asteroid(
        self, size: str = "big", pos: Optional[Iterable[int]] = None
    ) -> None:
        margin = 200

        if pos == None:
            rand_x = random.randint(margin, self.width - margin)
            rand_y = random.randint(margin, self.height - margin)

            while (
                distance((rand_x, rand_y), self.spaceship.position)
                < self.min_asteroid_distance
            ):
                rand_x = random.randint(0, self.width)
                rand_y = random.randint(0, self.height)

            temp_asteroid = Asteroid((rand_x, rand_y), size)

        else:
            temp_asteroid = Asteroid(pos, size)

        self.asteroids.append(temp_asteroid)

    def start(self) -> None:
        self.spaceship = Spaceship([self.width // 2, self.height // 2])
        self.missiles = []

        self.soundtrack.play(-1, 0, 1000)

        self.state = GameState.PLAYING

    def run(self) -> None:
        running = True

        while running:
            event = pygame.event.wait()
            if event.type == pygame.QUIT:
                running = False
            elif event.type == EventType.REFRESH.value:
                if self.state != GameState.WELCOME:
                    keys = pygame.key.get_pressed()

                    if keys[pygame.K_SPACE]:
                        new_time = datetime.datetime.now()
                        if new_time - self.fire_time > datetime.timedelta(seconds=0.15):
                            self.spaceship.fire()

                            self.missile_sound.play()

                            self.fire_time = new_time

                    if self.state == GameState.PLAYING:
                        if keys[pygame.K_RIGHT] or keys[pygame.K_d]:
                            self.spaceship.angle -= 10
                            self.spaceship.angle %= 360

                        if keys[pygame.K_LEFT] or keys[pygame.K_a]:
                            self.spaceship.angle += 10
                            self.spaceship.angle %= 360

                        if keys[pygame.K_UP] or keys[pygame.K_w]:
                            self.spaceship.is_throttle_on = True

                            if self.spaceship.speed < 20:
                                self.spaceship.speed += 1
                        else:
                            if self.spaceship.speed > 0:
                                self.spaceship.speed -= 1
                            self.spaceship.is_throttle_on = False

                        if len(self.spaceship.active_missiles) > 0:
                            self.missiles_physics()

                        if len(self.asteroids) > 0:
                            self.asteroids_physics()

                        self.physics()

                self.draw()
            elif event.type == EventType.START.value:
                pygame.time.set_timer(EventType.START.value, 0)
                if self.lives < 1:
                    self.game_over()
                else:
                    self.asteroids = []
                    for i in range(4):
                        self.make_asteroid()
                    self.start()
            elif event.type == EventType.RESTART.value:
                pygame.time.set_timer(EventType.RESTART.value, 0)
                self.state = GameState.STARTING
            elif event.type == pygame.MOUSEBUTTONDOWN and (
                self.state == GameState.STARTING or self.state == GameState.WELCOME
            ):
                self.do_init()
            elif (
                event.type == pygame.KEYDOWN
                and event.key == pygame.K_RETURN
                and (
                    self.state == GameState.STARTING or self.state == GameState.WELCOME
                )
            ):
                self.do_init()
            else:
                pass

    def game_over(self) -> None:
        self.soundtrack.stop()

        self.state = GameState.GAME_OVER
        self.gameover_sound.play()

        self.repository.save_record(record={"record": self.score})

        delay = int((self.gameover_sound.get_length() + 1) * 1000)
        pygame.time.set_timer(EventType.RESTART.value, delay)

    def die(self) -> None:
        self.soundtrack.stop()

        self.lives -= 1
        self.counter = 0
        self.state = GameState.DYING
        self.die_sound.play()

        delay = int((self.die_sound.get_length() + 1) * 1000)
        pygame.time.set_timer(EventType.START.value, delay)

    def physics(self) -> None:
        if self.state == GameState.PLAYING:
            self.spaceship.move()

    def missiles_physics(self) -> None:
        if len(self.spaceship.active_missiles) > 0:
            for missile in self.spaceship.active_missiles:
                missile.move()

                for asteroid in self.asteroids:
                    if asteroid.size == "big":
                        if distance(missile.position, asteroid.position) < 80:
                            self.asteroids.remove(asteroid)
                            if missile in self.spaceship.active_missiles:
                                self.spaceship.active_missiles.remove(missile)
                            self.make_asteroid(
                                "normal",
                                (asteroid.position[0] + 10, asteroid.position[1]),
                            )
                            self.make_asteroid(
                                "normal",
                                (asteroid.position[0] - 10, asteroid.position[1]),
                            )
                            self.score += 20

                    elif asteroid.size == "normal":
                        if distance(missile.position, asteroid.position) < 55:
                            self.asteroids.remove(asteroid)
                            if missile in self.spaceship.active_missiles:
                                self.spaceship.active_missiles.remove(missile)
                            self.make_asteroid(
                                "small",
                                (asteroid.position[0] + 10, asteroid.position[1]),
                            )
                            self.make_asteroid(
                                "small",
                                (asteroid.position[0] - 10, asteroid.position[1]),
                            )
                            self.score += 50
                    else:
                        if distance(missile.position, asteroid.position) < 30:
                            self.asteroids.remove(asteroid)
                            if missile in self.spaceship.active_missiles:
                                self.spaceship.active_missiles.remove(missile)

                            if len(self.asteroids) < 10:
                                self.make_asteroid()

                            self.score += 100

    def asteroids_physics(self) -> None:
        if len(self.asteroids) > 0:
            for asteroid in self.asteroids:
                asteroid.move()

                if (
                    distance(asteroid.position, self.spaceship.position)
                    < self.death_distances[asteroid.size]
                ):
                    self.die()

                elif distance(
                    asteroid.position, (self.width / 2, self.height / 2)
                ) > math.sqrt((self.width / 2) ** 2 + (self.height / 2) ** 2):
                    self.asteroids.remove(asteroid)
                    if len(self.asteroids) < 10:
                        self.make_asteroid(asteroid.size)

    def draw(self):
        self.screen.fill(self.bg_color)

        if self.state != GameState.WELCOME:
            self.spaceship.draw_on(self.screen)

            if len(self.spaceship.active_missiles) > 0:
                for missile in self.spaceship.active_missiles:
                    missile.draw_on(self.screen)

            if len(self.asteroids) > 0:
                for asteroid in self.asteroids:
                    asteroid.draw_on(self.screen)

            if self.state == GameState.PLAYING:
                self.counter += 1

                if self.counter == 20 * self.FPS:
                    if len(self.asteroids) < 15:
                        self.make_asteroid()

                    if self.min_asteroid_distance < 200:
                        self.min_asteroid_distance -= 50

                    self.counter = 0

            scores_text = self.medium_font.render(str(self.score), True, (0, 155, 0))
            draw_centered(
                scores_text,
                self.screen,
                (self.width - scores_text.get_width(), scores_text.get_height() + 10),
            )

            if self.state == GameState.GAME_OVER or self.state == GameState.STARTING:
                draw_centered(
                    self.gameover_text, self.screen, (self.width // 2, self.height // 2)
                )

            for i in range(self.lives):
                draw_centered(
                    self.lives_image,
                    self.screen,
                    (
                        self.lives_image.get_width() * i * 1.2 + 40,
                        self.lives_image.get_height() // 2,
                    ),
                )

        else:
            draw_centered(
                self.welcome_asteroids,
                self.screen,
                (
                    self.width // 2,
                    self.height // 2 - self.welcome_asteroids.get_height(),
                ),
            )

            draw_centered(
                self.welcome_desc,
                self.screen,
                (self.width // 2, self.height // 2 + self.welcome_desc.get_height()),
            )

        pygame.display.flip()
