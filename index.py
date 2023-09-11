import random
 
class BattleshipGame:
    def __init__(self):
        # Initialize game attributes and variables
        self.player_name = ""
        self.player_board = []
        self.cpu_board = []
        self.board_size = 10
        self.ship_size = 3
        self.quit_game = False
 
    def start_game(self):
        """
        Start the battleship game.
        """
        # Get player name, initialize boards, place ships, and start the game
        self.player_name = input("Enter your name: ")
        self.initialize_boards()
        self.place_ships()
        self.play()
 
    def initialize_boards(self):
        """
        Initialize the player and CPU boards.
        """
        # Create empty player and CPU boards filled with spaces
        self.player_board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
        self.cpu_board = [[' ' for _ in range(self.board_size)] for _ in range(self.board_size)]
 
    def place_ships(self):
        """
        Place ships randomly on the player and CPU boards.
        """
        # Place ships on both player and CPU boards
        self.place_ship(self.player_board)
        self.place_ship(self.cpu_board)
 
    def place_ship(self, board):
        """
        Place a ship randomly on the given board.
 
        Args:
        - board (list): The board to place the ship on.
        """
        # Place ships randomly on the board
        for _ in range(self.ship_size):
            while True:
                x = random.randint(0, self.board_size - 1)
                y = random.randint(0, self.board_size - 1)
                if board[x][y] == ' ':
                  board[x][y] = 'S' # 'S' represents a ship
                  break
 
    def play(self):
        """
        Play the battleship game.
        """
        # Main game loop
        while not self.quit_game:
            self.print_boards() # Display player and CPU boards
            self.player_turn()  # Player's turn
            if self.check_game_over():
                break
            self.cpu_turn()     # CPU's turn
            if self.check_game_over():
                break
 
    def print_boards(self):
        """
        Print the player and CPU boards.
        """
        # Display player's name, player board, and CPU board
        print(f"\nPlayer: {self.player_name}")
        print("Player Board:")
        self.print_board(self.player_board)
        print("\nCPU Board:")
        self.print_board(self.cpu_board, hide_ships=True)
 
    def print_board(self, board, hide_ships=False):
        """
        Print the given board with ships, hits and misses visually represented.
 
        Args:
        - board (list): The board to print.
        - hide_ships (bool): Whether to hide the ships on the board or not.
        """
        # Display the board with coordinates and visual representations
        print("  0 1 2 3 4 5 6 7 8 9")
        print("  -------------------")
        for i, row in enumerate(board):
            print(f"{i}|{'|'.join(['S' if cell == 'S' and not hide_ships else 'X' if cell == 'X' else 'O' if cell == '*' else ' ' for cell in row])}|")
 
    def player_turn(self):
        """
        Perform the player's turn.
        """
        # Get player's coordinates for an attack
        while True:
            try:
                x = int(input("Enter the x-coordinate (0-9) to attack: "))
                y = int(input("Enter the y-coordinate (0-9) to attack: "))
                if not self.is_valid_coordinate(x) or not self.is_valid_coordinate(y):
                    raise ValueError("Invalid coordinate")
                break
            except ValueError as e:
                print(e)
        
        # Check if the attack hits or misses and update the boards accordingly
        if self.cpu_board[x][y] == 'S':
            print("You Hit!")
            self.cpu_board[x][y] = 'X' # 'X' represents a hit
        else:
            print("You Missed!")
            self.cpu_board[x][y] = '*' # '*' represents a miss but it will show as O 
 
        # Display updated boards after the player's turn
        print("Player Board after player's turn:")
        self.print_board(self.player_board)
        print("CPU Board after player's turn:")
        self.print_board(self.cpu_board, hide_ships=True)
 
    def cpu_turn(self):
        """
        Perform the CPU's turn.
        """
        # Generate random coordinates for CPU's attack
        x = random.randint(0, self.board_size - 1)
        y = random.randint(0, self.board_size - 1)
        # Check if the CPU's attack hits or misses and update the boards accordingly
        if self.player_board[x][y] == 'S':
            print("CPU Hit!")
            self.player_board[x][y] = 'X'
        elif self.player_board[x][y] == ' ':
            print("CPU Miss!")
            self.player_board[x][y] = '*'
 
        # Display updated boards after the CPU's turn
        print("Player Board after CPU's turn:")
        self.print_board(self.player_board)
        print("CPU Board after CPU's turn:")
        self.print_board(self.cpu_board, hide_ships=True)
 
    def is_valid_coordinate(self, coordinate):
        """
        Check if the given coordinate is valid.
 
        Args:
        - coordinate (int): The coordinate to check.
 
        Returns:
        - bool: True if the coordinate is valid, False otherwise.
        """
        return 0 <= coordinate < self.board_size
 
    def check_game_over(self):
        """
        Check if the game is over.
 
        Returns:
        - bool: True if the game is over, False otherwise.
        """
        # Check if either player or CPU has no remaining ships
        if self.check_board_empty(self.player_board):
            print("You lost! CPU wins!")
            return True
        elif self.check_board_empty(self.cpu_board):
            print(f"Congratulations {self.player_name}! You won!")
            return True
        return False
 
    def check_board_empty(self, board):
        """
        Check if the given board is empty.
 
        Args:
        - board (list): The board to check.
 
        Returns:
        - bool: True if the board is empty, False otherwise.
        """
        # Check if any 'S' (ship) is left on the board
        for row in board:
            if 'S' in row:
                return False
        return True
 
    def quit(self):
        """
        Quit the game.
        """
        self.quit_game = True
 
if __name__ == "__main__":
    game = BattleshipGame()
    game.start_game()