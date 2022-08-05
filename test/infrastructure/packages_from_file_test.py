import unittest

from src.infrastructure.packages_from_file import PackagesFromFile


class PackagesFromFileTest(unittest.TestCase):
    def test_should_obtain_no_packages_when_database_file_empty(self):
        database = PackagesFromFile(file_path="test/fixtures/package_database/empty.txt")
        expected = []
        actual = database.get_packages()
        self.assertListEqual(expected, actual)


if __name__ == '__main__':
    unittest.main()
