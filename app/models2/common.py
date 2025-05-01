import numpy as np
from app.declarations import COLUMN_NAMES


class TurnManager:

    def __init__(self, white_player, black_player):
        self.players = {
            "white": white_player,
            "black": black_player
        }
        self.current_color = "white"

    def get_current_player(self):
        return self.players[self.current_color]

    def change_turn(self):
        self.current_color = "black" if self.current_color == "white" else "white"


class PieceMove:
    from_pos: tuple[int, int]
    to_pos: tuple[int, int] = None

    def __init__(self, board_move_split: list):
        from_pos_board = board_move_split[0]
        self.from_pos = self.__position_converter(from_pos_board)

        if len(board_move_split) > 1:
            to_pos_board = board_move_split[1]
            self.to_pos = self.__position_converter(to_pos_board)

    @staticmethod
    def __position_converter(pos_board: str) -> tuple[int, int]:
        x_pos_board, y_pos_board = (pos_board[0].upper(), pos_board[1])

        x_pos_array = int(np.where(COLUMN_NAMES == x_pos_board)[0][0])
        y_pos_array = int(y_pos_board) - 1

        return x_pos_array, y_pos_array

    def is_spectate_move(self):
        return self.to_pos is None


class GameResignedException(Exception):
    default_exception_type = "GAME OVER"

    def __init__(self, player_name: str, player_color: str):
        self.exception_type = self.default_exception_type
        self.player_name = player_name
        self.player_color = player_color
        super().__init__(self.get_exception_msg())

    def get_exception_msg(self) -> str:
        return f"[{self.exception_type}] {self.player_name} as {self.player_color} has resigned!"
