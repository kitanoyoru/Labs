# from ._metadata import __version__

# from ._utils import check_versions

# check_versions()
# del check_versions

# from ._settings import settings
from .backend.server import init_backend
from .simulation import init_simulation

from flask import Flask


def create_app(n_plants) -> Flask:
    _simulation = init_simulation(n_plants)
    _backend = init_backend(_simulation)



