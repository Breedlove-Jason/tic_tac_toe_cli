import random


class TicTacToe:
    def __init__(self):

        self.board = [[' ' for x in range(3)] for y in range(3)]
        self.user_input = 'X'
        self.computer_input = 'O'

    def create_board(self):
        horizontal_line = "------------------"
        print(horizontal_line)
        for row in range(3):
            print(" | ", end=" ")
            for col in range(3):
                print(self.board[row][col], end="  |  ")
            print("\n" + horizontal_line)

    create_board()

    def player_move(self, game_board, user_input):
        if user_input == 'X' or user_input == 'O':
            print("Player move")
            row = int(input("Enter row: "))
            col = int(input("Enter column: "))
            if game_board[row][col] == ' ':
                game_board[row][col] = user_input
                self.create_board()
                self.computer_move(game_board, 'O')
            else:
                print("This place is already taken. Try again")
                self.player_move(game_board, user_input)
        else:
            print("Wrong input. Try again")
            self.player_move(game_board, user_input)

    def computer_move(self, game_board, computer_input):
        print("Computer move")
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if game_board[row][col] == ' ':
            game_board[row][col] = computer_input
            self.create_board()
        else:
            self.computer_move(game_board, computer_input)

    # game_loop = True
    # while game_loop:


new_game = TicTacToe()
new_game.player_move(new_game.board, 'X')
