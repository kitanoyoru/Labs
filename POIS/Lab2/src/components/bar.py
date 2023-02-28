from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton

from src.models.action import Action


class Bar:
    def __init__(self, controller) -> None:
        self.controller = controller

    def build_widget(self) -> MDBoxLayout:
        return MDBoxLayout(
            MDRaisedButton(
                text="Add",
                on_press=self._add_student
            ),
            MDRaisedButton(
                text="Remove",
                on_press=self._remove_student
            ),
            MDRaisedButton(
                text="Filter",
                on_press=self._filter_student
            ),
            id="Bar",
            size=(200, 100),
            size_hint=(1,None),
            spacing=10,
            padding=10
        )
    
    def _add_student(self) -> None:
        self.controller.dispatch(Action.ADD)

    def _remove_student(self) -> None:
        self.controller.dispatch(Action.REMOVE)
    
    def _filter_student(self) -> None:
        self.controller.dispatch(Action.FILTER)