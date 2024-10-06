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

    def validate_move(self, board: np.array, move: PieceMove, white_turn: bool):
        pass


class Pawn(Piece):
    def validate_move(self, board: np.array, move: PieceMove, white_turn: bool):
        super().validate_move(board, move, white_turn)

        # 1 for white_turn (up), -1 for not white_turn (down)
        direction = 1 if white_turn else -1

        # Move in the same column
        if move.to_pos[0] == move.from_pos[0] + direction and move.from_pos[1] == move.to_pos[1]:
            print("moved", "up" if white_turn else "down")
            print("same column")
            print("moved 1 block")
            return True

        # Move diagonally
        if move.to_pos[0] == move.from_pos[0] + direction and abs(move.from_pos[1] - move.to_pos[1]) == 1:
            print("moved", "up" if white_turn else "down")
            print("different column")
            print("moved 1 block")
            return True

        raise WrongMoveError()


class Knight(Piece): ...


class Bishop(Piece): ...


class Rook(Piece): ...


class Queen(Piece): ...


class King(Piece): ...


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
