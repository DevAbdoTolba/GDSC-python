import unittest
from unittest.mock import patch
from io import StringIO
from Game.StartGame import main

class TestStartGame(unittest.TestCase):

    @patch('sys.stdin', StringIO('50\n'))
    def test_main(self):
        with patch('builtins.print') as mock_print:
            main()
            mock_print.assert_called_with("Congratulations! You guessed the number in 1 attempts!")
