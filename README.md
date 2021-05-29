# Sudoku Solver

This is an interactive sudoku game written in python with `pygame` integration. The program uses a simple recursive backtracking algorithm to complete partially-solved sudoku boards. The pygame interface is meant to provide both an interactive element to the program, as well as an visual demonstration of the backtracking algorithm at the heart of the program.

## Installation

This project uses `pip` for package management. To install, first clone the repository. If you do not have `pip`, you must first install it (see instructions [here](https://pip.pypa.io/en/stable/installing/)). `Setup.py` defines an installation routine for the `sudoku-solver` package. Initialize it by running `pip install -e .`. This will additionally install the latest version of all required libraries. If you wish to download a more strictly versioned set of dependencies (i.e. for production purposes), you can run `pip install -r requirements.txt`.

Note that `pygame 2.0.1` is incompatible with `python versions < 3`, so be sure to have `python 3` installed and use the `python3` command if running without the `sudoku-solver` package installation.

## Usage

The user can attempt to solve the board manually by clicking on cells within the incomplete board and typing in numbers. The user can check their work by pressing the "Check" button, which will outline correct cells with green and incorrect cells with red. The board will be automatically solved if the user clicks the "Solve" button. This also gives proper demonstration of the backtracking algorithm. The board can be reset by pressing the "Reset" button, which will wipe both auto-solved cells, as well as user input. A new board can be generated and loaded by pressing the "New Board" button. Any new board is guaranteed to have exactly 1 valid solution.

## Analysis

At the core of the solver is the backtracking algorithm. When given a partially-filled board, the algorithm will itiratively select successive empty cells and attempt to fill them. Before entering a value into an empty cell, the algorithm checks the row, column, and 3x3 section of the cell for a query number. Thus, any value placed into an empty cell is guaranteed to be valid. When there is no valid number in any given cell, this means there is no valid board solution for the already-placed numbers. The algorithm will then backtrack to previously-filled cells and try different numbers.

In taking this approach, any solvable board will be solved eventually. The time taken to solve the board depends on the number and placement of seed numbers on the board - the more seed numbers, the less potential numbers for eac cell, so the less backtracking will need to be done.

The program uses a similar backtracking algorithm to generate new boards. First, a full board is randomly generated. Then, numbers are removed randomly from the board, one at a time. Between each removal, the backtracking algorithm checks for all possible solutions to the board. Instead of exiting the algorithm when one solution is found (which is safe when one solution is assumed), the algorithm continues until there are either multiple valid board solutions or every possible board configuration is checked. This results in a slower execution time of the board generation (generally between 10 and 30 seconds), but guarantees only one valid solution for any generated board.

## License

Licensed under MIT license. Copyright (c) 2021 Christopher Nathan.
