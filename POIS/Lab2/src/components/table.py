from kivy.metrics import dp
from kivymd.uix.datatables import MDDataTable
from kivymd.uix.boxlayout import MDBoxLayout


class Table:
    def __init__(self, controller) -> None:
        self.controller = controller

    def build_widget(self) -> MDBoxLayout:
        return MDBoxLayout(
            MDDataTable(
                padding=10,
                elevation=0,
                use_pagination=True,
                pagination_menu_height=330,
                check=True,
                column_data=[
                    ("Full name", dp(60)),
                    ("Group No", dp(30)),
                    ("Address", dp(60)),
                    ("Landline phone", dp(30)),
                    ("Mobile phone", dp(30)),
                ],
                row_data=props['controller'].get_customers()
            ),
            id='table_box',
        )