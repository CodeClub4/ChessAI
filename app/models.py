import numpy as np

# Constant values
START_BOARD = np.array(
    [
        ["r", "n", "b", "q", "k", "b", "n", "r"],
        ["p", "p", "p", "p", "p", "p", "p", "p"],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        [" ", " ", " ", " ", " ", " ", " ", " "],
        ["P", "P", "P", "P", "P", "P", "P", "P"],
        ["R", "N", "B", "Q", "K", "B", "N", "R"],
    ]
)


class PieceMove:
    from_x: int
    from_y: int
    to_x: int
    to_y: int


class ChessBoard:
    board: np.array

    def __init__(self):
        self.board = np.copy(START_BOARD)

    def print_board(self):
        print(self.board)

    def is_valid_move(self, move: PieceMove) -> bool:
        pass

    def make_move(self, move: PieceMove) -> bool:
        pass

    def is_game_over(self) -> bool:
        pass