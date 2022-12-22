from colorama import Fore, Back, Style
import numpy as np

from utils import *

th_posx = 10
th_posy = 70
th_rows = 3
th_cols = 4

th_life = []
th_life.append(5)

townhall_g = ([[background+'x'+reset for col in range(th_rows)]
               for row in range(th_cols)])


class townhall_cl:

    def __init__(self, rows_t, cols_t):
        self.rows = rows_t
        self.cols = cols_t
        self.life = th_life[0]
        c1 = Back.YELLOW + Fore.CYAN
        c2 = Fore.BLACK+Back.CYAN
        c3 = Fore.BLACK+Back.RED

        reset = "\033[0m"

        if(self.life >= 3):
            self.grid = ([[c1+'x'+reset for col in range(self.cols)]
                          for row in range(self.rows)])

        if(self.life <= 2):
            self.grid = ([[c2+'x'+reset for col in range(self.cols)]
                          for row in range(self.rows)])

        if(self.life <= 1):
            self.grid = ([[c3+'x'+reset for col in range(self.cols)]
                          for row in range(self.rows)])

        self.grid[0][0] = Back.YELLOW + Fore.RED+'t'+reset

        self.grid[0][1] = Back.YELLOW + Fore.RED+'o'+reset
        self.grid[0][2] = Back.YELLOW + Fore.RED+'w'+reset

        self.grid[0][3] = Back.YELLOW + Fore.RED+'n'+reset

        if(self.life <= 0):
            self.grid = ([[background for col in range(self.cols)]
                          for row in range(self.rows)])

            self.grid[0][0] = background

            self.grid[0][1] = background
            self.grid[0][2] = background

            self.grid[0][3] = background

        # self.grid[0][4] = Back.YELLOW + Fore.RED+'h'+reset

        # self.grid[0][5] = Back.YELLOW + Fore.RED+'a'+reset

        # self.grid[0][6] = Back.YELLOW + Fore.CYAN+'l'+reset
