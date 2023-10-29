
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

        # list settings
        self.list_length = list_length
        self.min_value = min_value
        self.max_value = max_value
        self.lst = self.get_random_list()
        self.value_bar_width = round((self.screen_width - self.pad_x) / self.list_length - VALUES_BAR_SPACE)

        if self.value_bar_width < 1:
            raise ValueError("Too small screen for too many values")

        # sorting
        self.Sort_Algorithm = InsertionSort
        self.sorting_fun = self.Sort_Algorithm.sort(self.lst)

    def get_random_list(self):
        return [randint(self.min_value, self.max_value) for _ in range(self.list_length)]

    def draw_value_bar(self, list_index, color=WHITE):
        # count x,y coordinate from which we start drawing value bar
        x = ceil(list_index * (self.value_bar_width + VALUES_BAR_SPACE) + self.pad_x / 2)
        y = ceil(((self.screen_height - self.pad_y) * (1 - self.lst[list_index] / self.max_value)) + self.pad_y / 2)

        # count width and height of value bar
        width = self.value_bar_width
        height = self.screen_height - self.pad_y/2 - y

        pygame.draw.rect(self.screen, color, (x, y, width, height))

    def draw(self):
        self.screen.fill(BLACK)

        # todo print instruction for user

        # print value bars
        for i, _ in enumerate(self.lst):
            self.draw_value_bar(i)

    def sort(self):
        try:
            compared = next(self.sorting_fun)
        except StopIteration:
            return

        if compared is not None:
        # todo try to print elemnt that is being moved during animation (red is element being checked, green being moved)
            self.draw()
            self.draw_value_bar(compared[0], RED)
            self.draw_value_bar(compared[1], GREEN)
            pygame.display.flip()

    def main_loop(self):
        running = True
        sorting = False
        clock = pygame.time.Clock()

        while running:
            clock.tick(FPS)
            self.draw()
            pygame.display.flip()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # todo handle different sorting types
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_r:
                        sorting = False
                        self.lst = self.get_random_list()
                        self.sorting_fun = self.Sort_Algorithm.sort(self.lst)
                    if event.key == pygame.K_SPACE:
                        sorting = not sorting

            if sorting:
                self.sort()

        pygame.quit()
