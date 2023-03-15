from kivymd.uix.button import MDFlatButton
from kivymd.uix.dialog import MDDialog
from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.textfield import MDTextField

from src.controllers import RootController
from src.models.action import DialogAction, StudentAction


class FilterStudentDialog:
    def __init__(self, controller: RootController) -> None:
        self._controller = controller

    def build_dialog(self) -> MDDialog:
        return MDDialog(
            title="Add Student",
            type="custom",
            content_cls=MDBoxLayout(
                MDTextField(
                    id="name",
                    hint_text="Full name",
                    font_size="36",
                    helper_text_mode="on_error",
                ),
                MDTextField(
                    id="group",
                    hint_text="Group",
                    font_size="36",
                    helper_text_mode="on_error",
                ),
                MDTextField(
                    id="max",
                    hint_text="Max Score",
                    font_size="36",
                    helper_text_mode="on_error",
                ),
                MDTextField(
                    id="min",
                    hint_text="Min Score",
                    font_size="36",
                    helper_text_mode="on_error",
                ),
                MDTextField(
                    id="avg",
                    hint_text="Avg Score",
                    font_size="36",
                    helper_text_mode="on_error",
                ),
                id="form",
                orientation="vertical",
                spacing="15dp",
                size_hint_y=None,
                height="475dp",
            ),
            buttons=[
                MDFlatButton(
                    text="CANCEL",
                    theme_text_color="Custom",
                    on_release=lambda event: self._close_dialog(),
                ),
                MDFlatButton(
                    text="FILTER",
                    theme_text_color="Custom",
                    on_release=lambda event: self._filter_student(),
                ),
            ],
        )

    def _close_dialog(self) -> None:
        self._controller.dispatch(DialogAction.CLOSE_DIALOG)

    def _filter_student(self) -> None:
        self._controller.dispatch(StudentAction.FILTER)
