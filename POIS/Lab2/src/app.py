from typing import Optional

from kivymd.app import MDApp

from ._meta import *
from ._settings import * 


class App(MDApp):
    def __init__(self) -> None:
        self.view: Optional[IView] = None
        self.controller: Optional[IController] = None

    def build(self) -> None:
        self.title = __PROJECT_NAME__ 

        self.theme_cls.colors = __COLORS__
        self.theme_cls.primary_palette = __PRIMARY_PALLETE__
        self.theme_cls.accent_palette = __ACCENT_PALLETE__ 

        self.controller = MainController()
        self.view = MainView(self.controller)

        return self.view

    