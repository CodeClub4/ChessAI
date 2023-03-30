from models import ChessBoard, PieceMove


def get_input() -> PieceMove:
    move_split = tuple(input("make your move: ").split())

    start_pos, end_pos = (move_split[0], move_split[1])

    start_pos_conv = PieceMove.position_converter(start_pos)
    end_pos_conv = PieceMove.position_converter(end_pos)

    piece_move = PieceMove(start_pos_conv, end_pos_conv)

    return piece_move


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
