from kivymd.uix.boxlayout import MDBoxLayout
from kivymd.uix.button import MDRaisedButton


class Bar:
    def __init__(self, controller) -> None:
        self._controller = controller

    def build_widget(self) -> MDBoxLayout:
        return MDBoxLayout(
            MDRaisedButton(
                text="Drought", 
                size_hint=(1, 1), 
                elevation=0, 
                on_press=lambda event: self._on_drought()
            ),
            MDRaisedButton(
                text="Irrigation",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self._on_irrigation(),
            ),
            MDRaisedButton(
                text="Latest",
                size_hint=(1, 1),
                elevation=0,
                on_press=lambda event: self._on_get_latest(),
            ),

            id="bar",
            size=(200, 100),
            size_hint=(1, None),
            spacing=10,
            padding=10,
        )

    def _on_drought(self) -> None:
        self._controller._on_drought()

    def _on_irrigation(self) -> None:
        self._controller._on_irrigation()

    def _on_get_latest(self):
        self._controller._on_get_latest()
