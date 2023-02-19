# from ._metadata import __version__

# from ._utils import check_versions

# check_versions()
# del check_versions

# from ._settings import settings

import os

from flask import Flask
from flask_restful import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from app.simulation import init_simulation, Simulation

from app.api import ControlSimulation


class App:
    @staticmethod
    def create_app(n: int) -> Flask:
        app = Flask(__name__)

        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)

        sim = init_simulation(n)

        api = Api(app)
        api.add_resource(
            ControlSimulation, "/control", resource_class_kwargs={"simulation": sim}
        )

        return app
