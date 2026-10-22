import random
import string
from typing import List, Set

# ASCII gallows for each number of incorrect guesses (0-6)
GALLOWS = [
    r"""
     +---+
     |   |
         |
         |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
         |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
     |   |
         |
         |
    =========
    """,
    """
     +---+
     |   |
     O   |
    /|   |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
         |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    /    |
         |
    =========
    """,
    r"""
     +---+
     |   |
     O   |
    /|\  |
    / \  |
         |
    =========
    """,
]

DEFAULT_WORD_LIST = [
    "python",
    "hangman",
    "challenge",
    "programming",
    "internship",
    "computer",
    "science",
    "algorithm",
    "function",
    "variable",
]

class HangmanGame:
    """Encapsulates the Hangman game logic.

    Attributes
    ----------
    secret_word: str
        The word the player needs to guess (lower‑case).
    guessed_letters: Set[str]
        Letters that have been guessed (lower‑case).
    max_mistakes: int
        Maximum allowed incorrect guesses (default 6).
    mistakes: int
        Number of incorrect guesses made so far.
    """

    def __init__(self, secret_word: str, max_mistakes: int = 6) -> None:
        self.secret_word = secret_word.lower()
        self.guessed_letters: Set[str] = set()
        self.max_mistakes = max_mistakes
        self.mistakes = 0

    # ---------------------------------------------------------------------
    # Helper methods
    # ---------------------------------------------------------------------
    def _is_correct_guess(self, letter: str) -> bool:
        return letter in self.secret_word

    def _update_state(self, letter: str) -> None:
        """Update the game state after a new, valid guess.

        Parameters
        ----------
        letter: str
            A single lower‑case alphabetic character.
        """
        self.guessed_letters.add(letter)
        if not self._is_correct_guess(letter):
            self.mistakes += 1

    # ---------------------------------------------------------------------
    # Public API used by the UI and the tests
    # ---------------------------------------------------------------------
    def guess(self, raw_input: str) -> str:
        """Process a raw user input.

        Returns a message describing the outcome – useful for the UI and
        for unit‑testing. The method does **not** raise on invalid input; it
        simply returns an explanatory string and does not penalise the
        player.
        """
        cleaned = raw_input.strip().lower()
        # Validation – reject anything that is not a single English letter
        if len(cleaned) != 1 or cleaned not in string.ascii_lowercase:
            return "Invalid input. Please enter a single alphabetic letter."
        if cleaned in self.guessed_letters:
            return f"You already guessed '{cleaned}'."
        # Valid new guess – update state
        self._update_state(cleaned)
        if self._is_correct_guess(cleaned):
            return f"Good guess! '{cleaned}' is in the word."
        else:
            return f"Sorry, '{cleaned}' is not in the word."

    def display_word(self) -> str:
        """Return the secret word with unguessed letters shown as underscores.

        Example: secret "apple", guessed {"a", "p"} → "a p p _ e"
        """
        return " ".join([c if c in self.guessed_letters else "_" for c in self.secret_word])

    def remaining_attempts(self) -> int:
        return self.max_mistakes - self.mistakes

    def is_won(self) -> bool:
        return all(c in self.guessed_letters for c in self.secret_word)

    def is_lost(self) -> bool:
        return self.mistakes >= self.max_mistakes

    def gallows(self) -> str:
        """Return the ASCII gallows corresponding to the current mistake count."""
        return GALLOWS[self.mistakes]

    def guessed_so_far(self) -> str:
        """Return a comma‑separated list of guessed letters in alphabetical order."""
        return ", ".join(sorted(self.guessed_letters))


def select_random_word(word_list: List[str] = None) -> str:
    """Return a random word from *word_list* or the default list.

    The function is isolated so that tests can monkey‑patch ``random.choice``
    without touching the game class.
    """
    if word_list is None:
        word_list = DEFAULT_WORD_LIST
    return random.choice(word_list)


def play_game() -> None:
    """Entry‑point for the terminal based Hangman game.

    The function orchestrates input / output while delegating game logic to
    :class:`HangmanGame`. It is deliberately kept small so that the core
    mechanics remain testable.
    """
    secret = select_random_word()
    game = HangmanGame(secret)
    print("Welcome to Hangman!")
    while not (game.is_won() or game.is_lost()):
        print(game.gallows())
        print(f"Word: {game.display_word()}")
        print(f"Incorrect guesses left: {game.remaining_attempts()}")
        print(f"Guessed letters: {game.guessed_so_far()}")
        user_input = input("Enter a letter: ")
        message = game.guess(user_input)
        print(message)
        print()  # Blank line for readability
    # Game ended – final display
    print(game.gallows())
    if game.is_won():
        print(f"Congratulations! You guessed the word '{game.secret_word}'.")
    else:
        print(f"Game over. The word was '{game.secret_word}'.")


if __name__ == "__main__":
    play_game()
