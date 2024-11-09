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
        # Prevent moving to the same position
        if move.from_pos == move.to_pos:
            raise WrongMoveError()


class Pawn(Piece):
    def validate_move(self, board: np.array, move: PieceMove):
        super().validate_move(board, move)

        # Get the color of the piece at the starting position
        color = self.get_color(board, move.from_pos)

        # 1 for white (moves up), -1 for black (moves down)
        direction = 1 if color == "white" else -1

        # Determine the starting row for pawns
        start_pos = 1 if color == "white" else 6

        # Calculate the differences between positions
        col_diff = abs(move.to_pos[0] - move.from_pos[0])
        row_diff = move.to_pos[1] - move.from_pos[1]

        # Check for valid forward moves
        if move.from_pos[0] == move.to_pos[0]:
            # Move 1 block forward
            if row_diff == direction:
                print("moved 1 block")
                return
            # Move 2 blocks from starting position
            if move.from_pos[1] == start_pos and row_diff == 2 * direction:
                print("moved 2 blocks")
                return

        # Check for diagonal capture
        if col_diff == 1 and row_diff == direction:
            print("capture 1 block diagonally")
            return

        raise WrongMoveError()


class Knight(Piece):
    def validate_move(self, board: np.array, move: PieceMove):
        super().validate_move(board, move)

        col_diff = abs(move.from_pos[0] - move.to_pos[0])
        row_diff = abs(move.from_pos[1] - move.to_pos[1])

        # Check for the knight's "gama" move:
        if (col_diff == 2 and row_diff == 1) or (col_diff == 1 and row_diff == 2):
            print("valid gama move")
            return

        raise WrongMoveError()


class Bishop(Piece):
    def validate_move(self, board: np.array, move: PieceMove):
        super().validate_move(board, move)

        # Check if the move is diagonal
        if abs(move.from_pos[0] - move.to_pos[0]) == abs(move.from_pos[1] - move.to_pos[1]):
            print(f"valid diagonal move")
            return

        raise WrongMoveError()


class Rook(Piece):
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

        raise WrongMoveError()


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
            return

        raise WrongMoveError()


class King(Piece):
    def validate_move(self, board: np.array, move: PieceMove):
        super().validate_move(board, move)

        # Restrict the king's movement to one block
        if abs(move.from_pos[0] - move.to_pos[0]) <= 1 and abs(move.from_pos[1] - move.to_pos[1]) <= 1:
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
                print("valid diagonal move")
                return

        raise WrongMoveError()


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
