import math

# Define the score values for different game outcomes
X = 1  # Computer wins
O = -1  # Human wins
EMPTY = 0  # No winner yet

# Define the game board as a 3x3 matrix
board = [[EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY],
         [EMPTY, EMPTY, EMPTY]]


def print_board():
    """
    Prints the current state of the game board.
    """
    print("-------------")
    for row in range(3):
        print("|", end=" ")
        for col in range(3):
            if board[row][col] == X:
                print("X", end=" | ")
            elif board[row][col] == O:
                print("O", end=" | ")
            else:
                print(" ", end=" | ")
        print()
        print("-------------")


def get_valid_moves():
    """
    Returns a list of all valid moves on the game board.
    """
    valid_moves = []
    for row in range(3):
        for col in range(3):
            if board[row][col] == EMPTY:
                valid_moves.append((row, col))
    return valid_moves


def get_user_move():
    """
    Asks the user to input a valid move and returns it.
    """
    valid_moves = get_valid_moves()
    while True:
        user_input = input("Enter a move (1-9): ")
        try:
            move = int(user_input) - 1
            row = move // 3
            col = move % 3
            if (row, col) in valid_moves:
                return row, col
            else:
                print("Invalid move! Please try again.")
        except ValueError:
            print("Invalid input! Please enter a number between 1 and 9.")


def get_winner():
    """
    Returns the winner of the game (if any).
    """
    # Check rows for a winner
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != EMPTY:
            return board[row][0]

    # Check columns for a winner
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]

    # Check diagonals for a winner
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]

    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    # If no winner yet, check if the game is a draw
    if len(get_valid_moves()) == 0:
        return 0

    # If the game is still ongoing, return None
    return None


def minimax(is_maximizing):
    """
    Implements the Minimax algorithm to find the best move for the computer.
    """
    # Base case: check if the game is over or the maximum depth is reached
    winner = get_winner()
    if winner is not None:
        return winner

    # Recursive case: use the Minimax algorithm to evaluate each possible move
    if is_maximizing:
        best_score = -math.inf
       
        for move in get_valid_moves():
            row, col = move
            board[row][col] = X
            score = minimax(False)
            board[row][col] = EMPTY
            best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for move in get_valid_moves():
            row, col = move
            board[row][col] = O
            score = minimax(True)
            board[row][col] = EMPTY
            best_score = min(score, best_score)
        return best_score


def get_computer_move():
    """
    Finds the best move for the computer using the Minimax algorithm and returns it.
    """
    best_move = None
    best_score = -math.inf
    for move in get_valid_moves():
        row, col = move
        board[row][col] = X
        score = minimax(False)
        board[row][col] = EMPTY
        if score > best_score:
            best_move = move
            best_score = score
    return best_move


def play_game():
    """
    Runs a game of Tic Tac Toe.
    """
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        # Human player's turn
        row, col = get_user_move()
        board[row][col] = O
        print_board()
        winner = get_winner()
        if winner is not None:
            break

        # Computer player's turn
        print("Computer is thinking...")
        row, col = get_computer_move()
        board[row][col] = X
        print_board()
        winner = get_winner()
        if winner is not None:
            break

    if winner == X:
        print("Computer wins!")
    elif winner == O:
        print("You win!")
    else:
        print("Draw!")


if __name__ == '__main__':
    play_game()
