def print_board(board):
    i = 0
    while i < 3:
        print(" | ".join(board[i]))
        if i < 2:
            print("_" * 5)
        i += 1


def check_win(board, player):
    # Check rows
    for i in range(3):
        if board[i][0] == board[i][1] == board[i][2] == player:
            return True

    # Check columns
    for j in range(3):
        if board[0][j] == board[1][j] == board[2][j] == player:
            return True

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] == player:
        return True
    if board[0][2] == board[1][1] == board[2][0] == player:
        return True

    return False


def ttt():
    board = [["", "", ""], ["", "", ""], ["", "", ""]]
    players = ['X', 'O']
    moves = 0

    while moves < 9:
        print_board(board)
        current_player = players[moves % 2]
        print("Current player:", current_player)

        row = int(input("Enter row (0,1,2): "))
        col = int(input("Enter col (0,1,2): "))

        if board[row][col] == "":
            board[row][col] = current_player
            moves += 1
        else:
            print("Cell already taken, try again!")
            continue

        if check_win(board, current_player):
            print_board(board)
            print("Player", current_player, "wins!")
            return

    print_board(board)
    print("It's a draw!")


ttt()
