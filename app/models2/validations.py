import numpy as np
from app.errors import *
from app.models2.common import TurnManager, PieceMove
from app.models2.pieces import get_piece, Piece


class Validator:

    def __init__(self, board: np.array, move: PieceMove, turn: TurnManager):
        self.board = board
        self.move = move
        self.turn = turn

    @staticmethod
    def validate_player_input(player_input: str) -> list:
        """Validates player input in algebraic notation"""
        positions = player_input.strip().lower().split()
        # Check if we have either 1 or 2 positions
        if len(positions) not in [1, 2]:
            raise InvalidPlayerInputError("Must be 'e2 e4' for a move or 'e2' for a spectate")
        # Validate each position
        for position in positions:
            if not (len(position) == 2 and
                    'a' <= position[0] <= 'h' and
                    '1' <= position[1] <= '8'):
                raise InvalidPlayerInputError(f"Format for '{position}' position should be like 'e2'")
        return positions

    def __check_board_limitations(self):
        """Validates that move positions are within the board boundaries"""
        for pos in (self.move.from_pos, self.move.to_pos):
            if not (0 <= pos[0] <= 7 and 0 <= pos[1] <= 7):
                raise InvalidBoardLimitationError()
        return True, ""

    def __check_piece_existence(self):
        """Validates that there is a piece at the starting position"""
        if self.board[self.move.from_pos] == " ":
            raise InvalidPieceExistenceError()
        return True, ""

    def __check_player_turn(self):
        """Validates that the correct player is moving their own piece"""
        piece_color = Piece.get_color(self.board, self.move.from_pos)
        if piece_color != self.turn.current_color:
            raise InvalidPlayerTurnError()
        return True, ""

    def __check_piece_rules(self):
        """Validates piece movement and capture rules"""
        piece = get_piece(self.board[self.move.from_pos])
        possible_moves = piece.get_possible_moves(self.board, self.move.from_pos)
        if self.move.to_pos not in possible_moves:
            raise InvalidPieceMoveError(f"Invalid move for the {piece.__class__.__name__}")
        return True, ""

    def validate_move(self) -> tuple[bool, str]:
        """Central validation method that runs all validation checks"""
        try:
            # Run all validation checks
            self.__check_board_limitations()
            self.__check_piece_existence()
            self.__check_player_turn()
            self.__check_piece_rules()

            return True, ""
        except BaseError as error:
            return False, error.get_error_msg()
