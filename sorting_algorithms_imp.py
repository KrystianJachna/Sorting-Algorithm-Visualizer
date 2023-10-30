
from sorting_algorithm_abs import SortingAlgorithm


class BubbleSort(SortingAlgorithm):

    @staticmethod
    def sort(lst: list[int]) -> GeneratorExit(tuple[int, int]):
        size = len(lst)

        for i in range(size):
            for j in range(0, size - i - 1):
                yield (j+1, lst[j+1]), (j, lst[j])
                if lst[j] > lst[j + 1]:
                    lst[j], lst[j + 1] = lst[j + 1], lst[j]


class InsertionSort(SortingAlgorithm):
    @staticmethod
    def sort(lst: list[int]) -> GeneratorExit(tuple[int, int]):
        size = len(lst)

        for i in range(1, size):
            current_value = lst[i]
            position = i

            yield (position - 1, lst[position - 1]), (position, current_value)

            while position > 0 and lst[position - 1] > current_value:
                lst[position] = lst[position - 1]
                yield (position - 1, lst[position - 1]), (position, current_value)
                position -= 1

            lst[position] = current_value


