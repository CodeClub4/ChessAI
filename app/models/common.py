import numpy as np
from app.declarations import COLUMN_NAMES


class PieceMove:
    from_pos: tuple[int, int]
    to_pos: tuple[int, int]

    def __init__(self, board_move_split: list):
        from_pos_board, to_pos_board = board_move_split[0], board_move_split[1]
        self.from_pos = self.__position_converter(from_pos_board)
        self.to_pos = self.__position_converter(to_pos_board)

    @staticmethod
    def __position_converter(pos_board: str) -> tuple[int, int]:
        x_pos_board, y_pos_board = (pos_board[0].upper(), pos_board[1])

        x_pos_array = int(np.where(COLUMN_NAMES == x_pos_board)[0][0])
        y_pos_array = int(y_pos_board) - 1

        return x_pos_array, y_pos_array
