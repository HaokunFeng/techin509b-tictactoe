# This file contains the Command Line Interface (CLI) for
# the Tic-Tac-Toe game. This is where input and output happens.
# For core game logic, see logic.py.

from logic import make_empty_board, get_winner, other_player

def print_board(board):
    for row in board:
        print(" | ".join(cell if cell is not None else " " for cell in row))
        print("-" * 9)

# Reminder to check all the tests

if __name__ == '__main__':
    board = make_empty_board()
    winner = None
    current_player = 'X'
    while winner == None:
        print(f"Player {current_player}'s turn")

        # TODO: Show the board to the user.
        print_board(board)

        # TODO: Input a move from the player.
        row, col = map(int, input("Enter row and column (e.g., 1 2): ").split())
        if row < 1 or row > 3 or col < 1 or col > 3 or board[row - 1][col - 1] is not None:
            print("Invalid input. Try again.")
            continue

        # TODO: Update the board.
        board[row - 1][col - 1] = current_player

        # Check for a winner using get_winner from logic.py
        winner = get_winner(board)
        if winner == 'Draw':
            print_board(board)
            print("It's a draw!")
            break
        elif winner:
            print_board(board)
            print(f"Player {winner} wins!")
            break

        # TODO: Update who's turn it is.
        current_player = other_player(current_player)
    
    print_board(board)
