from typing import Optional

from kivymd.uix.boxlayout import MDBoxLayout

from src.components import Table, Bar
from src.controllers import RootController


class RootView(MDBoxLayout):
    def __init__(self, controller, *args, **kwargs) -> None:
        super().__init__(args, kwargs)

        self._controller = controller

        self._bar = Bar(self._controller).build_widget()
        self._table = Table(self._controller).build_widget()

        self._root = MDBoxLayout(self.bar, self.table, id="root", orientation="vertical")

    def update(self) -> None:
        self._root.remove_widget(self._table)
        self._table = Table(self._controller).build_widget()
        self._root.add_widget(self._table)
