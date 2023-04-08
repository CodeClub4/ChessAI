from models import ChessBoard, PieceMove


def get_input() -> PieceMove:
    input_move_split = input("make your move: ").split()
    piece_move = PieceMove(input_move_split)
    return piece_move


def main():
    chess_board = ChessBoard()
    white_turn = True
    while not chess_board.is_game_over():
        # print the current board
        chess_board.print_board()

        # get user input
        move = get_input()

        # check if the move is valid
        if not chess_board.is_valid_move(move):
            print("Invalid move, please try again")
            continue

        if chess_board.is_white_piece(move) is white_turn:
            # make the move and update the board
            chess_board.make_move(move)
            # change player turn
            white_turn = not white_turn
        else:
            print("Invalid move, It is your opponent's turn")


if __name__ == "__main__":
    main()
