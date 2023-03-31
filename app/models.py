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
    from_x: int
    from_y: int
    to_x: int
    to_y: int

    def __init__(self, start_conv, end_conv):
        self.from_x, self.from_y = start_conv[0], start_conv[1]
        self.to_x, self.to_y = end_conv[0], end_conv[1]

    @staticmethod
    def position_converter(board_pos: str) -> tuple[int, int]:
        board_pos_split = [*board_pos]
        start_pos, end_pos = (board_pos_split[0].upper(), board_pos_split[1])

        start_pos_conv = np.where(COLUMN_NAMES == start_pos)[0][0]
        end_pos_conv = int(end_pos) - 1

        return start_pos_conv, end_pos_conv

    @staticmethod
    def from_input_move(move_split) -> "PieceMove":
        start_pos, end_pos = (move_split[0], move_split[1])

        start_pos_conv = PieceMove.position_converter(start_pos)
        end_pos_conv = PieceMove.position_converter(end_pos)

        return PieceMove(start_pos_conv, end_pos_conv)


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
        pass

    def make_move(self, move: PieceMove) -> bool:
        pass

    def is_game_over(self) -> bool:
        pass
