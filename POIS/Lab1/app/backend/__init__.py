import os

from flask import Flask
from flask_restful import Api
from werkzeug.middleware.proxy_fix import ProxyFix

from app.simulation.simulation import Simulation

from .api.control import ControlSimulation

from app.simulation import Simulation


sim: Optional[Simulation] = None

def init_backend(s: Simulation) -> Flask:
    app = Flask(__name__)

    global sim
    sim = s

    app.wsgi_app = ProxyFix(app.wsgi_app, x_for=1, x_host=1)

    api = Api(app)

    api.add_resource(ControlSimulation, "/control")

    return app