import unittest
from hangman import HangmanEngine
from io_utils import input_with_timeout
from words import choose_word
import time

class TestHangmanEngine(unittest.TestCase):
    def setUp(self):
        self.engine = HangmanEngine("test", lives=3)
        self.phrase_engine = HangmanEngine("software engineer", lives=3)

    def test_correct_guess(self):
        self.assertTrue(self.engine.guess("t"))
        self.assertIn("t", self.engine.state.guessed)

    def test_wrong_guess_deducts_life(self):
        self.assertFalse(self.engine.guess("x"))
        self.assertEqual(self.engine.state.lives, 2)

    def test_masked_output(self):
        self.engine.guess("t")
        self.assertEqual(self.engine.state.masked(), "t__t")

    def test_win_condition(self):
        for l in "tes":
            self.engine.guess(l)
        self.assertTrue(self.engine.state.is_won())

    def test_loss_condition(self):
        for l in "xyz":
            self.engine.guess(l)
        self.assertTrue(self.engine.state.is_lost())

    def test_input_with_timeout(self):
        """Test that input_with_timeout returns False if time runs out."""
        start_time = time.time()
        got, value = input_with_timeout("Enter letter (wait for timeout): ", 1)  # shortest timeout
        end_time = time.time()

        self.assertFalse(got)         # Should be False because no input
        self.assertIsNone(value)      # Value should be None
        self.assertGreaterEqual(end_time - start_time, 1)  # At least 1 second waited

    def test_choose_word(self):
        """Test that choose_word returns valid words/phrases and handles invalid levels."""
        basic_words = ["python", "testing", "hangman", "Ahnaf", "Rashid", "CDU", "PRT582"]
        intermediate_phrases = ["testing", "Morning Class", "software engineer", "Video Games"]
        self.assertIn(choose_word("basic"), basic_words)
        self.assertIn(choose_word("intermediate"), intermediate_phrases)
        with self.assertRaises(ValueError):
            choose_word("invalid")

    def test_phrase_masked_output(self):
        """Test masked output for phrases with spaces."""
        self.phrase_engine.guess("s")
        self.assertEqual(self.phrase_engine.state.masked(), "s_______ ________")

    def test_invalid_guess(self):
        """Test that guess raises ValueError for invalid inputs."""
        with self.assertRaises(ValueError):
            self.engine.guess("12")
        

    def test_game_loop_simulation(self):
        """Simulate game loop to test win condition progression."""
        engine = HangmanEngine("cat", lives=2)
        self.assertFalse(engine.state.is_won())
        self.assertFalse(engine.state.is_lost())
        engine.guess("c")
        engine.guess("a")
        engine.guess("t")
        self.assertTrue(engine.state.is_won())
        self.assertFalse(engine.state.is_lost())

if __name__ == "__main__":
    unittest.main()