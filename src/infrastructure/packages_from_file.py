from src.domain.package_repository import PackageRepository


class PackagesFromFile(PackageRepository):
    def __init__(self, file_path: str):
        self.file_path = file_path

    def get_packages(self):
        with open(self.file_path, "r") as database_file:
            return [package.rstrip("\n") for package in database_file.readlines()]
