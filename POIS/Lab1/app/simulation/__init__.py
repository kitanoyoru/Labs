from .simulation import Simulation


def init_simulation(n_plants: int) -> Simulation:
    return Simulation(n_plants)