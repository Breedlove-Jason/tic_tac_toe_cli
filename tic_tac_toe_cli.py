import random

board = [[' ' for x in range(3)] for y in range(3)]

# for i in range(3):
#     for j in range(3):
#         board[i][j] = random.choice(['X', 'O'])
# computer_move = random.choice([0, 1])

def create_board():
    horizontal_line = "------------------"
    print(horizontal_line)
    for row in range(3):
        print(" | ", end=" ")
        for col in range(3):
            print(board[row][col], end="  |  ")
        print("\n" + horizontal_line)


create_board()


def player_move(game_board, user_input):
    if user_input == 'X' or user_input == 'O':
        print("Player move")
        row = int(input("Enter row: "))
        col = int(input("Enter column: "))
        if game_board[row][col] == ' ':
            game_board[row][col] = user_input
            create_board()
            computer_move(game_board, 'O')
        else:
            print("This place is already taken. Try again")
            player_move(game_board, user_input)
    else:
        print("Wrong input. Try again")
        player_move(game_board, user_input)


def computer_move(game_board, computer_input):
    print("Computer move")
    row = random.randint(0, 2)
    col = random.randint(0, 2)
    if game_board[row][col] == ' ':
        game_board[row][col] = computer_input
        create_board()
    else:
        computer_move(game_board, computer_input)


player_move(board, 'X')