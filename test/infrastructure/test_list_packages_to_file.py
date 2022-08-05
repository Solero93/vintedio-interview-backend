import unittest
from unittest.mock import patch, call

from src.infrastructure.list_packages_to_console import ListPackagesToConsole


class OutputFormatterTest(unittest.TestCase):
    @patch('builtins.print')
    def test_should_return_empty_string_when_empty_input(self, mock_print):
        subject = ListPackagesToConsole()
        packages = []
        expected = ""
        subject.output_formatted(packages)
        assert mock_print.mock_calls == [call(expected)]

    @patch('builtins.print')
    def test_should_format_tabulated_separated_by_newline_when_some_input(self, mock_print):
        subject = ListPackagesToConsole()
        packages = ["1", "2", "3"]
        expected = "\t1\n\t2\n\t3"
        subject.output_formatted(packages)
        assert mock_print.mock_calls == [call(expected)]


if __name__ == '__main__':
    unittest.main()
