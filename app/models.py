import numpy as np

# Constant values
COLUMN_NAMES = np.array(["A", "B", "C", "D", "E", "F", "G", "H"])
ROW_NAMES = np.array(["8", "7", "6", "5", "4", "3", "2", "1", "0"])
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
    from_pos: tuple
    to_pos: tuple

    def __init__(self, board_move_split):
        from_board_pos, to_board_pos = (board_move_split[0], board_move_split[1])
        self.from_pos = PieceMove.position_converter(from_board_pos)
        self.to_pos = PieceMove.position_converter(to_board_pos)

    @staticmethod
    def position_converter(board_pos: str) -> tuple[int, int]:
        board_pos_split = [*board_pos]
        x_pos, y_pos = (board_pos_split[0].upper(), board_pos_split[1])

        x_pos_conv = np.where(COLUMN_NAMES == x_pos)[0][0]
        y_pos_conv = int(y_pos) - 1

        return y_pos_conv, x_pos_conv


class ChessBoard:
    board: np.array

    def __init__(self):
        self.board = np.copy(START_BOARD)

    def print_board(self):
        flipped_board = np.flipud(self.board)
        board_col_names_added = np.r_[flipped_board, [COLUMN_NAMES]]
        full_board = np.c_[ROW_NAMES, board_col_names_added]
        print(full_board)

    def is_valid_move(self, move: PieceMove) -> bool:
        return 1

    def make_move(self, move: PieceMove) -> bool:
        self.board[move.to_pos] = self.board[move.from_pos]
        self.board[move.from_pos] = " "

    def is_game_over(self) -> bool:
        return 0
