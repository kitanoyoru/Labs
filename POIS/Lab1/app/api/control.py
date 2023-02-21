from flask_restful import Resource, reqparse

from typing import Tuple

from app.models.actions import ActionType
from app.simulation import Simulation


class ControlSimulation(Resource):
    parser = reqparse.RequestParser()

    parser.add_argument("action", type=int, required=True)

    def __init__(self, simulation: Simulation) -> None:
        self._sim: Optional[Simulation] = simulation

    def get(self) -> Tuple[dict, int]:
        try:
            if self._sim is None:
                raise Exception()

            info = self._sim.get_info()
            return {"message": info}, 201
        except Exception as exc:
            return {"message": f"failed: {exc}"}, 500

    def post(self) -> Tuple[dict, int]:
        data = ControlSimulation.parser.parse_args()

        action = data["action"]

        try:
            if self._sim is None:
                raise Exception()

            action_type: ActionType = ActionType(action)
            self._sim.call_action(action_type)
        except Exception as exc:
            return {"message": f"failed: {exc}"}, 500

        return {"message": "ok"}, 201
