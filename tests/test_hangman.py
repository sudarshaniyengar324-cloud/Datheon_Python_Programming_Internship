import unittest
from unittest.mock import patch
import string

# Import the game module
from hangman.hangman import HangmanGame, select_random_word, DEFAULT_WORD_LIST

class TestHangmanGame(unittest.TestCase):
    def setUp(self):
        # Use a deterministic word for most tests
        self.game = HangmanGame("apple")

    def test_initial_state(self):
        self.assertEqual(self.game.display_word(), "_ _ _ _ _")
        self.assertEqual(self.game.remaining_attempts(), 6)
        self.assertFalse(self.game.is_won())
        self.assertFalse(self.game.is_lost())

    def test_correct_guess_reveals_letters(self):
        msg = self.game.guess('a')
        self.assertIn("Good guess", msg)
        self.assertEqual(self.game.display_word(), "a _ _ _ _")
        self.assertEqual(self.game.mistakes, 0)

    def test_multiple_occurrences(self):
        self.game.guess('p')
        self.assertEqual(self.game.display_word(), "_ p p _ _")
        self.assertEqual(self.game.mistakes, 0)

    def test_incorrect_guess_increments_mistake(self):
        msg = self.game.guess('z')
        self.assertIn("Sorry", msg)
        self.assertEqual(self.game.mistakes, 1)
        self.assertEqual(self.game.remaining_attempts(), 5)

    def test_duplicate_guess_no_penalty(self):
        self.game.guess('a')
        before = self.game.mistakes
        msg = self.game.guess('a')
        self.assertIn("already guessed", msg)
        self.assertEqual(self.game.mistakes, before)

    def test_invalid_input_rejected(self):
        for invalid in ["", "ab", "1", "!", "ä"]:
            with self.subTest(invalid=invalid):
                msg = self.game.guess(invalid)
                self.assertIn("Invalid input", msg)
                self.assertEqual(self.game.mistakes, 0)

    def test_win_condition(self):
        for l in "aple":
            self.game.guess(l)
        self.assertTrue(self.game.is_won())
        self.assertFalse(self.game.is_lost())

    def test_loss_condition(self):
        for l in ['b', 'c', 'd', 'f', 'g', 'h']:
            self.game.guess(l)
        self.assertTrue(self.game.is_lost())
        self.assertFalse(self.game.is_won())

    def test_case_insensitive_guess(self):
        msg = self.game.guess('A')
        self.assertIn("Good guess", msg)
        self.assertIn('a', self.game.guessed_letters)

    def test_select_random_word_is_deterministic_when_patched(self):
        with patch('random.choice', return_value='testing'):
            word = select_random_word()
        self.assertEqual(word, 'testing')

    def test_final_missing_letter_triggers_win(self):
        # Guess all but one letter correctly
        for l in ['a', 'p', 'l']:
            self.game.guess(l)
        self.assertFalse(self.game.is_won())
        # Guess final missing letter
        self.game.guess('e')
        self.assertTrue(self.game.is_won())

if __name__ == '__main__':
    unittest.main()
