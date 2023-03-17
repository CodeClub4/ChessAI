from models import ChessBoard, PieceMove


def get_input() -> PieceMove:
    pass


def main():
    chess_board = ChessBoard()
    while not chess_board.is_game_over():
        # print the current board
        chess_board.print_board()

        # get user input
        move = get_input()

        # check if the move is valid
        if not chess_board.is_valid_move(move):
            print("Invalid move, please try again")
            continue

        # make the move and update the board
        chess_board.make_move(move)


if __name__ == "__main__":
    # main()
    pass
