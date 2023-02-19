from ..models.seed import AppleSeed, Seed
from ..models.place import FruitGarden
from ..models.actions import ActionType, Drought

class Simulation:
    def __init__(self, plants: int) -> None:
        self._n_plants = plants

        seeds = [AppleSeed() for _ in range(self._n_plants)]
        self._fg = FruitGarden(seeds)

    def call_action(self, action_type: ActionType) -> None:
        match action_type:
            case ActionType.DROUGHT:
                action = Drought()
                self._fg.handle_action(action)

    def get_info(self) -> dict:
        info = dict()

        fg_info = self._fg.to_dict()
        info.update(fg_info)

        return info
        



    