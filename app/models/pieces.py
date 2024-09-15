import numpy as np

from models.common import PieceMove


class Piece:
    @staticmethod
    def is_white(board: np.array, pos: tuple[int, int]) -> bool:
        if board[pos].islower():
            return True
        elif board[pos].isupper():
            return False

    def __get_piece_candidate_moves(self, move: PieceMove): ...

    def validate_move(self, board: np.array, move: PieceMove):
        pass


class Pawn(Piece):
    def validate_move(self, board: np.array, move: PieceMove):
        super().validate_move(board, move)


class Knight(Piece): ...


class Bishop(Piece): ...


class Rook(Piece):
    def __get_piece_candidate_moves(
        self, move: PieceMove
    ) -> list[tuple[int, int]]:
        y_pos = move.from_pos[0]
        x_pos = move.from_pos[1]

        candidate_moves = []
        # same_y, decrease_x
        for tmp_x in range(x_pos - 1, -1, -1):
            candidate_moves.append(())
            ...

        # same_y, increase_x

        # decrease_y, same_x
        # increase_y, same_x
        candidate_moves


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
