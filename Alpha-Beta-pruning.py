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


def get_winner(board):
    """
    Checks if there is a winner in the current game board state and returns the winner.
    Returns EMPTY if there is no winner yet.
    """
    # Check rows
    for row in range(3):
        if board[row][0] == board[row][1] == board[row][2] and board[row][0] != EMPTY:
            return board[row][0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] and board[0][col] != EMPTY:
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] and board[0][0] != EMPTY:
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] and board[0][2] != EMPTY:
        return board[0][2]

    return EMPTY


def evaluate(board):
    """
    Evaluates the current state of the game board and returns the score.
    """
    winner = get_winner(board)
    if winner == X:
        return 1
    elif winner == O:
        return -1
    else:
        return 0

def alphabetapruning(board, depth, is_maximizing_player, alpha, beta):
    """
    Implements the minimax algorithm with alpha-beta pruning to find the best move for the computer.
    """
    winner = get_winner(board)
    if winner != EMPTY or depth == 0:
        return evaluate(board)

    if is_maximizing_player:
        best_score = -math.inf
        for row, col in get_valid_moves():
            board[row][col] = X
            score = alphabetapruning(board, depth - 1, False, alpha, beta)
            board[row][col] = EMPTY
            best_score = max(best_score, score)
            alpha = max(alpha, score)
            if alpha >= beta:
                break
        return best_score
    else:
        best_score = math.inf
        for row, col in get_valid_moves():
            board[row][col] = O
            score = alphabetapruning(board, depth - 1, True, alpha, beta)
            board[row][col] = EMPTY
            best_score = min(best_score, score)
            beta = min(beta, score)
            if alpha >= beta:
                break
        return best_score

def get_computer_move():
    """
    Calculates the best move for the computer using the alpha-beta pruning algorithm.
    """
    best_score = -math.inf
    valid_moves = get_valid_moves()
    best_move = valid_moves[0]

    for move in valid_moves:
        board[move[0]][move[1]] = X
        score = alphabetapruning(board, 0, False, -math.inf, math.inf)
        board[move[0]][move[1]] = EMPTY

        if score > best_score:
            best_score = score
            best_move = move

    return best_move



def play_game():
    """
    Runs the main game loop.
    """
    print("Welcome to Tic Tac Toe!")
    print_board()

    while True:
        # Get the user's move
        row, col = get_user_move()
        board[row][col] = O
        print_board()

        # Check if the game is over
        winner = get_winner(board)
        if winner != EMPTY:
            print("Game over! Winner: ", end="")
            if winner == X:
                print("Computer")
            else:
                print("Human")
            break
        elif not get_valid_moves():
            print("Game over! It's a draw!")
            break

        # Get the computer's move
        print("Computer's turn...")
        row, col = get_computer_move()
        board[row][col] = X
        print_board()

        # Check if the game is over
        winner = get_winner(board)
        if winner != EMPTY:
            print("Game over! Winner: ", end="")
            if winner == X:
                print("Computer")
            else:
                print("Human")
            break
        elif not get_valid_moves():
            print("Game over! It's a draw!")
            break

if __name__ == '__main__':
    play_game()


