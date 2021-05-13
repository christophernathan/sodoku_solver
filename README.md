# Sudoku Solver

This is an interactive sudoku game written in python with pygame integration. The program uses a simple recursive backtracking algorithm to complete partially-solved sudoku boards. The user can attempt to solve the board manually by clicking on cells within the incomplete board and typing in numbers. The user can check their work by pressing the "Check" button, which will outline correct cells with green and incorrect cells with red. The board will be automatically solved if the user clicks the "Solve" button. This also gives proper demonstration of the backtracking algorithm. The board can be reset by pressing the "Reset" button, which will wipe both auto-solved cells, as well as user input. A new board can be generated and loaded by pressing the "New Board" button. Any new board is guaranteed to have exactly 1 valid solution.

# Getting Started

This program was developed using Python 3.7.7, which can be downloaded from https://www.python.org/.
It utilizes pygame 2.0.1, which can be downloaded and installed by running the following command:
```
python3 -m pip install -U pygame --user
```
Once installed, the game can be run with:
```
python3 game.py
```
It is important to use the ```python3``` command instead of simply ```python```, because it will default to earlier python versions if not specified, which are incompatible with pygame 2.0.1.
