import numpy as np
from declarations import COLUMN_NAMES, ROW_NAMES, START_BOARD
from errors import BaseError, BoardLimitError, WrongTurnError
from models.common import PieceMove
from models.pieces import Piece, get_piece


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


class Validator:
    board: np.array
    move: PieceMove
    turn: GameTurn

    def __init__(self, board: np.array, move: PieceMove, turn: GameTurn):
        self.board = board
        self.move = move
        self.turn = turn

    @staticmethod
    def validate_input(board_move_split: list):
        from_pos_board, to_pos_board = board_move_split[0], board_move_split[1]
        Validator.__validate_input_move(from_pos_board)
        Validator.__validate_input_move(to_pos_board)

    @staticmethod
    def __validate_input_move(pos_board: str):
        pos_letter, pos_numb = pos_board[0].upper(), pos_board[1]
        if not (pos_letter in COLUMN_NAMES and int(pos_numb) in range(1, 9)):
            raise BoardLimitError()

    def __check_turn(self):
        if (
            Piece.get_color(self.board, self.move.from_pos)
            != self.turn.get_color()
        ):
            raise WrongTurnError()

    def validate(self):
        self.__check_turn()

        piece = get_piece(self.board[self.move.from_pos])
        piece.validate_move(self.board, self.move)


class ChessGame:
    chess_board: ChessBoard
    turn: GameTurn

    def __get_input(self) -> PieceMove:
        turn_color = self.turn.get_color()
        input_move_msg = f"({turn_color}'s turn) make your move: "
        input_move_split = input(input_move_msg).split()

        Validator.validate_input(input_move_split)
        return PieceMove(input_move_split)

    def validate_move(self, move: PieceMove):
        move_validator = Validator(self.chess_board.board, move, self.turn)
        move_validator.validate()

    def start(self):
        self.chess_board = ChessBoard()
        self.turn = GameTurn()
        while not self.chess_board.is_game_over():
            self.chess_board.print_board()
            try:
                next_move = self.__get_input()
                self.validate_move(next_move)
            except BaseError as error:
                print(error.get_error_msg())
                continue
            self.chess_board.make_move(next_move)
            self.turn.change_turn()
