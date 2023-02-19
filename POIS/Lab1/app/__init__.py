# from ._metadata import __version__

# from ._utils import check_versions

# check_versions()
# del check_versions

# from ._settings import settings

from typing import Optional

from flask import Flask

from .backend import init_backend
from .simulation import init_simulation, Simulation


class App:
    @staticmethod
    def create_app(n_plants: int) -> Flask:
        sim = init_simulation(n_plants)
        backend = init_backend(sim)

        return backend



