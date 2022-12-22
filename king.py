import colorama
from colorama import Fore, Back, Style
import numpy as np

from utils import *
from input import *
from globals import *


class king_cl:

    def __init__(self, rows1, cols1, pos_x, pos_y):
        self.rows = rows1
        self.cols = cols1

        # self.posx = spawn_t_locx
        # self.posy = spawn_t_locy

        # self.posx = king_posx
        # self.posy = king_posy

        self.posx = pos_x
        self.posy = pos_y

        self.vel_x = 1
        self.vel_y = 1

        self.score = kscore

        self.grid = ([[Back.YELLOW + Fore.RED+'K'+reset for col in range(self.cols)]
                      for row in range(self.rows)])

    def move_up(self):

        # global king_posx
        # self.posx += self.vel_x
        # king_posx += self.vel_x
        # print(king_posx)
        king_px[0] -= 1

    def move_right(self):
        king_py[0] += 1

    def move_left(self):
        king_py[0] -= 1

    def move_down(self):
        king_px[0] += 1

    def move_xy(x, y):
        pass

    def spawn(x, y):
        pass

    def get_posx():
        pass

    def get_posy():
        pass

    def shoot(x, y, building):
        pass

    def get_lives(self):
        pass  # king_life

    def get_score():
        pass


class queen_cl:

    def __init__(self, rows1, cols1, pos_x, pos_y):
        self.rows = rows1
        self.cols = cols1

        # self.posx = spawn_t_locx
        # self.posy = spawn_t_locy

        # self.posx = king_posx
        # self.posy = king_posy

        self.posx = pos_x
        self.posy = pos_y

        self.vel_x = 1
        self.vel_y = 1

        self.score = q_score

        self.grid = ([[Back.YELLOW + Fore.RED+'Q'+reset for col in range(self.cols)]
                      for row in range(self.rows)])

    def move_up(self):

        # global king_posx
        # self.posx += self.vel_x
        # king_posx += self.vel_x
        # print(king_posx)
        queen_px[0] -= 1

    def move_right(self):
        queen_py[0] += 1

    def move_left(self):
        queen_py[0] -= 1

    def move_down(self):
        queen_px[0] += 1
