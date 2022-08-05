import unittest
from unittest.mock import patch

from src.list_packages import list_packages


class ListPackagesTest(unittest.TestCase):
    @patch("src.list_packages.get_packages")
    def test_should_list_empty_when_no_packages(self, mock_get_packages):
        mock_get_packages.return_value = []
        all_packages = list_packages()
        self.assertListEqual([], all_packages)  # add assertion here


if __name__ == '__main__':
    unittest.main()
