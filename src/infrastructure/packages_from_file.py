from src.domain.package_repository import PackageRepository


class PackagesFromFile(PackageRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_packages(self):
        return []
