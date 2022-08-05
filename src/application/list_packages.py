from src.domain.list_packages_output import ListPackagesOutput
from src.domain.package_repository import PackageRepository

from src.infrastructure.list_packages_to_console import ListPackagesToConsole
from src.infrastructure.packages_from_file import PackagesFromFile


class ListPackages:
    def __init__(self, package_repository: PackageRepository = PackagesFromFile("db.txt"),
                 output_formatter: ListPackagesOutput = ListPackagesToConsole()):
        self._output_formatter = output_formatter
        self._package_repository = package_repository

    def invoke(self):
        self._output_formatter.output_formatted(self._package_repository.get_packages())
