# Datheon Python Programming Internship

A collection of Python projects completed as part of the Datheon Python Programming Internship.

## Projects

### Task 1: Hangman Game
A command-line word-guessing game built with Python.

**Features**
- Interactive gameplay
- Guess letters to reveal the hidden word
- Tracks incorrect guesses and game progress

**Run the project**
```bash
python hangman/hangman.py
```

> Adjust the filename above if your Hangman entry-point file has a different name.

### Task 2: Stock Portfolio Performance Tracker
A Python command-line application that calculates stock portfolio performance using offline sample prices.

**Features**
- Interactive stock ticker, purchase price, and quantity inputs
- Calculates investment value and profit or loss
- Summarizes portfolio performance
- Exports a CSV report
- Includes unit tests

**Run the project**
```bash
python task2/portfolio.py
```

**Run the tests**
```bash
python -m unittest discover -s task2/tests -v
```

**Price data:** This project uses offline sample prices and does not fetch live market quotes. The results are for demonstration and educational purposes.

## Project Structure

```text
Datheon_Python_Programming_Internship/
├── hangman/
├── tests/
├── task2/
│   ├── tests/
│   ├── portfolio.py
│   ├── sample_prices.csv
│   ├── portfolio_summary.csv
│   └── README.md
├── .gitignore
├── LICENSE
└── README.md
```

## Technologies
- Python
- CSV
- Unit testing with `unittest`
- Git and GitHub

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE).
