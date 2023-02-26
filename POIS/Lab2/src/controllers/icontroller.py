from abc import ABC, abstractclassmethod


class IController(ABC):
    @abstractclassmethod
    def get_view() -> IView:
        pass