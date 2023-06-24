import random


class TicTacToe:
    def __init__(self):

        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.user_input = ''
        self.computer_input = ''
        self.player = ''

    def choose_side(self):
        """Prompt the user to choose their side ('X' or 'O') and set the player and computer inputs accordingly."""
        valid_inputs = ['X', 'O']
        self.user_input = input("Would you like to play as 'X' or 'O'? ").upper()
        self.player = self.user_input
        while self.user_input not in valid_inputs:
            print("Invalid input. Please choose 'X' or 'O'.")
            self.user_input = input("Would you like to play as 'X' or 'O'? ").upper()

        self.computer_input = 'X' if self.user_input == 'O' else 'O'

    def create_board(self):
        """Print the current state of the Tic-Tac-Toe board."""
        horizontal_line = "---------------------"
        print(horizontal_line)
        for row in range(3):
            print(" | ", end=" ")
            for col in range(3):
                print(self.board[row][col], end="  |  ")
            print("\n" + horizontal_line)

    def player_move(self):
        """Handle the player's move by accepting their input and updating the board."""
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
                    return self.check_winner()
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
        """Make a random move for the computer by selecting an empty cell on the board."""
        print("Computer move")
        available_moves = []
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    available_moves.append((row, col))
        if available_moves:
            row, col = random.choice(available_moves)
            self.board[row][col] = self.computer_input
            self.create_board()
        else:
            self.check_winner()

    def play_game(self):
        """Start and control the flow of the Tic-Tac-Toe game."""
        self.choose_side()
        self.create_board()
        while True:
            result = self.player_move()
            if result:
                break
            self.computer_move()

    def check_winner(self):
        """Check if there is a winning combination on the board and return the result."""
        win_conditions = [
            [(0, 0), (0, 1), (0, 2)],  # Row 1
            [(1, 0), (1, 1), (1, 2)],  # Row 2
            [(2, 0), (2, 1), (2, 2)],  # Row 3
            [(0, 0), (1, 0), (2, 0)],  # Column 1
            [(0, 1), (1, 1), (2, 1)],  # Column 2
            [(0, 2), (1, 2), (2, 2)],  # Column 3
            [(0, 0), (1, 1), (2, 2)],  # Diagonal top-left to bottom-right
            [(0, 2), (1, 1), (2, 0)]  # Diagonal top-right to bottom-left
        ]
        for player in ['X', 'O']:
            if any(all(self.board[row][col] == player for row, col in combination) for combination in win_conditions):
                if self.player == player:
                    print("You won!")
                    return player
                else:
                    print("Computer won!")
                    return self.computer_input
        if all(self.board[row][col] != ' ' for row in range(3) for col in range(3)):
            print("No more moves left. It's a draw!")
            return 'T'
        return None


new_game = TicTacToe()
new_game.play_game()
