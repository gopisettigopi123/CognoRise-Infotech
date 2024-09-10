# Function to print the Sudoku grid
def print_board(board):
    for row in board:
        print(" ".join(str(num) for num in row))

# Function to check if it's valid to place a number at the given position
def is_valid(board, row, col, num):
    # Check row
    for i in range(9):
        if board[row][i] == num:
            return False

    # Check column
    for i in range(9):
        if board[i][col] == num:
            return False

    # Check 3x3 subgrid
    start_row = (row // 3) * 3
    start_col = (col // 3) * 3
    for i in range(3):
        for j in range(3):
            if board[start_row + i][start_col + j] == num:
                return False

    return True

# Function to solve the Sudoku using backtracking
def solve_sudoku(board):
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:  # Find an empty space (represented by 0)
                for num in range(1, 10):  # Try numbers 1 to 9
                    if is_valid(board, row, col, num):
                        board[row][col] = num  # Place the number

                        # Recursively solve the rest of the board
                        if solve_sudoku(board):
                            return True

                        # If the number doesn't lead to a solution, backtrack
                        board[row][col] = 0

                return False  # Trigger backtracking if no valid number found
    return True  # Board is completely filled and valid

# Example Sudoku board (0 represents empty spaces)
board = [
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
if solve_sudoku(board):
    print("Solved Sudoku:")
    print_board(board)
else:
    print("Solved Sudoku:")
  
