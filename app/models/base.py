import numpy as np

from declarations import COLUMN_NAMES, ROW_NAMES, START_BOARD
from errors import BaseError, WrongTurnError
from models.common import PieceMove
from models.pieces import Piece, get_piece


class ChessBoard:
    board: np.array

    def __init__(self):
        self.board = np.copy(START_BOARD)

    def print_board(self):
        flipped_board = np.flipud(self.board)
        board_col_names_added = np.r_[flipped_board, [COLUMN_NAMES]]
        full_board = np.c_[ROW_NAMES, board_col_names_added]
        print(full_board)

    def make_move(self, move: PieceMove):
        self.board[move.to_pos] = self.board[move.from_pos]
        self.board[move.from_pos] = " "

    def is_game_over(self) -> bool:
        return False


class MoveValidator:
    board: np.array
    move: PieceMove
    white_turn: bool

    def __init__(self, board: np.array, move: PieceMove, white_turn: bool):
        self.board = board
        self.move = move
        self.white_turn = white_turn

    def check_turn(self):
        if Piece.is_white(self.board, self.move.from_pos) != self.white_turn:
            raise WrongTurnError()

    def check_move_limitations(self):
        ...

    def validate(self):
        self.check_turn()
        self.check_move_limitations()

        piece = get_piece(self.board[self.move.from_pos])
        piece.validate_move(self.board, self.move)


class ChessGame:
    chess_board: ChessBoard
    white_turn: bool

    def get_input(self) -> PieceMove:
        turn_color = "white" if self.white_turn else "black"
        input_move_msg = f"({turn_color}'s turn) make your move: "
        input_move = input(input_move_msg).split()
        return PieceMove(input_move)

    def validate_move(self, move: PieceMove) -> tuple[bool, str]:
        try:
            move_validator = MoveValidator(
                self.chess_board.board, move, self.white_turn
            )
            move_validator.validate()
        except BaseError as error:
            return False, error.get_error_msg()
        return True, ""

    def start(self):
        self.chess_board = ChessBoard()
        self.white_turn = True
        while not self.chess_board.is_game_over():
            # print the current board
            self.chess_board.print_board()

            # get user input
            next_move = self.get_input()

            # validation step
            is_valid_move, error_msg = self.validate_move(next_move)
            if not is_valid_move:
                print(error_msg)
                continue

            # make the move and update the board
            self.chess_board.make_move(next_move)

            # change player turn
            self.white_turn = not self.white_turn
