# Sudoku Solver
## Description
This is a Python program that solves a standard 9x9 Sudoku puzzle using a backtracking algorithm. 

It also includes a board validation function to ensure that the input follows the correct format. 

The project is tested using `pytest` to ensure correct functionality and code quality. ``pycodestyle` is used to enforce PEP 8 style guidelines.

## Features
* Validate Sudoku boards for correctness.
* Solve a Sudoku puzzle using backtracking.
* Handle invalid Sudoku puzzles by raising specific exceptions.
* Include unit tests using pytest.
* Enforce PEP 8 coding style with pycodestyle.

## Getting Started
### Prerequisites
* Python 3.x installed on your machine.
* The following Python packages:
    * `pytest` for testing
    * `pycodestyle` for code style checks

### Installing Dependencies
Install the necessary dependencies using `pip`:

```
pip install pytest pycodestyle
```

## Usage
### Running the Program
1. Clone the repository:

```
git clone https://github.com/Wise-deldu/PRODIGY_SD_04.git
cd sudoku-solver
```

2. Run the solver:

```
python3 sudoku_solver.py
```

3. Input the Sudoku puzzle:

The program will prompt you to input the Sudoku puzzle row by row, using `0` for empty cells. Example input:

```
5 3 0 0 7 0 0 0 0
6 0 0 1 9 5 0 0 0
0 9 8 0 0 0 0 6 0
8 0 0 0 6 0 0 0 3
4 0 0 8 0 3 0 0 1
7 0 0 0 2 0 0 0 6
0 6 0 0 0 0 2 8 0
0 0 0 4 1 9 0 0 5
0 0 0 0 8 0 0 7 9
```

4. Output:

The program will output the solved Sudoku puzzle, or it will indicate if the puzzle is invalid or unsolvable.

### Example Output

```
Solving...

5 3 4 6 7 8 9 1 2
6 7 2 1 9 5 3 4 8
1 9 8 3 4 2 5 6 7
8 5 9 7 6 1 4 2 3
4 2 6 8 5 3 7 9 1
7 1 3 9 2 4 8 5 6
9 6 1 5 3 7 2 8 4
2 8 7 4 1 9 6 3 5
3 4 5 2 8 6 1 7 9
```

