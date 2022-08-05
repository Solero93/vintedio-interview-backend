import unittest

from src.infrastructure.output_formatter import format_output


class OutputFormatterTest(unittest.TestCase):
    def test_should_return_empty_string_when_empty_input(self):
        what_to_format = []
        expected = ""
        actual = format_output(what_to_format)
        self.assertEqual(actual, expected)

    def test_should_format_tabulated_separated_by_newline_when_some_input(self):
        what_to_format = ["1", "2", "3"]
        expected = "\t1\n\t2\n\t3"
        actual = format_output(what_to_format)
        self.assertEqual(actual, expected)


if __name__ == '__main__':
    unittest.main()
