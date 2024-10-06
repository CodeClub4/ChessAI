import numpy as np

from app.models.common import PieceMove
from app.errors import WrongMoveError


class Piece:
    @staticmethod
    def is_white(board: np.array, pos: tuple[int, int]) -> bool:
        if board[pos].islower():
            return True
        elif board[pos].isupper():
            return False

    def validate_move(self, board: np.array, move: PieceMove):
        pass


class Pawn(Piece):
    ...


class Knight(Piece):
    def validate_move(self, board: np.array, move: PieceMove):
        super().validate_move(board, move)

        row_diff = abs(move.from_pos[0] - move.to_pos[0])
        col_diff = abs(move.from_pos[1] - move.to_pos[1])

        # Check for the knight's "gama" move:
        if (row_diff == 2 and col_diff == 1) or (row_diff == 1 and col_diff == 2):
            print("valid gama move")
            return True

        raise WrongMoveError()


class Bishop(Piece):
    ...


class Rook(Piece):
    ...


class Queen(Piece):
    ...


class King(Piece):
    ...


PIECE_CLASS_MAP = {
    "p": Pawn,
    "n": Knight,
    "b": Bishop,
    "r": Rook,
    "q": Queen,
    "k": King,
}


def get_piece(piece_char: str) -> Piece:
    piece_class = PIECE_CLASS_MAP[piece_char.lower()]
    return piece_class()
