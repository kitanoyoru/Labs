import sys

from enum import Enum

from app._utils import *
from app._errors import *
from app._settings import *

from ..models.seed import AppleSeed, Seed
from ..models.place import FruitGarden
from ..models.state import State
from ..models.actions import ActionType, Drought


class SimulationFields(Enum):
    FRUIT_GARDEN = "fruit_garden"

class Simulation:
    def __init__(self, plants: int) -> None:
        self._n_plants = plants

        path = os.getenv(ENV_STATE_FILE)
        if path is None:
            raise NotFoundPathErr() 

        if is_file_exists(path):
            data = read_from_json(path)

            fg = data.get(SimulationFields.FRUIT_GARDEN.value)
            self._fg = State.get_fruit_garden(fg)
        else:
            seeds = [AppleSeed() for _ in range(self._n_plants)]
            self._fg = FruitGarden(seeds=seeds)

    def call_action(self, action_type: ActionType) -> None:
        match action_type:
            case ActionType.DROUGHT:
                action = Drought()
                self._fg.handle_action(action)
            case ActionType.QUIT:
                state = self.get_info()
                path = os.getenv(ENV_STATE_FILE) # REFACTOR
                if path is None:
                    raise NotFoundPathErr() 
                
                save_in_json(state, path)

                sys.exit(0)

    def get_info(self) -> dict:
        info = dict()

        info[SimulationFields.FRUIT_GARDEN.value] = self._fg.to_dict()

        return info
