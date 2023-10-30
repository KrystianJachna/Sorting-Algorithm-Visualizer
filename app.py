
from random import randint
import pygame
from settings import *
from math import ceil
from sorting_algorithms_imp import *


class App:

    def __init__(self, screen_width=SCREEN_WIDTH, screen_height=SCREEN_HEIGHT,
                 list_length=LIST_LENGTH, min_value=LIST_MIN, max_value=LIST_MAX):
        pygame.init()
        pygame.display.set_caption("Sorting Visualizer")

        # screen settings
        self.screen_width = screen_width
        self.screen_height = screen_height
        self.screen = pygame.display.set_mode(
            (self.screen_width, self.screen_height)
        )
        self.pad_x = PAD_X
        self.pad_y = PAD_Y
        self.font = pygame.font.SysFont("comicsans", 30)

        # list settings
        self.list_length = list_length
        self.min_value = min_value
        self.max_value = max_value
        self.lst = self.get_random_list()
        self.value_bar_width = round((self.screen_width - self.pad_x) / self.list_length - VALUES_BAR_SPACE)

        if self.value_bar_width < 1:
            raise ValueError("Too small screen for too many values")
        if self.pad_y < 50:
            raise Exception("Too small y-padding")

        # sorting
        self.sorting_algorithms = [BubbleSort, InsertionSort]
        self.current_algorithm_index = 0
        self.sorting_fun = self.sorting_algorithms[0].sort(self.lst)

        # sorting delay
        self.delay_list = [0, 50, 150]
        self.current_delay_index = 0
        self.current_delay = self.delay_list[0]
        self.delay_names = {0: "fast", 50: "medium", 150: "slow"}

    def change_delay(self):
        self.current_delay_index = (self.current_delay_index + 1) % len(self.delay_list)
        self.current_delay = self.delay_list[self.current_delay_index]

    def change_algorithm(self):
        self.current_algorithm_index = (self.current_algorithm_index + 1) % len(self.sorting_algorithms)
        self.sorting_fun = self.sorting_algorithms[self.current_algorithm_index].sort(self.lst)

    def get_random_list(self):
        return [randint(self.min_value, self.max_value + 1) for _ in range(self.list_length)]

    def draw_value_bar(self, list_index, color=WHITE, height=None, with_reset=False):
        height = height if height is not None else self.lst[list_index]

        # count x,y coordinate from which we start drawing value bar
        x = ceil(list_index * (self.value_bar_width + VALUES_BAR_SPACE) + self.pad_x / 2)
        y = ceil(((self.screen_height - self.pad_y) * (1 - height / self.max_value)) + self.pad_y / 2)

        # count width and height of value bar
        width = self.value_bar_width
        height = self.screen_height - self.pad_y / 2 - y

        # clear previous shown bar
        if with_reset:
            pygame.display.update(pygame.draw.rect(
                self.screen,
                BLACK,
                (x, self.pad_y // 2 - 10, width, self.screen_height - self.pad_y + 10)
            ))
            pygame.display.update(pygame.draw.rect(self.screen, color, (x, y, width, height)))
        else:
            pygame.draw.rect(self.screen, color, (x, y, width, height))

    def draw_info(self, sorting):
        options = self.font.render("R - Reset & Randomize  |  SPACE - Start/Stop Sorting  |  "
                                   "C - Change Algorithm  |  S - Speed sorting",
                                   True, GREY)
        self.screen.blit(options, (self.screen_width // 2 - options.get_width() // 2, self.pad_y // 4))

        state = "sorting" if sorting else "stopped"

        sorting_info = self.font.render(f"Algorithm: "
                                        f"{self.sorting_algorithms[self.current_algorithm_index].__name__}  "
                                        f"|  State: {state}  |  "
                                        f"Speed: {self.delay_names[self.delay_list[self.current_delay_index]]}",
                                        True, GREY)
        self.screen.blit(sorting_info, (self.screen_width // 2 - sorting_info.get_width() // 2,
                                        self.screen_height - self.pad_y // 4))

    def draw(self, sorting=False):
        self.screen.fill(BLACK)
        self.draw_info(sorting)

        # print value bars
        for i, _ in enumerate(self.lst):
            self.draw_value_bar(i)

    def sort(self):
        try:
            red, green = next(self.sorting_fun)
        except StopIteration:
            return False

        if red and green:
            self.draw(sorting=True)
            self.draw_value_bar(red[0], RED, height=red[1], with_reset=True)
            self.draw_value_bar(green[0], GREEN, height=green[1], with_reset=True)
        return True

    def reset(self):
        self.lst = self.get_random_list()
        self.sorting_fun = self.sorting_algorithms[self.current_algorithm_index].sort(self.lst)

    def main_loop(self):
        running = True
        sorting = False
        clock = pygame.time.Clock()

        while running:
            clock.tick(FPS)
            self.draw(sorting)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_c:
                        self.change_algorithm()
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_r:
                        sorting = False
                        self.reset()
                    if event.key == pygame.K_SPACE:
                        sorting = not sorting
                    if event.key == pygame.K_s:
                        self.change_delay()

            if sorting:
                sorting = self.sort()

            pygame.display.flip()
            pygame.time.delay(self.current_delay)
        pygame.quit()
