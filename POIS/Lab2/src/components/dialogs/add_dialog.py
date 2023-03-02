from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField


class AddStudentDialog:
    def __init__(self, controlller) -> None:
        self.controller = controller

    def build_dialog() -> MDDialog:
        return MDDialog(
            title="adder",
            type="custom",
            content_cls=MDBoxLayout(
                MDTextField(
                    id="fullname",
                    hint_text="Full name",
                    font_size="36",
                )
            )
        )



