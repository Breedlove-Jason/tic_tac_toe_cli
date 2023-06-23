import random

board = [[' ' for x in range(3)] for y in range(3)]

for i in range(3):
    for j in range(3):
        board[i][j] = random.choice(['X', 'O'])


def create_board(game_board):
    horizontal_line = "------------------"
    print(horizontal_line)
    for row in range(3):
        print(" | ", end=" ")
        for col in range(3):
            print(board[row][col], end="  |  ")
        print("\n" + horizontal_line)


create_board(board)
