
from abc import ABC, abstractmethod


class SortingAlgorithm(ABC):
    @staticmethod
    @abstractmethod
    def sort(lst: list[int]) -> GeneratorExit(tuple[tuple[int, int], tuple[int, int]]):
        """
        Sorting algorithm template to be implemented for every added algorithm.
        Important: You have to yield every two indexes, and it's height that are being compared to show progress
        during animation. ex. ((first_index, height), (second_index, height))

        :param lst: list of values to be sorted
        :return: tuple of indexes where each index is a value that is being compared
        """

    #TODO: make functions compare/swap to show progress instead of yielding to make it more friendly to upgrade
