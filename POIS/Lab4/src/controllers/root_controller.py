from typing import Optional, List, Tuple, Any 

from src.api.http import HttpFirstLabAPI
from src.models import ActionType, Place

class RootController:
    def __init__(self, api: HttpFirstLabAPI) -> None:
        self._api = api

        self._place_index: Optional[Place] = None 

    def link_view(self, view) -> None:
        self._view = view

    def get_table_info(self) -> List[Tuple[Any, ...]]:
        if self._place_index is None:
            self.__get_latest()

        res = []

        res.extend([("fruit", fruit.name, fruit.current_growth) for fruit in self._place_index.fruits])
        res.extend([("seed", seed.name, seed.current_growth) for seed in self._place_index.seeds])
        res.extend([("tree", tree.name, tree.current_growth) for tree in self._place_index.trees])

        return res

    def dispatch(self, action: ActionType) -> None:
        match action:
            case ActionType.DROUGHT:
                self._on_drought()
            case ActionType.IRRIGATION:
                self._on_irrigation()
            case ActionType.LATEST:
                self._on_get_latest()

    def _on_drought(self) -> None:
        data = self._api.send_drought_action()
        self._place_index = Place(**data)
        self._view.update()

    def _on_irrigation(self) -> None:
        data = self._api.send_irrigation_action()
        self._place_index = Place(**data)
        self._view.update()

    def _on_get_latest(self):
        self.__get_latest()
        self._view.update()

    def __get_latest(self):
        data = self._api.get_info()
        print(data)
        self._place_index = Place(**data)
