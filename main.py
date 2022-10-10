import math

board = [[" " for x in range(3)] for y in range(3)]
player = "x"
ai = "o"
scores = {player: -1, ai: 1}


def free_fields(board):
    for y in range(3):
        if " " in board[y]:
            return True


def field_available(board, x, y):
    return board[y][x] == " "


def check_winner(board):
    for i in range(3):
        if board[0][i] == board[1][i] == board[2][i] != " ":
            return scores[board[0][i]]
        if board[i][0] == board[i][1] == board[i][2] != " ":
            return scores[board[i][0]]
    if board[0][0] == board[1][1] == board[2][2] != " ":
        return scores[board[0][0]]
    if board[0][2] == board[1][1] == board[2][0] != " ":
        return scores[board[0][2]]
    if not free_fields(board):
        return 0  # tie
    return None  # game not over


def minimax(board, ismaximizing):
    winner = check_winner(board)
    if winner is not None:
        return winner

    if ismaximizing:
        value = -math.inf
        for y in range(3):
            for x in range(3):
                if field_available(board, x, y):
                    board[y][x] = ai
                    value = max(value, minimax(board, False))
                    board[y][x] = " "
        return value

    if not ismaximizing:
        value = math.inf
        for y in range(3):
            for x in range(3):
                if field_available(board, x, y):
                    board[y][x] = player
                    value = min(value, minimax(board, True))
                    board[y][x] = " "
        return value


def best_move(board):
    move = (-1, -1)
    value = -math.inf
    for y in range(3):
        for x in range(3):
            if field_available(board, x, y):
                board[y][x] = ai
                nvalue = minimax(board, False)
                board[y][x] = " "
                if nvalue > value:
                    value = nvalue
                    move = y, x
    return move


while check_winner(board) is None and free_fields(board):
    for row in board:
        print(row)
    print("\n")

    player_x = input("x: ")
    player_y = input("y: ")
    board[int(player_y)][int(player_x)] = player

    y, x = best_move(board)
    board[y][x] = ai

print("Tie" if check_winner(board) is None else check_winner(board))
