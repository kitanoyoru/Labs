

from ..models.seed import AppleSeed, Seed
from ..models.place import FruitGarden
from ..models.actions import Drought

class Simulation:
    ACTIONS = {
        "drought": Drought() 
    }
    
    def __init__(self, plants: int) -> None:
        self._n_plants = plants

        seeds = [AppleSeed() for _ in range(self._n_plants)]
        self.fg = FruitGarden(seeds)

    def call_action(self, action_type: str) -> None:
        action = Simulation.ACTIONS.get(action_type)

        if isinstance(action, Drought):
            self.fg.cb_ob_drought()



    