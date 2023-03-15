from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout

from src.controllers import RootController


class Table:
    def __init__(self, controller: RootController) -> None:
        self._controller = controller

    def build_widget(self) -> MDBoxLayout:
        return MDBoxLayout(
            MDDataTable(
                padding=10,
                elevation=0,
                use_pagination=True,
                pagination_menu_height=330,
                check=True,
                column_data=[
                    ("Full name", dp(50)),
                    ("Group No", dp(30)),
                    ("Exam 1", dp(50)),
                    ("Exam 2", dp(50)),
                    ("Exam 3", dp(50)),
                ],
                row_data=self._controller.get_student_info(),
            ),
            id="table",
        )
