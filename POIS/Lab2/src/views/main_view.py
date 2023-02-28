from kivymd.uix.boxlayout import MDBoxLayout


class MainView(MDBoxLayout):
    def __init__(self, controller, *args, **kwargs) -> None:
        super().__init__(args, kwargs)

        self.controller = controller
        self.dialog = None
        
        self.bar = Bar(self.controller).build_widget()
        self.table = Table(self.controller).build_widget()

        self.root = MDBoxLayout(self.bar, self.table)

    def update(self) -> None:
        self.root.remove_widget(self.table)
        self.table = Table(self.controller)
        self.root.add_widget(self.table)

    def open_student_adding_dialog(self):
        self.dialog = AddStudentDialog(self.controller)
        self.dialog.open()

    def open_student_filter_dialog(self):
        self.dialog = FilterStudentDialog(self.controller)
        self.dialog.open()

    def close_dialog(self):
        self.dialog.dismiss(force=True)

    


    
