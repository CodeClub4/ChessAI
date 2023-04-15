import numpy as np

from models.common import PieceMove


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
    def validate_move(self, board: np.array, move: PieceMove):
        super().validate_move(board, move)


class Knight(Piece):
    ...


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
