from typing import List

from src.domain.list_packages_output import ListPackagesOutput


class ListPackagesToConsole(ListPackagesOutput):
    def output_formatted(self, packages: List[str]):
        tabulated_what_to_format = [f"\t{line}" for line in packages]
        formatted_packages = "\n".join(tabulated_what_to_format)
        print(formatted_packages)
