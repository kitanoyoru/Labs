from flask_restful import Resource, reqparse

from typing import Tuple

from app.simulation.simulation import Simulation

class ControlSimulation(Resource):
    simulation: Simulation = None

    parser = reqparse.RequestParser()

    parser.add_argument("action", type=str, required=True)

    def get(self) -> str:
        info: str = ControlSimulation.simulation.get_info()
        return info

    def post(self) -> Tuple[dict, int]:
        data = ControlSimulation.parser.parse_args()

        action = data["action"]

        try:
            if ControlSimulation.simulation is None:
                raise Exception()

            ControlSimulation.simulation.call_action(action)
        except Exception as exc:
            return {"message": f"failed: {exc}"}, 500

        return {"message": "ok"}, 201
