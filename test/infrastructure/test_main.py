import unittest
from unittest.mock import patch

from src.infrastructure.main import main


class MainTest(unittest.TestCase):
    @patch('builtins.print')
    @patch('sys.stdin')
    def test_should_do_nothing_if_only_end_is_input(self, mock_print, mock_stdin):
        mock_stdin.readline.return_value = "END"
        main()
        assert mock_print.mock_calls == []


if __name__ == '__main__':
    unittest.main()
