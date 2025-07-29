import csv
import time
from functools import wraps
from typing import List, Generator, Optional, Tuple

class Sudoku:
    def __init__(self, grid: Optional[List[List[int]]] = None):
        self.grid = grid if grid else [[0 for _ in range(9)] for _ in range(9)]
        self.solved = False
    
    def load_from_csv(self, filename: str) -> None:
        """File handling: Load Sudoku puzzle from CSV"""
        try:
            with open(filename, 'r') as file:
                reader = csv.reader(file)
                self.grid = []
                for row in reader:
                    if len(row) != 9:
                        raise ValueError("Each row must have exactly 9 elements")
                    self.grid.append([int(cell) if cell != '' else 0 for cell in row])
            
            if len(self.grid) != 9:
                raise ValueError("Sudoku grid must have exactly 9 rows")
            
            print(f"Loaded Sudoku puzzle from {filename}")
        except FileNotFoundError:
            raise FileNotFoundError(f"File {filename} not found")
        except ValueError as e:
            raise ValueError(f"Invalid Sudoku grid in CSV: {str(e)}")
    
    def is_valid(self) -> bool:
        """Check if the current grid is valid"""
        
        for row in self.grid:
            nums = [n for n in row if n != 0]
            if len(nums) != len(set(nums)):
                return False

        for col in range(9):
            nums = [self.grid[row][col] for row in range(9) if self.grid[row][col] != 0]
            if len(nums) != len(set(nums)):
                return False

        for box_row in range(0, 9, 3):
            for box_col in range(0, 9, 3):
                nums = []
                for row in range(box_row, box_row + 3):
                    for col in range(box_col, box_col + 3):
                        if self.grid[row][col] != 0:
                            nums.append(self.grid[row][col])
                if len(nums) != len(set(nums)):
                    return False
        
        return True
    
    def find_empty_cell(self) -> Optional[Tuple[int, int]]:
        """Find the next empty cell (0 represents empty)"""
        for row in range(9):
            for col in range(9):
                if self.grid[row][col] == 0:
                    return (row, col)
        return None
    
    def possible_numbers(self, row: int, col: int) -> Generator[int, None, None]:
        """Generator: Yield possible numbers for a cell"""
        used_numbers = set()

        used_numbers.update(self.grid[row])

        used_numbers.update(self.grid[r][col] for r in range(9))

        box_row, box_col = (row // 3) * 3, (col // 3) * 3
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                used_numbers.add(self.grid[r][c])

        for num in range(1, 10):
            if num not in used_numbers:
                yield num
    
    def is_valid_move(self, row: int, col: int, num: int) -> bool:
        """Check if a number can be placed in a cell"""
        
        if num in self.grid[row]:
            return False

        if num in [self.grid[r][col] for r in range(9)]:
            return False

        box_row, box_col = (row // 3) * 3, (col // 3) * 3
        for r in range(box_row, box_row + 3):
            for c in range(box_col, box_col + 3):
                if self.grid[r][c] == num:
                    return False
        
        return True
    
    @timeit
    def solve(self) -> bool:
        """Solve the Sudoku using backtracking"""
        empty_cell = self.find_empty_cell()

        if not empty_cell:
            self.solved = True
            return True
        
        row, col = empty_cell
        
        for num in self.possible_numbers(row, col):
            if self.is_valid_move(row, col, num):
                self.grid[row][col] = num
                
                if self.solve():
                    return True

                self.grid[row][col] = 0
        
        return False
    
    def display(self) -> None:
        """Display the Sudoku grid"""
        print("\nSudoku Grid:")
        for i, row in enumerate(self.grid):
            if i % 3 == 0 and i != 0:
                print("-" * 21)
            
            row_str = []
            for j, num in enumerate(row):
                if j % 3 == 0 and j != 0:
                    row_str.append("|")
                row_str.append(str(num) if num != 0 else ".")
            
            print(" ".join(row_str))
        print()

def timeit(func):
    """Decorator: Measure function execution time"""
    @wraps(func)
    def wrapper(self, *args, **kwargs):
        start_time = time.time()
        result = func(self, *args, **kwargs)
        end_time = time.time()
        print(f"Solved in {end_time - start_time:.4f} seconds")
        return result
    return wrapper

def main():
    print("Sudoku Solver")

    sample_grid = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]
    
    sudoku = Sudoku(sample_grid)
    
    while True:
        print("\nMenu:")
        print("1. Load puzzle from CSV")
        print("2. Solve current puzzle")
        print("3. Display current puzzle")
        print("4. Exit")
        
        choice = input("Enter your choice: ")
        
        if choice == "1":
            filename = input("Enter CSV filename: ")
            try:
                sudoku = Sudoku()
                sudoku.load_from_csv(filename)
                sudoku.display()
            except Exception as e:
                print(f"Error: {str(e)}")
        
        elif choice == "2":
            if not sudoku.is_valid():
                print("Invalid Sudoku puzzle - duplicate numbers detected")
                continue
            
            print("Solving...")
            if sudoku.solve():
                print("Solution found!")
                sudoku.display()
            else:
                print("No solution exists for this puzzle")
        
        elif choice == "3":
            sudoku.display()
        
        elif choice == "4":
            print("Goodbye!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()