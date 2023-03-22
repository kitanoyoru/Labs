from src.game import Game


class App:
    def __init__(self) -> None:
        self._game = Game()

    def run(self) -> None:
        self._game.run()
