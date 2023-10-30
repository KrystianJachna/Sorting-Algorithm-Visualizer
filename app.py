import time
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
        # todo list of sorting algorithms
        self.Sort_Algorithm = InsertionSort
        self.sorting_fun = self.Sort_Algorithm.sort(self.lst)

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
                (x, self.pad_y // 2, width, self.screen_height - self.pad_y)
            ))

        pygame.draw.rect(self.screen, color, (x, y, width, height))

    def draw(self):
        self.screen.fill(BLACK)

        # todo print instruction for user

        # print value bars
        for i, _ in enumerate(self.lst):
            self.draw_value_bar(i)

    def sort(self):
        try:
            red, green = next(self.sorting_fun)
        except StopIteration:
            return

        if red and green:
        # todo try to print elemnt that is being moved during animation (red is element being checked, green being
        #  moved)
            self.draw()
            self.draw_value_bar(red[0], RED, height=red[1], with_reset=True)
            self.draw_value_bar(green[0], GREEN, height=green[1], with_reset=True)


    def reset(self):
        self.lst = self.get_random_list()
        self.sorting_fun = self.Sort_Algorithm.sort(self.lst)

    def main_loop(self):
        running = True
        sorting = False
        clock = pygame.time.Clock()

        while running:
            clock.tick(FPS)
            self.draw()

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                if event.type == pygame.KEYDOWN:
                    # todo handle different sorting types
                    if event.key == pygame.K_ESCAPE:
                        running = False
                    if event.key == pygame.K_r:
                        sorting = False
                        self.reset()
                    if event.key == pygame.K_SPACE:
                        sorting = not sorting

            if sorting:
                self.sort()
            pygame.display.flip()
            #time.sleep()    # todo for testing
        pygame.quit()
