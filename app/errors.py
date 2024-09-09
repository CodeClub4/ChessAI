class BaseError(Exception):
    error_msg: str

    def get_error_msg(self) -> str:
        return f"[Error]: ----- {self.error_msg} -----"


class WrongTurnError(BaseError):
    error_msg = "Wrong turn, please try again"
