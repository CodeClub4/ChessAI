class Piece:

    @staticmethod
    def get_color(board, position):
        """Gets the color of a piece at a given position"""
        piece_char = board[position]
        return "white" if piece_char.islower() else "black"

    def get_possible_moves(self, board, from_pos):
        """Returns all valid moves for this piece from the given position"""

    def is_opponent_piece(self, board, from_pos, to_pos):
        """Checks if the piece at to_pos is an opponent's piece"""
        if board[to_pos] == ' ':
            return False
        return self.get_color(board, from_pos) != self.get_color(board, to_pos)


class Pawn(Piece):

    def get_possible_moves(self, board, from_pos):
        """Returns all possible legal moves for a pawn at the given position"""
        possible_moves = []

        # Get the color of the piece at the starting position
        color = self.get_color(board, from_pos)

        # 1 for white (moves up), -1 for black (moves down)
        direction = 1 if color == "white" else -1

        # Determine the starting row for pawns
        start_pos = 1 if color == "white" else 6

        row, col = from_pos

        # Check one square forward
        to_pos = (row, col + 1 * direction)
        if 0 <= to_pos[1] <= 7:  # Check if still on board
            if board[to_pos] == ' ':  # Check if square is empty
                possible_moves.append(to_pos)

                # Check two squares forward from starting position
                if col == start_pos:
                    double_to_pos = (row, col + 2 * direction)
                    if 0 <= double_to_pos[1] <= 7 and board[double_to_pos] == ' ':
                        possible_moves.append(double_to_pos)

        # Check diagonal captures
        for col_offset in [-1, 1]:
            capture_pos = (row + col_offset, col + 1 * direction)
            if 0 <= capture_pos[0] <= 7 and 0 <= capture_pos[1] <= 7:  # Check if on board
                if board[capture_pos] != ' ':  # Check if square has a piece
                    if self.is_opponent_piece(board, from_pos, capture_pos):
                        possible_moves.append(capture_pos)

        return possible_moves


class Knight(Piece):

    def get_possible_moves(self, board, from_pos):
        """Returns all possible legal moves for a knight at the given position"""
        possible_moves = []

        # Knight gama move patterns
        move_patterns = [
            (-2, -1), (-2, 1), (2, -1), (2, 1),
            (-1, -2), (-1, 2), (1, -2), (1, 2)
        ]

        for dx, dy in move_patterns:
            to_pos = (from_pos[0] + dx, from_pos[1] + dy)

            # Check if position is on the board
            if 0 <= to_pos[0] <= 7 and 0 <= to_pos[1] <= 7:
                # Check if position is empty or contains enemy piece
                if board[to_pos] == ' ' or self.is_opponent_piece(board, from_pos, to_pos):
                    possible_moves.append(to_pos)

        return possible_moves


class Bishop(Piece):

    def get_possible_moves(self, board, from_pos):
        """Returns all possible legal moves for a bishop at the given position"""
        possible_moves = []

        # Bishop diagonal move patterns
        directions = [(-1, -1), (-1, 1), (1, -1), (1, 1)]

        for dx, dy in directions:
            for distance in range(1, 8):
                to_pos = (from_pos[0] + dx * distance, from_pos[1] + dy * distance)

                # Check if position is on the board
                if not (0 <= to_pos[0] <= 7 and 0 <= to_pos[1] <= 7):
                    break  # Off the board

                if board[to_pos] == ' ':
                    # Empty square, valid move
                    possible_moves.append(to_pos)
                elif self.is_opponent_piece(board, from_pos, to_pos):
                    # Enemy piece, can capture and then must stop
                    possible_moves.append(to_pos)
                    break
                else:
                    break

        return possible_moves


class Rook(Piece):

    def get_possible_moves(self, board, from_pos):
        """Returns all possible legal moves for a rook at the given position"""
        possible_moves = []

        # Rook horizontal and vertical move patterns
        directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]  # up, right, down, left

        for dx, dy in directions:
            for distance in range(1, 8):
                to_pos = (from_pos[0] + dx * distance, from_pos[1] + dy * distance)

                # Check if position is on the board
                if not (0 <= to_pos[0] <= 7 and 0 <= to_pos[1] <= 7):
                    break  # Off the board

                if board[to_pos] == ' ':
                    # Empty square, valid move
                    possible_moves.append(to_pos)
                elif self.is_opponent_piece(board, from_pos, to_pos):
                    # Enemy piece, can capture and then must stop
                    possible_moves.append(to_pos)
                    break
                else:
                    break

        return possible_moves


class Queen(Piece):

    def get_possible_moves(self, board, from_pos):
        """Returns all possible legal moves for a queen at the given position"""
        possible_moves = []

        # Queen horizontal, vertical, and diagonal move patterns
        directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0),  # Rook-like moves
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Bishop-like moves
        ]

        for dx, dy in directions:
            for distance in range(1, 8):
                to_pos = (from_pos[0] + dx * distance, from_pos[1] + dy * distance)

                # Check if position is on the board
                if not (0 <= to_pos[0] <= 7 and 0 <= to_pos[1] <= 7):
                    break  # Off the board

                if board[to_pos] == ' ':
                    # Empty square, valid move
                    possible_moves.append(to_pos)
                elif self.is_opponent_piece(board, from_pos, to_pos):
                    # Enemy piece, can capture and then must stop
                    possible_moves.append(to_pos)
                    break
                else:
                    break

        return possible_moves


class King(Piece):

    def get_possible_moves(self, board, from_pos):
        """Returns all possible legal moves for a king at the given position"""
        possible_moves = []

        # King one square move patterns
        directions = [
            (0, 1), (1, 0), (0, -1), (-1, 0),  # Rook-like moves
            (1, 1), (1, -1), (-1, 1), (-1, -1)  # Bishop-like moves
        ]

        for dx, dy in directions:
            to_pos = (from_pos[0] + dx, from_pos[1] + dy)

            # Check if position is on the board
            if 0 <= to_pos[0] <= 7 and 0 <= to_pos[1] <= 7:
                # Check if position is empty or contains enemy piece
                if board[to_pos] == ' ' or self.is_opponent_piece(board, from_pos, to_pos):
                    # Add additional check here for king not moving into check
                    possible_moves.append(to_pos)

        return possible_moves


PIECE_CLASS_MAP = {
    "p": Pawn,
    "n": Knight,
    "b": Bishop,
    "r": Rook,
    "q": Queen,
    "k": King,
}


def get_piece(piece_char: str) -> Piece:
    piece_class = PIECE_CLASS_MAP[piece_char.lower()]
    return piece_class()
