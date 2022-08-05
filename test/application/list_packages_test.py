import unittest

from src.application.list_packages import ListPackages
from test.mock.packages_from_static_data import PackagesFromStaticData


class ListPackagesTest(unittest.TestCase):
    def test_should_list_empty_when_no_packages(self):
        mock_package_repository = PackagesFromStaticData([])
        list_packages = ListPackages(package_repository=mock_package_repository)
        expected = []
        actual = list_packages.invoke()
        self.assertListEqual([], actual)


if __name__ == '__main__':
    unittest.main()
