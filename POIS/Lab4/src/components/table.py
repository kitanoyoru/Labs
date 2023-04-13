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
                    ("Name", dp(50)),
                    ("Current growth", dp(50))
                ],
                row_data=self._controller.get_table_info(),
            ),
            id="table",
        )