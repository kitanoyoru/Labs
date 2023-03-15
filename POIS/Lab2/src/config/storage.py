from dataclasses import dataclass, field


__STUDENTS_COLLECTION__ = "students"


@dataclass
class StorageConfig:
    Url: str

    StudentsCollection: str = field(default=__STUDENTS_COLLECTION__, init=False)
