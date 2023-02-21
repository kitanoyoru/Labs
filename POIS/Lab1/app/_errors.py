class NotFoundPathErr(Exception):
    def __init__(self, message="specify path to file") -> None:
        self.message = message
        super().__init__(message)

class NotFoundSimulationInstance(Exception):
    def __init__(self, message="internal error with simulatiob object") -> None:
        self.message = message
        super().__init__(message)