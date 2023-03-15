from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton

from src.models.action import DialogAction, TableAction


class Bar:
    def __init__(self, controller) -> None:
        self._controller = controller

    def build_widget(self) -> MDBoxLayout:
        return MDBoxLayout(
            MDRaisedButton(
                text="Add", 
                size_hint=(1, 1), 
                elevation=0, 
                on_press=lambda event: self._add_student()
            ),
            MDRaisedButton(
                text="Delete",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self._delete_student(),
            ),
            MDRaisedButton(
                text="Filter",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self._filter_student(),
            ),
            MDRaisedButton(
                text="Latest",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self._get_latest(),
            ),

            id="bar",
            size=(200, 100),
            size_hint=(1, None),
            spacing=10,
            padding=10,
        )

    def _add_student(self) -> None:
        self._controller.dispatch(DialogAction.OPEN_ADD_DIALOG)

    def _delete_student(self) -> None:
        self._controller.dispatch(DialogAction.OPEN_DELETE_DIALOG)

    def _filter_student(self) -> None:
        self._controller.dispatch(DialogAction.OPEN_FILTER_DIALOG)

    def _get_latest(self) -> None:
        self._controller.dispatch(TableAction.LATEST)
