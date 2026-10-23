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
### Task 3: Automated File Organizer & Cleanup Utility

A Python utility that automatically organizes files into folders based on their file extensions.

**Features**
- Categorizes files into Documents, Images, Videos, Archives, Code, and Other.
- Provides a dry-run mode to preview changes before moving files.
- Avoids overwriting files with duplicate names.
- Handles invalid paths and filesystem errors.
- Displays a summary of moved, skipped, and failed files.
- Includes automated unit tests.

**Run the project**
```powershell
python .\task3\organizer.py
```

**Run the tests**
```powershell
python -m unittest discover -s task3\tests -v
```

**Safety:** Test with a sample directory and preview planned changes before organizing real files. The utility processes files in the selected directory's top level.


## Technologies
- Python
- CSV
- Unit testing with `unittest`
- Git and GitHub

## License
This project is licensed under the MIT License. See [LICENSE](LICENSE).
