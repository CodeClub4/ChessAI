import numpy as np
from app.declarations import COLUMN_NAMES, ROW_NAMES, START_BOARD
from app.errors import BaseError, WrongTurnError
from app.models.common import PieceMove
from app.models.pieces import Piece, get_piece


class ChessBoard:
    board: np.array

    def __init__(self):
        self.board = np.copy(START_BOARD)

    def print_board(self):
        flipped_board = np.flipud((np.rot90(np.fliplr(self.board))))
        board_col_names_added = np.r_[flipped_board, [COLUMN_NAMES]]
        full_board = np.c_[ROW_NAMES, board_col_names_added]
        print(full_board)

    def make_move(self, move: PieceMove):
        self.board[move.to_pos] = self.board[move.from_pos]
        self.board[move.from_pos] = " "

    def is_game_over(self) -> bool:
        return False


class GameTurn:

    def __init__(self):
        self.white_turn = True

    def get_color(self):
        return "white" if self.white_turn else "black"

    def is_white_turn(self):
        return self.white_turn

    def is_black_turn(self):
        return not self.white_turn

    def change_turn(self):
        self.white_turn = not self.white_turn


class MoveValidator:
    board: np.array
    move: PieceMove
    turn: GameTurn

    def __init__(self, board: np.array, move: PieceMove, turn: GameTurn):
        self.board = board
        self.move = move
        self.turn = turn

    def __check_turn(self):
        if (
            Piece.get_color(self.board, self.move.from_pos)
            != self.turn.get_color()
        ):
            raise WrongTurnError()

    def __check_move_limitations(self): ...

    def validate(self):
        self.__check_turn()
        self.__check_move_limitations()

        piece = get_piece(self.board[self.move.from_pos])
        piece.validate_move(self.board, self.move)


class ChessGame:
    chess_board: ChessBoard
    turn: GameTurn

    def __get_input(self) -> PieceMove:
        turn_color = self.turn.get_color()
        input_move_msg = f"({turn_color}'s turn) make your move: "
        input_move = input(input_move_msg).split()
        return PieceMove(input_move)

    def __validate_move(self, move: PieceMove) -> tuple[bool, str]:
        try:
            move_validator = MoveValidator(
                self.chess_board.board, move, self.turn
            )
            move_validator.validate()
        except BaseError as error:
            return False, error.get_error_msg()
        return True, ""

    def start(self):
        self.chess_board = ChessBoard()
        self.turn = GameTurn()
        while not self.chess_board.is_game_over():
            # print the current board
            self.chess_board.print_board()

            # get user input
            next_move = self.__get_input()

            # validation step
            is_valid_move, error_msg = self.__validate_move(next_move)
            if not is_valid_move:
                print(error_msg)
                continue

            # make the move and update the board
            self.chess_board.make_move(next_move)

            # change player turn
            self.turn.change_turn()
