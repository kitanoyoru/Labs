class NotFoundPathErr(Exception):
    def __init__(self, msg="specify path to file") -> None:
        super().__init__(self.msg)
