# from ._metadata import __version__

# from ._utils import check_versions

# check_versions()
# del check_versions

# from ._settings import settings

from flask import Flask

from .backend.server import init_backend
from .simulation import init_simulation


class App:
    simulation: Optional[Simulation] = None

    @classmethod
    def create_app(cls, n_plants: int) -> Flask:
        cls.simulation = init_simulation(n_plants)
        backend = init_backend()

        return backend



