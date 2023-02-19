from flask_restful import Resource, reqparse

from typing import Tuple

from app.backend import sim
from app.models.actions import ActionType


class ControlSimulation(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("action", type=int, required=True)

    def get(self) -> Tuple[dict, int]:
        print(simulation)
        try:
            if simulation is None:
                raise Exception()

            info = sim.get_info()
            return {"message": f"{info}"}, 201
        except Exception as exc:
            return {"message": f"failed: {exc}"}, 500


    def post(self) -> Tuple[dict, int]:
        data = ControlSimulation.parser.parse_args()

        action = data["action"]

        try:
            if simulation is None:
                raise Exception()

            action_type: ActionType = ActionType(action)
            simulation.call_action(action_type)
        except Exception as exc:
            return {"message": f"failed: {exc}"}, 500

        return {"message": "ok"}, 201
