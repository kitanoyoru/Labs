from typing import Optional

from kivymd.uix.boxlayout import MDBoxLayout

from src.components import Table, Bar
from src.components.dialogs import (
    AddStudentDialog,
    DeleteStudentDialog,
    FilterStudentDialog,
)
from src.controllers import RootController


class RootView(MDBoxLayout):
    def __init__(self, *args, **kwargs) -> None:
        super().__init__(args, kwargs)

        self.dialog = None

        self.bar = Bar(self.controller).build_widget()
        self.table = Table(self.controller).build_widget()

        self.root = MDBoxLayout(self.bar, self.table, id="root", orientation="vertical")

    def link_controller(self, controller: RootController) -> None:
        self.controller = controller

    def update(self) -> None:
        self.root.remove_widget(self.table)
        self.table = Table(self.controller).build_widget()
        self.root.add_widget(self.table)

    def show_student_adding_dialog(self) -> None:
        self.dialog = AddStudentDialog(self.controller).build_dialog()
        self.dialog.open()

    def show_student_filter_dialog(self) -> None:
        self.dialog = FilterStudentDialog(self.controller).build_dialog()
        self.dialog.open()

    def show_student_delete_dialog(self) -> None:
        self.dialog = DeleteStudentDialog(self.controller).build_dialog()
        self.dialog.open()

    def close_dialog(self) -> None:
        if self.dialog is not None:
            self.dialog.dismiss(force=True)
