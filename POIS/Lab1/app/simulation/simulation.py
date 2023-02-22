import os
import sys

from enum import Enum

from ..models.seed import AppleSeed, Seed
from ..models.place import FruitGarden
from ..models.state import State
from ..models.actions import ActionType, Irrigation, Drought

from app._settings import *
from app._utils import FileUtils
from app._errors import NotFoundPathErr


class SimulationFields(Enum):
    FRUIT_GARDEN = "fruit_garden"


class Simulation:
    def __init__(self, plants: int) -> None:
        self._n_plants = plants

        self._read_state()

    def call_action(self, action_type: ActionType) -> None:
        match action_type:
            case ActionType.IRRIGATION:
                action = Irrigation()
                self._fg.handle_action(action)
            case ActionType.DROUGHT:
                action = Drought()
                self._fg.handle_action(action)
            case ActionType.QUIT:
                self._write_state()
                sys.exit(0)

    def _read_state(self) -> dict:
        path = os.getenv(ENV_STATE_FILE)
        if path is None:
            raise NotFoundPathErr() 

        if FileUtils.is_file_exists(path):
            data = FileUtils.read_from_json(path)

            fg = data.get(SimulationFields.FRUIT_GARDEN.value)
            self._fg = State.get_fruit_garden(fg)
        else:
            seeds = [AppleSeed() for _ in range(self._n_plants)]
            self._fg = FruitGarden(seeds=seeds)

    def _write_state(self) -> None:
        state = self.get_info()
        path = os.getenv(ENV_STATE_FILE) # REFACTOR
        if path is None:
            raise NotFoundPathErr() 
        
        FileUtils.save_in_json(state, path)



    def get_info(self) -> dict:
        info = dict()

        info[SimulationFields.FRUIT_GARDEN.value] = self._fg.to_dict()

        return info
