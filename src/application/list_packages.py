from typing import List

from src.domain.package_repository import PackageRepository
from src.infrastructure.packages_from_file import PackagesFromFile


class ListPackages:
    def __init__(self, package_repository: PackageRepository = PackagesFromFile()):
        self.package_repository = package_repository

    def invoke(self) -> List[str]:
        return self.package_repository.get_packages()
