from models import ChessBoard, PieceMove


def get_input(white_turn: bool) -> PieceMove:
    color_turn = "white" if white_turn else "black"
    input_move_split = input(f"({color_turn}'s turn) make your move: ").split()
    piece_move = PieceMove(input_move_split)
    return piece_move


def main():
    chess_board = ChessBoard()
    white_turn = True
    while not chess_board.is_game_over():
        # print the current board
        chess_board.print_board()

        # get user input
        move = get_input(white_turn)

        # check if the move is valid
        if not chess_board.is_right_turn(move, white_turn):
            print("Wrong turn, please try again")
            continue

        # make the move and update the board
        chess_board.make_move(move)

        # change player turn
        white_turn = not white_turn


if __name__ == "__main__":
    main()
