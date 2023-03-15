from typing import Optional

from kivymd.app import MDApp

from src._meta import __PROJECT_NAME__
from src._settings import __ACCENT_PALLETE__, __COLORS__, __PRIMARY_PALLETE__

from src.views import RootView
from src.controllers import RootController


class App(MDApp):
    def __init__(self) -> None:
        self.view: Optional[RootView] = None
        self.controller: Optional[RootController] = None

    def build(self):
        self.title = __PROJECT_NAME__

        self.theme_cls.colors = __COLORS__
        self.theme_cls.primary_palette = __PRIMARY_PALLETE__
        self.theme_cls.accent_palette = __ACCENT_PALLETE__

        self.controller = RootController()
        self.view = RootView()

        # upd: cringe ._.
        self.view.link_controller(self.controller)
        self.controller.link_view(self.view)

        return self.view
