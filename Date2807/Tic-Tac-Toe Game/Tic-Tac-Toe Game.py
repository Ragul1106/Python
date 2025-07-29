import random
from functools import wraps
from typing import List, Tuple, Generator

class TicTacToe:
    def __init__(self):
        self.board = [[' ' for _ in range(3)] for _ in range(3)]
        self.current_player = 'X' 
        self.game_over = False
        self.winner = None
    
    def display_board(self) -> None:
        """Display the current game board"""
        print("\nCurrent Board:")
        for i, row in enumerate(self.board):
            print(f" {row[0]} | {row[1]} | {row[2]} ")
            if i < 2:
                print("-----------")
        print()
    
    def get_empty_cells(self) -> Generator[Tuple[int, int], None, None]:
        """Generator: Yield coordinates of empty cells"""
        for row in range(3):
            for col in range(3):
                if self.board[row][col] == ' ':
                    yield (row, col)
    
    def is_board_full(self) -> bool:
        """Check if the board is full (draw)"""
        return all(cell != ' ' for row in self.board for cell in row)
    
    def check_winner(self, player: str) -> bool:
        """Check if the specified player has won"""

        for row in self.board:
            if all(cell == player for cell in row):
                return True

        for col in range(3):
            if all(self.board[row][col] == player for row in range(3)):
                return True

        if all(self.board[i][i] == player for i in range(3)):
            return True
        if all(self.board[i][2-i] == player for i in range(3)):
            return True
        
        return False
    
    @validate_move
    def make_move(self, row: int, col: int) -> None:
        """Make a move on the board"""
        self.board[row][col] = self.current_player

        if self.check_winner(self.current_player):
            self.game_over = True
            self.winner = self.current_player
            return

        if self.is_board_full():
            self.game_over = True
            return

        self.current_player = 'O' if self.current_player == 'X' else 'X'
    
    def computer_move(self) -> None:
        """Computer makes a random move from available cells"""
        empty_cells = list(self.get_empty_cells())
        if empty_cells:
            row, col = random.choice(empty_cells)
            print(f"\nComputer plays at position ({row+1}, {col+1})")
            self.make_move(row, col)

def validate_move(func):
    """Decorator: Validate move position before executing"""
    @wraps(func)
    def wrapper(self, row: int, col: int, *args, **kwargs):

        if self.game_over:
            raise ValueError("Game is already over")

        if row not in [0, 1, 2] or col not in [0, 1, 2]:
            raise ValueError("Position must be between (1,1) and (3,3)")

        if self.board[row][col] != ' ':
            raise ValueError("That position is already taken")
        
        return func(self, row, col, *args, **kwargs)
    return wrapper

def main():
    print("Welcome to Tic-Tac-Toe!")
    print("You are X, and the computer is O")
    print("Enter moves as row and column numbers (1-3)")
    
    game = TicTacToe()
    game.display_board()
    
    while not game.game_over:
        if game.current_player == 'X':  
            while True:
                try:
                    move = input("Your move (row, column): ")
                    row, col = map(int, move.split(','))
                    row -= 1  
                    col -= 1
                    
                    game.make_move(row, col)
                    break
                except ValueError as e:
                    print(f"Invalid move: {e}. Please try again.")
        else:  
            game.computer_move()
        
        game.display_board()

    if game.winner == 'X':
        print("Congratulations! You won!")
    elif game.winner == 'O':
        print("Computer wins! Better luck next time.")
    else:
        print("It's a draw!")

if __name__ == "__main__":
    main()