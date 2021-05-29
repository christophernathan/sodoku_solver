# Sudoku Solver

This is an interactive sudoku game written in python with `pygame` integration. The program uses a simple recursive backtracking algorithm to complete partially-solved sudoku boards. The user can attempt to solve the board manually by clicking on cells within the incomplete board and typing in numbers. The user can check their work by pressing the "Check" button, which will outline correct cells with green and incorrect cells with red. The board will be automatically solved if the user clicks the "Solve" button. This also gives proper demonstration of the backtracking algorithm. The board can be reset by pressing the "Reset" button, which will wipe both auto-solved cells, as well as user input. A new board can be generated and loaded by pressing the "New Board" button. Any new board is guaranteed to have exactly 1 valid solution.

## Installation

This project uses `pip` for package management. To install, first clone the repository. If you do not have `pip`, you must first install it (see instructions [here](https://pip.pypa.io/en/stable/installing/)). `Setup.py` defines an installation routine for the `sudoku-solver` package. Initialize it by running `pip install -e .`. This will additionally install the latest version of all required libraries. If you wish to download a more strictly versioned set of dependencies (i.e. for production purposes), you can run `pip install -r requirements.txt`.

# Getting Started

This program was developed using Python 3.7.7, which can be downloaded [here](https://www.python.org/).
It utilizes pygame 2.0.1, which can be downloaded and installed by running the following command:
```
python3 -m pip install -U pygame --user
```
Once installed, the game can be run with:
```
python3 game.py
```
It is important to use the ```python3``` command instead of simply ```python```, because it will default to earlier python versions if not specified, which are incompatible with pygame 2.0.1.


# Sudoku Solver

Simple bot to automate crypto trades. Has full account integration via the Coinbase Pro API, with the ability to track account balances and place trades via a Coinbase Pro API key. Market data is managed with `numpy` and `pandas`, and `requests` is used to send HTTP requests to the API. Unit tests implemented using `pytest` and `requests-mock`. API keys managed using `dotenv`.

## Usage

After installing the `crypto-bot` package, you must create an account and API key via the [Coinbase Pro UI](https://pro.coinbase.com/profile/api). I would recommend creating a [sandbox API key](https://public.sandbox.pro.coinbase.com/profile/api) first, for testing and demo purposes. Next, create a `.env` file with 3 line-separated environment variables (API_SECRET, API_KEY, API_PASS) declared as follows: API_SECRET=XXX. 

The `bot` script command executed in the root directory will start running the trading bot. The bot will continue indefinitely until manually stopped. There is limited UI feedback provided via terminal to track the bot's activity. 

In order to switch from the Coinbase Pro sandbox environment to the production environment, change the `api_url` constant in the `bot/__main__.py` file. The `time.sleep` statement at the bottom of that file determines how often market data is pulled from the API. It is currently configured to poll the API every second to allow for expedited debugging, but you may want to increase the interval for a more realistic trading experience.

## Analysis

The bot's trading strategy revolves around the MACD indicator, which consists of the MACD line (difference between the 12 and 26 day price EMA) and a signal line (9 day EMA of the MACD line). When the MACD crosses above the signal line, the bot will attempt to open a long position in BTC. When the MACD crosses below the signal and BTC is currently held, the bot will attempt to sell all held BTC as long as the current bid price is above the cost basis + fees. By doing this, the bot should theoretically never sell at a loss. In order to test this strategy, I created a simplified implementation that manipulated BTCUSD 1 minute data from Feb 2020 to Feb 2021. Backtesting revealed an annualized return of about 444% for this time frame, but it should be noted that 2020 was certainly a bull market for crypto. Below is a visualization of this backtesting process created using `matplotlib`.

![Backtesting](backtesting.png)

## Testing

The package contains a set of unit tests for utility functions. In order to run them, use the `pytest` command in the root directory. These unit tests are not meant to be comprehensive, but test both successful and failing cases for most package utility functions.

## License

Licensed under MIT license. Copyright (c) 2021 Christopher Nathan.
