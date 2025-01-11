# Define the size of the grid
N = 9

# Function to print the Sudoku grid
def print_grid(grid):
    for row in grid:
        print(" ".join(str(num) for num in row))

# Function to check if placing a number in a given cell is valid
def is_valid(grid, row, col, num):
    # Check if the number is already in the row
    for i in range(N):
        if grid[row][i] == num:
            return False
    
    # Check if the number is already in the column
    for i in range(N):
        if grid[i][col] == num:
            return False
    
    # Check if the number is already in the 3x3 sub-grid
    start_row, start_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(3):
        for j in range(3):
            if grid[start_row + i][start_col + j] == num:
                return False
    
    return True

# Function to solve the Sudoku puzzle using backtracking
def solve_sudoku(grid):
    # Find the next empty cell (represented by 0)
    for row in range(N):
        for col in range(N):
            if grid[row][col] == 0:
                # Try all numbers from 1 to 9
                for num in range(1, N + 1):
                    if is_valid(grid, row, col, num):
                        grid[row][col] = num
                        
                        # Recursively try to solve the rest of the grid
                        if solve_sudoku(grid):
                            return True
                        
                        # Backtrack if the number didn't work
                        grid[row][col] = 0
                
                return False  # Return False if no valid number was found

    return True  # Return True if the puzzle is solved

# Example Sudoku puzzle (0 represents an empty cell)
sudoku_grid = [
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

# Solve the Sudoku puzzle
if solve_sudoku(sudoku_grid):
    print("Solved Sudoku Puzzle:")
    print_grid(sudoku_grid)
else:
    print("No solution exists.")
