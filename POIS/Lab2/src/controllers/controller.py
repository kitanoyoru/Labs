from typing import Union, Tuple, Any, List

from src.models.student import StudentModel
from src.models.lesson import Lesson
from src.models.action import StudentAction, DialogAction
from src.views.root_view import RootView
from src.repositories.student import StudentsRepository, StudentFilterOptions


class RootController:
    def __init__(self, repository: StudentsRepository) -> None:
        self._dialog = None
        self._repository = repository

        self._student_index = self._repository.list_all_students()

    def link_view(self, view: RootView) -> None:
        self._view = view

    def get_student_info(self) -> List[Tuple[Any, ...]]:
        return [student.to_table_row() for student in self._student_index]

    def dispatch(self, action: Union[StudentAction, DialogAction]) -> None:
        match action:
            case StudentAction.ADD:
                self._on_student_add()
            case StudentAction.FILTER:
                self._on_student_filter()
            case StudentAction.REMOVE:
                self._on_student_remove()

            case DialogAction.OPEN_ADD_DIALOG:
                self._on_open_add_dialog()
            case DialogAction.OPEN_FILTER_DIALOG:
                self._on_open_filter_dialog()
            case DialogAction.CLOSE_DIALOG:
                self._on_close_dialog()

    def _on_student_add(self):
        data = self._view.dialog.content_cls.ids
        try:
            lessons = Lesson.from_text(data.lessons.text)
            student = StudentModel(
                name=data.name.text, group=data.group.text, lessons=lessons
            )

            self._repository.add_student(student)
            self._student_index.append(student)

            self._view.close_dialog()
            self._view.update()
        except Exception as e:
            print(e)
            return

    def _on_student_filter(self):
        data = self._view.dialog.content_cls.ids
        try:
            opts = StudentFilterOptions(
                name=data.name.text,
                group=data.group.text,
                max=data.max.text,
                min=data.min.text,
                avg=data.avg.text,
            )

            self._student_index = self._repository.filter_student(opts)

            self._view.close_dialog()
            self._view.update()
        except Exception as e:
            print(e)
            return

    def _on_student_remove(self):
        data = self._view.dialog.content_cls.ids
        try:
            self._repository.delete_student(data.name.text)
            self._student_index = filter(
                lambda user: user.name == data.name.text, self._student_index
            )

            self._view.close_dialog()
            self._view.update()
        except Exception as e:
            print(e)
            return

    def _on_open_add_dialog(self):
        self._view.show_student_adding_dialog()

    def _on_open_filter_dialog(self):
        self._view.show_student_filter_dialog()

    def _on_open_delete_dialog(self):
        self._view.show_student_delete_dialog

    def _on_close_dialog(self):
        self._view.close_dialog()
