from typing import Union, Tuple, Any, List

from src.models.exam import Exam
from src.models.student import StudentModel
from src.models.action import StudentAction, DialogAction, TableAction
from src.repositories.student import StudentsRepository, StudentFilterOptions


class RootController:
    def __init__(self, repository: StudentsRepository) -> None:
        self._dialog = None
        self._repository = repository

        self._student_index = self._repository.list_all_students()

    def link_view(self, view) -> None:
        self._view = view

    def get_student_info(self) -> List[Tuple[Any, ...]]:
        return [student.to_table_row() for student in self._student_index]

    def dispatch(self, action: Union[StudentAction, DialogAction]) -> None:
        match action:
            case StudentAction.ADD:
                self._on_student_add()
            case StudentAction.FILTER:
                self._on_student_filter()
            case StudentAction.DELETE:
                self._on_student_remove()

            case DialogAction.OPEN_ADD_DIALOG:
                self._on_open_add_dialog()
            case DialogAction.OPEN_FILTER_DIALOG:
                self._on_open_filter_dialog()
            case DialogAction.OPEN_DELETE_DIALOG:
                self._on_open_delete_dialog()
            case DialogAction.CLOSE_DIALOG:
                self._on_close_dialog()

            case TableAction.LATEST:
                self._on_get_latest() 

    def _on_student_add(self):
        data = self._view.dialog.content_cls.ids

        exams = Exam.from_text(data.exams.text)
        student = StudentModel(
            name=data.name.text, group=data.group.text, exams=exams
        )

        self._repository.add_student(student)
        self._student_index.append(student)

        self._view.close_dialog()
        self._view.update()

    def _on_student_filter(self):
        data = self._view.dialog.content_cls.ids
        
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

    def _on_student_remove(self):
        data = self._view.dialog.content_cls.ids
        
        self._repository.delete_student(data.name.text)
        self._student_index = list(filter(
            lambda user: user.name != data.name.text, self._student_index
        ))

        self._view.close_dialog()
        self._view.update()

    def _on_open_add_dialog(self):
        self._view.show_student_adding_dialog()

    def _on_open_filter_dialog(self):
        self._view.show_student_filter_dialog()

    def _on_open_delete_dialog(self):
        self._view.show_student_delete_dialog()

    def _on_close_dialog(self):
        self._view.close_dialog()


    def _on_get_latest(self):
        self._student_index = self._repository.list_all_students()
        self._view.update()
