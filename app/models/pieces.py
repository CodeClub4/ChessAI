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

        # Determine the starting position
        start_pos = 1 if white_turn else 6

        row_diff = move.to_pos[0] - move.from_pos[0]
        col_diff = abs(move.from_pos[1] - move.to_pos[1])

        # Check for valid forward moves
        if move.from_pos[1] == move.to_pos[1]:
            # Move 1 block forward
            if row_diff == direction:
                print("moved 1 block")
                return True
            # Move 2 blocks from starting position
            if move.from_pos[0] == start_pos and row_diff == 2 * direction:
                print("moved 2 blocks")
                return True

        # Check for diagonal capture
        if row_diff == direction and col_diff == 1:
            print("capture 1 block diagonally")
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
