class BaseError(Exception):
    error_msg: str

    def get_error_msg(self) -> str:
        return f"[Error]: ----- {self.error_msg} -----"


class BoardLimitError(BaseError):
    error_msg = "Your move is out of board limits"


class WrongTurnError(BaseError):
    error_msg = "Wrong turn, please try again"
