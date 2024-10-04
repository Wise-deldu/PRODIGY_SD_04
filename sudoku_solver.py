class SudokuError(Exception):
    """Base class for Sudoku-related exceptions."""
    pass


class InvalidBoardError(SudokuError):
    """Exception raised for invalid Sudoku board."""
    pass


class UnsolvablePuzzleError(SudokuError):
    """Exception raised when the Sudoku puzzle is unsolvable."""
    pass


def validate_board(board):
    """
    Validate the Sudoku board.

    Args:
        board (list of lists): The Sudoku board.

    Raises:
        InvalidBoardError: If the board is not valid.
    """
    if len(board) != 9 or any(len(row) != 9 for row in board):
        raise InvalidBoardError("Board must be 9x9")
    if any(not all(0 <= num <= 9 for num in row) for row in board):
        raise InvalidBoardError("Board must contain numbers 0-9 only")


def is_valid(board, row, col, num):
    """
    Check if it's valid to place a number in a given position
    on the Sudoku board.

    Args:
        board (list of lists): The Sodoku board.
        row (int): The row index.
        col (int): The column index.
        num (int): The number to be placed.

    Returns:
        bool: True if the number can be placed
        at the given position, False otherwise.
    """
    for i in range(9):
        if board[row][i] == num or board[i][col] == num:
            return False
    subgrid_row, subgrid_col = 3 * (row // 3), 3 * (col // 3)
    for i in range(subgrid_row, subgrid_row + 3):
        for j in range(subgrid_col, subgrid_col + 3):
            if board[i][j] == num:
                return False
    return True


def solve_sudoku(board):
    """
    Solve the Sudoku puzzle using a backtracking algorithm.

    Args:
        baord (list of lists): The Sudoku board to be solved.

    Returns:
        bool: True if a solution is found, False otherwise.

    Raises:
        UnsolvablePuzzleError: If the puzzle is unsolvable.
    """
    for row in range(9):
        for col in range(9):
            if board[row][col] == 0:
                for num in range(1, 10):
                    if is_valid(board, row, col, num):

                        board[row][col] = num
                        if solve_sudoku(board):
                            return True
                        board[row][col] = 0
                return False
    return True


def print_sudoku(board):
    """
    Print the Sudoku board in a formatted manner.

    Args:
        board (list of lists): The Sudoku board to be printed.
    """
    for row in board:
        print(" ".join(map(str, row)))


def main():
    """
    Main function to run the Sudoku solver.

    This function handles user input, solves the Sudoku puzzle,
    and displays the result.
    """
    print("Welcome to Sudoku Solver!")
    print("=" * 30)
    print(
        "Please enter the Sudoku puzzle, row by row, using 0 for empty cells."
    )

    sudoku_board = []
    try:
        for _ in range(9):
            row = list(map(int, input().split()))
            sudoku_board.append(row)

        validate_board(sudoku_board)

        print("\nSolving...\n")

        solve_sudoku(sudoku_board)
        print("Sudoku Solved:")
        print_sudoku(sudoku_board)

    except ValueError:
        print("Invalid input. Please enter numbers only.")
    except InvalidBoardError as e:
        print(f"Invalid Sudoku board: {e}")
    except UnsolvablePuzzleError as e:
        print(f"Error: {e}")
    except Exception as e:
        print(f"An expected error occured: {e}")


if __name__ == "__main__":
    main()
