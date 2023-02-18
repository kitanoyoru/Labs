import os
import pymongo

from flask import Flask
from flask_restful import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from app.simulation.simulation import Simulation

from .api.control import ControlSimulation


def init_backend(simulation: Simulation) -> Flask:
    app = Flask(__name__)

    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)

    api = Api(app)

    api.add_resource(ControlSimulation, "/control")

    return app