import random


class TicTacToe:
    def __init__(self):

        self.board = [[' ' for x in range(3)] for y in range(3)]
        self.user_input = ''
        self.computer_input = ''
        self.player = ''

    def choose_side(self):
        valid_inputs = ['X', 'O']
        self.user_input = input("Would you like to play as 'X' or 'O'? ").upper()
        self.player = self.user_input
        while self.user_input not in valid_inputs:
            print("Invalid input. Please choose 'X' or 'O'.")
            self.user_input = input("Would you like to play as 'X' or 'O'? ").upper()

        self.computer_input = 'X' if self.user_input == 'O' else 'O'

    def create_board(self):
        horizontal_line = "------------------"
        print(horizontal_line)
        for row in range(3):
            print(" | ", end=" ")
            for col in range(3):
                print(self.board[row][col], end="  |  ")
            print("\n" + horizontal_line)

    def player_move(self):
        if self.user_input == 'X' or self.user_input == 'O':
            print("Player move")
            try:
                row = int(input("Enter row: "))
                col = int(input("Enter column: "))
                if row < 0 or row > 2 or col < 0 or col > 2:
                    print("Invalid input. Row and column must be between 0 and 2.")
                    self.player_move()
                elif self.board[row][col] == ' ':
                    self.board[row][col] = self.user_input
                    self.create_board()
                    if self.check_winner():
                        return
                    self.computer_move()
                else:
                    print("This place is already taken. Try again")
                    self.player_move()
            except ValueError:
                print("Invalid input. Please enter numeric values.")
                self.player_move()
        else:
            print("Wrong input. Try again")
            self.player_move()

    def computer_move(self):
        print("Computer move")
        row = random.randint(0, 2)
        col = random.randint(0, 2)
        if self.board[row][col] == ' ':
            self.board[row][col] = self.computer_input
            self.create_board()
        else:
            self.computer_move()

    def play_game(self):
        self.choose_side()
        self.create_board()
        while not self.check_winner():
            self.player_move()
        return

    def check_winner(self):
        winning_combinations = [
            [(0, 0), (0, 1), (0, 2)],  # Row 1
            [(1, 0), (1, 1), (1, 2)],  # Row 2
            [(2, 0), (2, 1), (2, 2)],  # Row 3
            [(0, 0), (1, 0), (2, 0)],  # Column 1
            [(0, 1), (1, 1), (2, 1)],  # Column 2
            [(0, 2), (1, 2), (2, 2)],  # Column 3
            [(0, 0), (1, 1), (2, 2)],  # Diagonal top-left to bottom-right
            [(0, 2), (1, 1), (2, 0)]  # Diagonal top-right to bottom-left
        ]
        for combination in winning_combinations:
            symbols = [self.board[row][col] for row, col in combination]
            if symbols == ['X', 'X', 'X']:
                if self.player == 'X':
                    print("You won!")
                    return 'X'
                else:
                    print("Computer won!")
                    return 'O'
            elif symbols == ['O', 'O', 'O']:
                if self.player == 'O':
                    print("You won!")
                    return 'O'
                else:
                    print("Computer won!")
                    return 'X'
        return None


new_game = TicTacToe()
new_game.play_game()
