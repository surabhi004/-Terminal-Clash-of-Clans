

import colorama
from colorama import Fore, Back, Style
import numpy as np

from utils import *

# x==rows not columns

th_rows = 1
th_cols = 1


class building():

    def __init__(self, life):
        self.life = life

    def get_life(self):
        return self.life

    def update_life(self, val):
        self.life -= val

    def shoot(self):
        pass


class hut_cl(building):
    # print("townhall")

    def __init__(self, rows_t, cols_t, pos_x, pos_y, huts_life):
        self.rows = rows_t
        self.cols = cols_t
        self.posx = pos_x
        self.posy = pos_y

        self.life = huts_life
        c1 = Fore.BLACK+Back.WHITE
        c2 = Fore.BLACK+Back.CYAN
        c3 = Fore.BLACK+Back.RED

        reset = "\033[0m"

        if(self.life >= 3):
            self.grid = ([[c1+'x'+reset for col in range(self.cols)]
                          for row in range(self.rows)])

        if(self.life == 2):
            self.grid = ([[c2+'x'+reset for col in range(self.cols)]
                          for row in range(self.rows)])

        if(self.life <= 1):
            self.grid = ([[c3+'x'+reset for col in range(self.cols)]
                          for row in range(self.rows)])

    def get_life(self):
        return self.life

    def update_life(self, val):
        self.life -= val


class cannon_cl(building):
    # print("townhall")

    def __init__(self, rows_t, cols_t, pos_x, pos_y, cnn_life):
        self.rows = rows_t
        self.cols = cols_t
        self.posx = pos_x
        self.posy = pos_y

        # self.life = huts_life
        self.c1 = Fore.BLACK+Back.BLUE
        self.c2 = Fore.BLACK+Back.CYAN
        self.c3 = Fore.BLACK+Back.RED

        self.life = cnn_life

        reset = "\033[0m"

        self.grid = ([[self.c1+'C'+reset for col in range(self.cols)]
                      for row in range(self.rows)])

    def get_life(self):
        return self.life

    def update_life(self, val):
        self.life -= val

    def shoot(self):
        pass


class wt_cl(building):
    # print("townhall")

    def __init__(self, rows_t, cols_t, pos_x, pos_y, wtx_life):
        self.rows = rows_t
        self.cols = cols_t
        self.posx = pos_x
        self.posy = pos_y

        self.life = wtx_life
        self.c1 = Fore.BLACK+Back.BLUE
        self.c2 = Fore.BLACK+Back.CYAN
        self.c3 = Fore.BLACK+Back.RED

        reset = "\033[0m"

        self.grid = ([[self.c1+'W'+reset for col in range(self.cols)]
                      for row in range(self.rows)])

    def get_life(self):
        return self.life

    def update_life(self, val):
        self.life -= val

    def shoot(self):
        pass
