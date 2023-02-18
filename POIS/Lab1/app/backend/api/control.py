from flask_restful import Resource, reqparse

from typing import Tuple

from app import App
from app.models.actions import ActionType


class ControlSimulation(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("action", type=int, required=True)

    def get(self) -> str:
        info: str = ControlSimulation.simulation.get_info()
        return info

    def post(self) -> Tuple[dict, int]:
        data = ControlSimulation.parser.parse_args()

        action = data["action"]

        try:
            if App.simulation is None:
                raise Exception()

            action_type: ActionType = ActionType(action)
            ControlSimulation.simulation.call_action(action_type)
        except Exception as exc:
            return {"message": f"failed: {exc}"}, 500

        return {"message": "ok"}, 201
