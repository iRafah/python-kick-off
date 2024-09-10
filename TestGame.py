import unittest
import main


class TestGame(unittest.TestCase):
    def test_input(self):
        answer = 5
        guess = 5
        result = main.checkNumberGuessed(guess, answer)
        self.assertTrue(result)

    def test_input_wrong_guess(self):
        result = main.checkNumberGuessed(10, 2)
        self.assertFalse(result)

    def test_input_wrong_range(self):
        result = main.checkNumberGuessed(12, 4)
        self.assertFalse(result)

    def test_input_wrong_type(self):
        result = main.checkNumberGuessed(5, '4')
        self.assertFalse(result)


if __name__ == '__main__':number
    unittest.main()
