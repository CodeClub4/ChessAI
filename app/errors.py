class BaseError(Exception):
    default_error_msg = "An error occurred"

    def __init__(self, custom_msg=None):
        self.error_msg = custom_msg if custom_msg else self.default_error_msg
        super().__init__(self.error_msg)

    def get_error_msg(self) -> str:
        return f"[Error]: ----- {self.error_msg} -----"


class WrongTurnError(BaseError):
    default_error_msg = "Wrong turn, please try again"


class WrongMoveError(BaseError):
    default_error_msg = "Wrong move, please try again"


class WrongCaptureError(BaseError):
    default_error_msg = "Wrong capture, please try again"
