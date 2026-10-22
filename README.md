# Datheon Python Programming Internship – Hangman Game

## Project Overview

This repository contains a **terminal‑based Hangman game** developed as part of the Datheon Python Programming Internship (Task 1). The game is written in pure Python 3 using only the standard library and follows the specifications provided by the internship brief.

### Features
- Randomly selects a secret English word from a built‑in word list.
- Allows the player to guess one letter at a time.
- Limits the player to **six** incorrect guesses.
- Displays ASCII gallows that update after each wrong guess.
- Shows correctly guessed letters while hiding the rest with underscores.
- Tracks previously guessed letters and prevents duplicate guesses from reducing the remaining attempts.
- Robust input validation (rejects empty input, digits, punctuation, multi‑character strings, and non‑English letters) without penalty.
- Provides clear victory/defeat messages and reveals the secret word on loss.
- Graceful handling of unexpected errors.

## Technologies Used
- **Python 3** – Standard library only (no external dependencies).
- **unittest** – Python’s built‑in testing framework.

## Prerequisites
- Windows 10/11 (or any OS with Python 3 installed).
- Python 3.8+ (the code uses type hints and f‑strings).
- Git (optional, for version control).

## Setup – Windows
1. Open **PowerShell** or **Command Prompt**.
2. Navigate to the directory where you want the project:
   ```powershell
   cd C:\Users\sudar\Datheon_Python_Programming_Internship
   ```
3. (Optional) Create a virtual environment:
   ```powershell
   python -m venv venv
   .\venv\Scripts\activate
   ```
   The project has no external dependencies, so this step is optional.

## Running the Game
```powershell
python -m hangman.hangman
```
The game runs in the terminal. Follow the prompts to guess letters.

## Running the Automated Tests
```powershell
python -m unittest discover -s tests -v
```
All tests should pass. The test suite covers word display, input validation, game‑logic, and edge cases.

## Example Terminal Session
```
Welcome to Hangman!
Word: _ _ _ _ _
Incorrect guesses left: 6
Guessed letters: 
Enter a letter: a
Good guess!
Word: a _ _ a _
Incorrect guesses left: 6
Guessed letters: a
Enter a letter: x
Oops! That letter is not in the word.
Word: a _ _ a _
Incorrect guesses left: 5
Guessed letters: a, x
... (game continues) ...
Congratulations! You guessed the word "apple".
```
*(Your actual output will vary based on the random word.)*

## Project Structure
```
Datheon_Python_Programming_Internship/
├── hangman/
│   └── hangman.py      # Game implementation
├── tests/
│   └── test_hangman.py # Unit tests
├── screenshots/
│   └── .gitkeep        # Placeholder for future screenshots
├── .gitignore
├── LICENSE
└── README.md
```

## Game Rules
1. The secret word is chosen at random from a predefined list.
2. You may guess **one** letter per turn.
3. You have **six** incorrect guesses before the game ends.
4. Re‑guessing a previously guessed letter does **not** count against you.
5. Invalid inputs (numbers, symbols, multiple characters, etc.) are ignored without penalty.
6. The game displays the current state of the word, the gallows diagram, remaining attempts, and guessed letters after each turn.

## Known Limitations
- The word list is static and limited to a few dozen common English words.
- The game runs only in a terminal/console environment.
- No colour or advanced UI – plain ASCII for maximum compatibility.

## License
This project is licensed under the **MIT License**. See the `LICENSE` file for details.

## Screenshots
*Add screenshots of the game in action here after you run it.*
