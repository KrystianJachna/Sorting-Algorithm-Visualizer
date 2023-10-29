
from abc import ABC, abstractmethod


class SortingAlgorithm(ABC):
    @staticmethod
    @abstractmethod
    def sort(lst: list[int]) -> GeneratorExit(tuple[int, int]):
        """
        Sorting algorithm that yields tuple of values' indexes which are being compared.
        Important: yield every indexes that are being compared

        :param lst: list of values to be sorted
        :return: tuple of indexes where each index is a value that is being compared
        """
