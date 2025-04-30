import numpy as np
from app.errors import *
from app.declarations import COLUMN_NAMES, ROW_NAMES, START_BOARD
from app.models2.common import TurnManager, PieceMove, GameResignedException
from app.models2.validations import Validator
from app.models2.pieces import get_piece


class ChessPlayer:

    def __init__(self, name: str, color: str):
        self.name = name
        self.color = color

    def __str__(self):
        return f"{self.name} ({self.color})"

    def get_player_input(self) -> PieceMove:
        """Ask the player for input, handle resign, and validate input."""
        while True:
            player_input = input(f"choose action (move: 'e2 e4', spectate: 'e2', resign: 'r'): ").strip()
            if player_input.lower() == "r":
                raise GameResignedException(self.name, self.color)
            try:
                positions = Validator.validate_player_input(player_input)
                return PieceMove(positions)
            except InvalidPlayerInputError as e:
                print(e.get_error_msg())


class ChessEngine:

    @staticmethod
    def get_piece_possible_moves(board: np.array, position: tuple):
        """Returns all possible moves for a piece at the given position"""
        piece_char = board[position]
        if piece_char == ' ':
            print(f"No piece at {position}")
            return []

        piece = get_piece(piece_char)
        possible_moves = piece.get_possible_moves(board, position)

        # Print possible moves
        if possible_moves:
            print(f"Possible moves for {piece.__class__.__name__} at {position}:")
            for move in possible_moves:
                print(f"{move}")
        else:
            print(f"No valid moves for piece at {position}")

        return possible_moves

    @staticmethod
    def is_check() -> bool:
        return False

    @staticmethod
    def is_checkmate() -> bool:
        return False


class ChessBoard:
    board: np.array
    COLOR_LABEL = "\033[33m"
    RESET = "\033[0m"

    def __init__(self):
        self.board = np.copy(START_BOARD)

    def print_board(self):
        """Print the board and add colored letters and numbers"""
        flipped_board = np.flipud((np.rot90(np.fliplr(self.board))))
        board_col_names_added = np.r_[flipped_board, [COLUMN_NAMES]]
        board = np.c_[ROW_NAMES, board_col_names_added]

        for i, row in enumerate(board):
            for j, square in enumerate(row):
                if j == 0 or i == len(board) - 1:
                    print(f"{self.COLOR_LABEL}{square}{self.RESET}", end=" ")
                else:
                    # print(cell, end=" ")
                    print(square if square != " " else "·", end=" ")
            print()

    def make_move(self, move: PieceMove):
        """Make a move on the board and report captures"""
        # Get the from piece name/color
        from_piece = get_piece(self.board[move.from_pos])
        from_piece_name = from_piece.__class__.__name__.lower()
        from_piece_color = from_piece.get_color(self.board, move.from_pos)

        # Check if this is a capture
        if self.board[move.to_pos] != " ":
            # Get the to piece name/color
            to_piece = get_piece(self.board[move.to_pos])
            to_piece_name = to_piece.__class__.__name__.lower()
            to_piece_color = from_piece.get_color(self.board, move.to_pos)
            print(f"{from_piece_color} {from_piece_name} captured {to_piece_color} {to_piece_name}!")
        else:
            print(f"{from_piece_color} {from_piece_name} moved from {move.from_pos} to {move.to_pos}!")

        # Update the board
        self.board[move.to_pos] = self.board[move.from_pos]
        self.board[move.from_pos] = " "


class ChessGame:
    chess_engine: ChessEngine
    chess_board: ChessBoard
    turn: TurnManager

    def start(self):
        """Setup players and start the game loop"""
        self.chess_engine = ChessEngine()
        self.chess_board = ChessBoard()

        # Setup players
        white_name = input(f"Enter Player name for White: ")
        black_name = input(f"Enter Player name for Black: ")
        white_player = ChessPlayer(white_name, "white")
        black_player = ChessPlayer(black_name, "black")

        self.turn = TurnManager(white_player, black_player)

        while not self.chess_engine.is_checkmate():

            current_player = self.turn.get_current_player()
            current_color = current_player.color

            # print the current board
            self.chess_board.print_board()

            # Show prompt for move
            print(f"{current_color}'s turn '{current_player.name}'")

            # get player input
            try:
                player_move = current_player.get_player_input()
            except GameResignedException as e:
                print(f"{e}")
                break

            # Check that player input is a spectate request
            if player_move.is_spectate_move():
                self.chess_engine.get_piece_possible_moves(self.chess_board.board, player_move.from_pos)
                continue

            # Check that player input is a valid move
            validation = Validator(self.chess_board.board, player_move, self.turn)
            is_valid, error_msg = validation.validate_move()
            if not is_valid:
                print(error_msg)
                continue

            # Make the move and update the board
            self.chess_board.make_move(player_move)

            # Change player turn
            self.turn.change_turn()
