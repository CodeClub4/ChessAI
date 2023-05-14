import numpy as np
from app.models.common import PieceMove


class Piece:
    @staticmethod
    def get_color(board: np.array, pos: tuple[int, int]) -> str:
        if board[pos].islower():
            return "white"
        elif board[pos].isupper():
            return "black"

    def validate_move(self, board: np.array, move: PieceMove):
        pass


class Pawn(Piece):
    def validate_move(self, board: np.array, move: PieceMove):
        super().validate_move(board, move)

        if move.from_pos[1] == move.to_pos[1]:
            print("same column")
            if move.to_pos[0] > move.from_pos[0]:
                print("moved front")
            if (board[move.to_pos] == " ") & (abs(move.to_pos[0] - move.from_pos[0]) == 1):
                print("free space, moved 1 block")
                return True

        if abs(move.from_pos[1] - move.to_pos[1]) == 1:
            print("different column")
            if move.to_pos[0] > move.from_pos[0]:
                print("moved front")
            if (board[move.to_pos] != " ") & (abs(move.to_pos[0] - move.from_pos[0]) == 1):
                print("valid space, moved 1 block")
                return True


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
