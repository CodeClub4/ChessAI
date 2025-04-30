class BaseError(Exception):
    default_error_type = "Unknown Error"
    default_error_msg = "please try again"

    def __init__(self, custom_msg=None):
        self.error_type = self.default_error_type
        self.error_msg = custom_msg if custom_msg else self.default_error_msg
        super().__init__(self.error_type, self.error_msg)

    def get_error_msg(self) -> str:
        return f"[Error] ----- {self.error_type}: {self.error_msg} -----"


class InvalidPlayerInputError(BaseError):
    default_error_type = "Invalid Player Input"


class InvalidBoardLimitationError(BaseError):
    default_error_type = "Invalid Board Limits"


class InvalidPieceExistenceError(BaseError):
    default_error_type = "Invalid Piece Existence"


class InvalidPlayerTurnError(BaseError):
    default_error_type = "Invalid Player Turn"


class InvalidPieceMoveError(BaseError):
    default_error_type = "Invalid Piece Move"


class InvalidPieceCaptureError(BaseError):
    default_error_type = "Invalid Piece Capture"
