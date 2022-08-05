from typing import List

from src.domain.package_repository import PackageRepository


class PackagesFromStaticData(PackageRepository):
    def __init__(self, static_data: List[str]):
        self.static_data = static_data

    def get_packages(self) -> List[str]:
        return self.static_data
