from typing import Optional

from kivymd.app import MDApp

from src._meta import __PROJECT_NAME__, __DB_URL__
from src._settings import __ACCENT_PALLETE__, __COLORS__, __PRIMARY_PALLETE__

from src.views import RootView
from src.controllers import RootController

from src.config import MongoConfig
from src.storage.mongo import MongoStorage
from src.repositories import StudentsRepository


class App(MDApp):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(*args, **kwargs)

        self.view: Optional[RootView] = None
        self.controller: Optional[RootController] = None

    def build(self):
        self.title = __PROJECT_NAME__

        #self.theme_cls.colors = __COLORS__
        #self.theme_cls.primary_palette = __PRIMARY_PALLETE__
        #self.theme_cls.accent_palette = __ACCENT_PALLETE__

        config = MongoConfig(url=__DB_URL__)
        db = MongoStorage(config=config)

        self.controller = RootController(db.handleStudents)
        self.view = RootView(self.controller)

        self.controller.link_view(self.view)

        return self.view.root
