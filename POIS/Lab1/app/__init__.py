from flask import Flask
from flask_restful import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from app.simulation import Simulation
from app.api import ControlSimulation

from ._settings import load_settings


class App:
    @staticmethod
    def create_app(n: int, settings_path: str) -> Flask:
        load_settings(settings_path)

        app = Flask(__name__)

        app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)

        sim = Simulation(n)

        api = Api(app)
        api.add_resource(
            ControlSimulation, "/control", resource_class_kwargs={"simulation": sim}
        )

        return app
