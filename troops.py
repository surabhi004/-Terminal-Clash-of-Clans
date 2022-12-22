from colorama import Fore, Back, Style
import numpy as np

from utils import *
from input import *

from globals import *


spawn_t_locx = 0
spawn_t_locy = 0

troop_speed_gl = 1

# balloons


class tr_cl():

    def __init__(self, rows1, cols1, pos_x, pos_y, velx, vely):
        self.rows = rows1
        self.cols = cols1
        self.posx = pos_x
        self.posy = pos_y

        self.vel_x = velx
        self.vel_y = vely


class troop_cl(tr_cl):

    def __init__(self, rows1, cols1, pos_x, pos_y, velx, vely):
        self.rows = rows1
        self.cols = cols1

        # self.posx = spawn_t_locx
        # self.posy = spawn_t_locy

        self.posx = pos_x
        self.posy = pos_y

        self.vel_x = velx
        self.vel_y = vely

        self.grid = ([[Back.BLUE + Fore.BLACK+'N'+reset for col in range(self.cols)]
                      for row in range(self.rows)])

        # for i in range(self.rows):
        #     # self.grid[i][0] = Back.BLUE + Fore.BLACK+'('+reset

        #     self.grid[i][0] = "("
        #     self.grid[i][self.cols-1] = ")"

        # print_listo_ar(self.grid)

    def move_x(self):
        self.posx += self.vel_x

    def move_y():
        pass

    def get_posx():
        pass

    def get_posy():
        pass

    def shoot(x, y):
        pass


class bl_cl(tr_cl):

    def __init__(self, rows1, cols1, pos_x, pos_y, velx, vely):
        self.rows = rows1
        self.cols = cols1

        self.posx = pos_x
        self.posy = pos_y

        self.vel_x = velx
        self.vel_y = vely

        self.grid = ([[Back.YELLOW + Fore.BLACK+'O'+reset for col in range(self.cols)]
                      for row in range(self.rows)])


class archer_cl(tr_cl):

    def __init__(self, rows1, cols1, pos_x, pos_y, velx, vely):
        self.rows = rows1
        self.cols = cols1

        self.posx = pos_x
        self.posy = pos_y

        self.vel_x = velx
        self.vel_y = vely

        self.grid = ([[Back.BLUE + Fore.BLACK+'A'+reset for col in range(self.cols)]
                      for row in range(self.rows)])

    def archer_collision_backup(self):
        global no_of_huts
        global no_of_walls

        # for j in range(len(archers_list)):
        for ax in archers_list:

            for i in range(len(huts)-1):
                if(abs(ax.posy-huts[i].posy)+abs(ax.posx-huts[i].posx) <= 8):

                    if(huts_life[i] <= 1):
                        self.grid[huts[i].posx][huts[i].posy] = background
                        del huts[i]
                        del hutx[i]
                        del huty[i]

                        no_of_huts -= 1
                        # del huts_life[i]
                        # kscore += 15

                    else:
                        huts[i].life -= 5
                        huts_life[i] -= 5

            # find shortest hut

            # check with walls
