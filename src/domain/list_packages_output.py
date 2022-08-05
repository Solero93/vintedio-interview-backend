from abc import ABC, abstractmethod
from typing import List


class ListPackagesOutput(ABC):
    @abstractmethod
    def output_formatted(self, packages: List[str]):
        pass
