import numpy as np
from app.models.common import PieceMove
from app.errors import WrongMoveError


class Piece:
    @staticmethod
    def get_color(board: np.array, pos: tuple[int, int]) -> str:
        if board[pos].islower():
            return "white"
        elif board[pos].isupper():
            return "black"

    def validate_move(self, board: np.array, move: PieceMove):
        pass


class Pawn(Piece): ...


class Knight(Piece): ...


class Bishop(Piece): ...


class Rook(Piece): ...


class Queen(Piece):
    def validate_move(self, board: np.array, move: PieceMove):
        super().validate_move(board, move)

        # Check if the move is in the same column
        if move.from_pos[0] == move.to_pos[0]:
            print("valid column move")
            return

        # Check if the move is in the same row
        if move.from_pos[1] == move.to_pos[1]:
            print("valid row move")
            return

        # Check if the move is diagonal
        if abs(move.from_pos[0] - move.to_pos[0]) == abs(move.from_pos[1] - move.to_pos[1]):
            print(f"valid diagonal move")
            return True

        raise WrongMoveError()


class King(Piece):
    def validate_move(self, board: np.array, move: PieceMove):
        pass


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
