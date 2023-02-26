from kivymd.uix.boxlayout import MDBoxLayout


class MainView(MDBoxLayout):
    def __init__(self, controller, *args, **kwargs) -> None:
        super().__init__(args, kwargs)

        self.controller = controller
