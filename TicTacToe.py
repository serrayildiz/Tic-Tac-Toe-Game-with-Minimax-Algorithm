import copy

board = [' ' for x in range(9)]

def print_board():
    row1 = "| {} | {} | {} |".format(board[0], board[1], board[2])
    row2 = "| {} | {} | {} |".format(board[3], board[4], board[5])
    row3 = "| {} | {} | {} |".format(board[6], board[7], board[8])

    print()
    print(row1)
    print(row2)
    print(row3)
    print()

def player_move(icon):
    if icon == 'X':
        number = 1
    elif icon == 'O':
        number = 2
    print("Your turn player {}".format(number))
    choice = int(input("Enter your move (1-9): ").strip())
    if board[choice - 1] == ' ':
        board[choice - 1] = icon
    else:
        print()
        print("That space is already taken!")

def computer_move(icon):
    print("Computer's turn")
    best_score = None
    for i in range(9):
        if board[i] == ' ':
            board[i] = icon
            score = minimax(board, False)
            board[i] = ' '
            if icon == 'O':
                if best_score is None or score > best_score:
                    best_score = score
                    move = i
            else:
                if best_score is None or score < best_score:
                    best_score = score
                    move = i
    board[move] = icon

def minimax(board, isMaximizing):
    result = check_victory()
    if result != None:
        return result
    if isMaximizing:
        best_score = None
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                score = minimax(board, False)
                board[i] = ' '
                if best_score is None or score > best_score:
                    best_score = score
        return best_score
    else:
        best_score = None
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                score = minimax(board, True)
                board[i] = ' '
                if best_score is None or score < best_score:
                    best_score = score
        return best_score

def check_victory():
    if (board[0] == 'X' and board[1] == 'X' and board[2] == 'X') or \
       (board[3] == 'X' and board[4] == 'X' and board[5] == 'X') or \
       (board[6] == 'X' and board[7] == 'X' and board[8] == 'X') or \
       (board[0] == 'X' and board[3] == 'X' and board[6] == 'X') or \
       (board[1] == 'X' and board[4] == 'X' and board[7] == 'X') or \
       (board[2] == 'X' and board[5] == 'X' and board[8] == 'X') or \
       (board[0] == 'X' and board[4] == 'X' and board[8] == 'X') or \
       (board[2] == 'X' and board[4] == 'X' and board[6] == 'X'):
        return -1
    elif (board[0] == 'O' and board[1] == 'O' and board[2] == 'O') or \
         (board[3] == 'O' and board[4] == 'O' and board[5] == 'O') or \
         (board[6] == 'O' and board[7] == 'O' and board[8] == 'O') or \
         (board[0] == 'O' and board[3] == 'O' and board[6] == 'O') or \
         (board[1] == 'O' and board[4] == 'O' and board[7] == 'O') or \
         (board[2] == 'O' and board[5] == 'O' and board[8] == 'O') or \
         (board[0] == 'O' and board[4] == 'O' and board[8] == 'O') or \
         (board[2] == 'O' and board[4] == 'O' and board[6] == 'O'):
        return 1
    elif ' ' not in board:
        return 0
    else:
        return None


def main():
    print_board()
    while True:
        player_move('X')
        print_board()
        result = check_victory()
        if result != None:
            break
        computer_move('O')
        print_board()
        result = check_victory()
        if result != None:
            break
    if result == -1:
        print("Congratulations, you won the game!")
    elif result == 1:
        print("Sorry, the computer won the game.")
    else:
        print("The game is a draw.")

if __name__ == '__main__':
    main()
