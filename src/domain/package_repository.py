import abc


class PackageRepository(abc.ABC):
    @abc.abstractmethod
    def get_packages(self):
        pass
