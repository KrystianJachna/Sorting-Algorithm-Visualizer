
from abc import ABC, abstractmethod


class SortingAlgorithm(ABC):
    @staticmethod
    @abstractmethod
    def sort(lst: list[int]) -> GeneratorExit(tuple[tuple[int, int], tuple[int, int]]):
        """
        Sorting algorithm that yields tuple of values' indexes, and it's height which are being compared.
        Important: You have to yield every two indexes, and it's height that are being compared to show progress
        during animation.

        :param lst: list of values to be sorted
        :return: tuple of indexes where each index is a value that is being compared
        """
