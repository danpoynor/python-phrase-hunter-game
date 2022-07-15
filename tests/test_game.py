import unittest
import io
from unittest.mock import patch
import sys

# import the game module
from phrasehunter.game import Game
from phrasehunter.phrase import Phrase


class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.missed = 0
        self.correct = 0
        self.guesses = set()
        self.user_guess = None
        self.active_phrase = Phrase("Hello World")
        self.phrases = ["Hello World", "Shot In The Dark",
                        "May the force be with you", "Make it work", "Easy As Pie"]

    @patch('builtins.print')
    def test_welcome_message(self, mock_print):
        Game.welcome()
        # Showing two ways to get the mock_print call here.
        string_received_0 = mock_print.call_args_list[0][0][0]
        string_received_1 = mock_print.mock_calls[1].args[0]
        string_received_2 = mock_print.mock_calls[2].args[0]
        string_received_3 = mock_print.mock_calls[3].args[0]
        string_received_4 = mock_print.mock_calls[4].args[0]
        string_expected_0 = "=" * 79
        string_expected_1 = "Welcome to Phrase Hunter!"
        string_expected_2 = "Guess the phrase before you run out of turns."
        string_expected_3 = "5 misses and you loose the game. Good luck!"
        string_expected_4 = "=" * 79
        self.assertIn(string_received_0, string_expected_0)
        self.assertIn(string_expected_1, string_received_1)
        self.assertIn(string_expected_2, string_received_2)
        self.assertIn(string_expected_3, string_received_3)
        self.assertIn(string_expected_4, string_received_4)

    @patch('builtins.print')
    def test_active_phrase_display(self, mock_print):
        self.active_phrase.display(self.guesses)
        string_received = mock_print.mock_calls[0].args[0]
        string_expected = "The secret phrase is: _____ _____"
        self.assertIn(string_expected, string_received)

    def test_should_include_at_least_5_phrases(self):
        phrase_list = Game.create_phrases()
        self.assertGreaterEqual(len(phrase_list), 5)

    def test_get_random_phrase_returns_a_string(self):
        returned_phrase = Game.get_random_phrase(self)
        self.assertEqual(type(returned_phrase), str)

    def test_is_valid_guess(self):
        # NOTE: One way to suppress print() output in tests is to use the
        # io.StringIO() class.
        # https://stackoverflow.com/questions/24134343/suppress-print-output-in-unittests#answer-63631661
        # Another way is to use the -b flag in the test runner.
        # `$ python test.py -b`
        # https://docs.python.org/3/library/unittest.html#command-line-options
        suppress_text = io.StringIO()
        sys.stdout = suppress_text
        # Test letters are valid
        self.assertTrue(Game.is_valid_guess(self, "a"))
        self.assertTrue(Game.is_valid_guess(self, "z"))
        self.assertTrue(Game.is_valid_guess(self, "A"))
        self.assertTrue(Game.is_valid_guess(self, "Z"))
        # Test multiple letters are invalid
        self.assertFalse(Game.is_valid_guess(self, "abc"))
        # Test numbers and punctuation are invalid
        self.assertFalse(Game.is_valid_guess(self, "1"))
        self.assertFalse(Game.is_valid_guess(self, "9"))
        self.assertFalse(Game.is_valid_guess(self, ""))
        self.assertFalse(Game.is_valid_guess(self, " "))
        self.assertFalse(Game.is_valid_guess(self, "!"))
        self.assertFalse(Game.is_valid_guess(self, "?"))
        self.assertFalse(Game.is_valid_guess(self, ","))
        self.assertFalse(Game.is_valid_guess(self, "."))
        self.assertFalse(Game.is_valid_guess(self, "-"))
        self.assertFalse(Game.is_valid_guess(self, "_"))
        # Test guessing the same letter twice is invalid
        self.guesses.add("a")
        self.assertFalse(Game.is_valid_guess(self, "a"))
        # Restore stdout
        sys.stdout = sys.__stdout__

    def test_check_guess_in_phrase(self):
        # Suppress print() output
        suppress_text = io.StringIO()
        sys.stdout = suppress_text
        # Test a correct guess
        self.assertTrue(self.correct == 0)
        self.active_phrase.phrase = "Hello World".lower()
        self.user_guess = "h"
        Game.check_guess_in_phrase(self)
        self.assertTrue(self.correct == 1)
        # Test an incorrect guess
        self.assertTrue(self.missed == 0)
        self.active_phrase.phrase = "Hello World".lower()
        self.user_guess = "x"
        Game.check_guess_in_phrase(self)
        self.assertTrue(self.missed == 1)
        # Restore stdout
        sys.stdout = sys.__stdout__

    @unittest.skip("TODO: When there's more time")
    def test_game_over_winner(self):
        self.assertTrue(Game.game_over(self))

    @unittest.skip("TODO: When there's more time")
    def test_game_over_loser(self):
        self.assertTrue(Game.game_over(self))

    @unittest.skip("TODO: When there's more time, test this")
    def test_scoreboard_stats(self):
        self.assertTrue(Game.start(self))


if __name__ == '__main__':
    unittest.main()
