import numpy as np

# Constant values
COLUMN_NAMES = np.array(["A", "B", "C", "D", "E", "F", "G", "H"])
ROW_NAMES = np.array(["8", "7", "6", "5", "4", "3", "2", "1", " "])
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
    from_pos: tuple[int, int]
    to_pos: tuple[int, int]

    def __init__(self, board_move_split):
        from_pos_board, to_pos_board = (board_move_split[0], board_move_split[1])
        self.from_pos = self.position_converter(from_pos_board)
        self.to_pos = self.position_converter(to_pos_board)

    @staticmethod
    def position_converter(pos_board: str) -> tuple[int, int]:
        x_pos_board, y_pos_board = (pos_board[0].upper(), pos_board[1])

        x_pos_array = np.where(COLUMN_NAMES == x_pos_board)[0][0]
        y_pos_array = int(y_pos_board) - 1

        return y_pos_array, x_pos_array


class ChessBoard:
    board: np.array

    def __init__(self):
        self.board = np.copy(START_BOARD)

    def print_board(self):
        flipped_board = np.flipud(self.board)
        board_col_names_added = np.r_[flipped_board, [COLUMN_NAMES]]
        full_board = np.c_[ROW_NAMES, board_col_names_added]
        print(full_board)

    def is_white_piece(self, move: PieceMove) -> bool:
        if self.board[move.from_pos].islower():
            return True
        elif self.board[move.from_pos].isupper():
            return False

    def is_valid_move(self, move: PieceMove) -> bool:
        return True

    def make_move(self, move: PieceMove):
        self.board[move.to_pos] = self.board[move.from_pos]
        self.board[move.from_pos] = " "

    def is_game_over(self) -> bool:
        return False
