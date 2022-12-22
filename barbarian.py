from colorama import Fore, Back, Style
import numpy as np

from utils import *


spawn_b_locx = 0
spawn_b_locy = 0


class barb_cl:

    def __init__(self, rows1, cols1, pos_x, pos_y):
        self.rows = rows1
        self.cols = cols1

        # self.posx = spawn_b_locx
        # self.posy = spawn_b_locy

        self.posx = pos_x
        self.posy = pos_y

        self.vel_x = 1
        self.vel_y = 1

        self.grid = ([[Back.RED + Fore.BLACK+'B'+reset for col in range(self.cols)]
                      for row in range(self.rows)])

        # for i in range(self.rows):
        #     # self.grid[i][0] = Back.BLUE + Fore.BLACK+'('+reset

        #     self.grid[i][0] = "("
        #     self.grid[i][self.cols-1] = ")"

        # print_listo_ar(self.grid)

    def move_x():
        pass

    def move_y():
        pass

    def get_posx():
        pass

    def get_posy():
        pass

    def shoot(x, y):
        pass
