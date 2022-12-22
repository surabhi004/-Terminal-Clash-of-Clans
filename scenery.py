from buildings import *
from king import *
from townhall import *
import colorama
from colorama import Fore, Back, Style
import numpy as np
import random
import time

from utils import *
from troops import *
from barbarian import *
from other import *
from globals import *

from input import *
import os
colorama.init()
reset = "\033[0m"

# troops_list = []
troops_posx = []
troops_posy = []

tr_gl_vlx = []
tr_gl_vly = []

troop_move_flag = []
troop_move_flag.append(0)

# spawn locs
troop1_posx = 10
troop1_posy = 80

# spawn locs in the middle
# archer1_posx = 15
# archer1_posy = 90

# CHANGE TO THIS IN THE FINAL CODE
# spawn locs at the top
# archer1_posx = 2
# archer1_posy = 120


archer1_posx = 7
archer1_posy = 100

# spawn loc at the bottom
archer2_posx = 15
archer2_posy = 100

# spawn balloons
b1_posx = 25
b1_posy = 20

# spawn loc for barb
barb_new_posx = 10
barb_new_posy = 130

# positon arrays
barbs_posx = []
barbs_posy = []


# QUEENS AOE CORRDINATES
# upper left,upper right,down left,downright
aoe = [[0, 0], [0, 0], [0, 0], [0, 0]]
aoe_w = [[0, 0], [0, 0], [0, 0], [0, 0]]

shortest_build_x = []
shortest_build_y = []
sht_dist = []
sht_build_index = []


shortest_build_bx = []
shortest_build_by = []
sht_dist_b = []
sht_build_index_b = []

for i in range(total_archers[0]):
    sht_dist.append(150)
    shortest_build_x.append(150)
    shortest_build_y.append(150)
    sht_build_index.append(0)

for i in range(total_balloons[0]):
    sht_dist_b.append(150)
    shortest_build_bx.append(150)
    shortest_build_by.append(150)
    sht_build_index_b.append(0)

# king_px = []
# king_px.append(4)

# king_py = []
# king_py.append(4)
# wall loc
wx = 30
wy = 80
wall_col = Back.YELLOW + Fore.BLACK+'|'+reset

wx1 = 10
wy1 = 120

wall_px = []
# wall_px.append(wx1)
wall_py = []
# wall_py.append(wy1)


left = []
left.append(False)
right = []
right.append(False)
up = []
up.append(False)
down = []
down.append(False)

for i in range(no_of_walls[0]):
    wall_px.append(wx1+i)

for i in range(no_of_walls[0]):
    wall_py.append(wy1)

gems = 0

king_posx = 4
king_posy = 4
for i in range(no_of_troops):

    y = troop1_posy+i+5

    troops_posx.append(troop1_posx+i)
    troops_posy.append(y)
    tr_gl_vlx.append(1)
    tr_gl_vly.append(1)

for i in range(no_of_barbs):

    barbs_posx.append(barb_new_posx+i)
    barbs_posy.append(barb_new_posy+i+5)


def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):
        command = 'cls'
    os.system(command)


index = []
index.append(0)


class scenery:
    def __init__(self, rows1, cols1):

        index[0] = 0

        self.grid = ([[Back.BLACK + Fore.GREEN+'.'+reset for col in range(cols1)]
                      for row in range(rows1)])
        self.rows = rows1
        self.cols = cols1

        self.wall_list = []

        # walls
        # self.grid[wx][wy] = wall_col
        # self.wall_list.append(wall(wx, wy))
        # walls.append(wall(wx, wy))

        # the wall next to the townhall
        # self.grid[wx1][wy1] = wall_col
        # self.grid[wx1+1][wy1] = wall_col
        # self.grid[wx1+2][wy1] = wall_col
        # self.grid[wx1+3][wy1] = wall_col
        # self.grid[wx1+4][wy1] = wall_col

        for i in range(no_of_walls[0]):
            self.wall_list.append(wall(wall_px[i], wall_py[i], wall_lifes[i]))
            walls.append(wall(wall_px[i], wall_py[i], wall_lifes[i]))
            self.grid[wall_px[i]][wall_py[i]] = wall_col

        # bullest lists because globals are not working it is appending to the list

        self.bullets_t = []
        self.bullets_b = []

        # townhall

        # self.townH = townhall_cl(5, 7)
        self.townH = townhall_cl(3, 4)
        buildings.append(self.townH)
        building_px.append(th_posx)
        building_py.append(th_posy)
        # index=0
        build_index.append(index[0])
        building_life.append(th_life[0])
        index[0] += 1

        if(th_life[0] > 0):

            for i in range(th_rows):
                for j in range(th_cols):
                    self.grid[i+th_posx][j+th_posy] = self.townH.grid[i][j]

        # huts

        for i in range(no_of_huts[0]):

            self.hut1 = hut_cl(1, 1, hutx[i], huty[i], huts_life[i])

            if(huts_life[i] > 0):
                self.hut1.life = huts_life[i]
                huts.append(self.hut1)
                buildings.append(self.hut1)
                building_px.append(hutx[i])
                building_py.append(huty[i])
                building_life.append(huts_life[i])

                # 1 to 1 +no_of_huts------index
                build_index.append(index[0])
                index[0] += 1

                for i in range(self.hut1.rows):
                    for j in range(self.hut1.cols):
                        if(within_bounds(i+self.hut1.posx, j + self.hut1.posy)):
                            self.grid[i+self.hut1.posx][j +
                                                        self.hut1.posy] = self.hut1.grid[i][j]

        # king
        # global king_posx
        if(king_flag[0] == True):
            self.king = king_cl(1, 1, king_px[0], king_py[0])

            if(king_health[0] > 0):
                for i in range(1):
                    for j in range(1):
                        self.grid[i+self.king.posx][j +
                                                    self.king.posy] = self.king.grid[i][j]

        if(queen_flag[0] == True):
            self.queen = queen_cl(1, 1, queen_px[0], queen_py[0])

            if(queen_health[0] > 0):

                for i in range(1):
                    for j in range(1):
                        self.grid[i+self.queen.posx][j +
                                                     self.queen.posy] = self.queen.grid[i][j]

        # cannon

        for k in range(no_of_cannons[0]):

            self.cannon1 = cannon_cl(1, 1, can_px[k], can_py[k], cnn_life[k])
            if(self.cannon1.life > 0):
                for i in range(1):
                    for j in range(1):
                        self.grid[i+self.cannon1.posx][j +
                                                       self.cannon1.posy] = self.cannon1.grid[i][j]

                cannons.append(self.cannon1)
                buildings.append(self.cannon1)
                building_px.append(self.cannon1.posx)
                building_py.append(self.cannon1.posy)
                building_life.append(cnn_life[k])

                build_index.append(index[0])
                index[0] += 1

            # 1+no_of_huts to 1+no_of_huts+no_of_cannons

        # wizard towers

        for k in range(no_of_wt[0]):

            self.wt1 = wt_cl(1, 1, wt_x[k], wt_y[k], wt_life[k])

            if(self.wt1.life > 0):

                for i in range(1):
                    for j in range(1):
                        self.grid[i+self.wt1.posx][j +
                                                   self.wt1.posy] = self.wt1.grid[i][j]

                wizards.append(self.wt1)
                buildings.append(self.wt1)
                building_px.append(self.wt1.posx)
                building_py.append(self.wt1.posy)
                building_life.append(wt_life[k])

                build_index.append(index[0])
                index[0] += 1
            # index

            # 1+no_of_huts+no_of_cannons to 1+no_of_huts+no_of_cannons+no_of_wt

        # troops

        if(flag_t[0] == 1):
            for k in range(no_of_troops):

                self.troop1 = troop_cl(
                    1, 1, troops_posx[k], troops_posy[k], tr_gl_vlx[k], tr_gl_vly[k])
                # self.troop1.posx=troop1_posx
                troops_list.append(self.troop1)

                for i in range(self.troop1.rows):
                    for j in range(self.troop1.cols):
                        if(within_bounds(i+self.troop1.posx, j + self.troop1.posy)):
                            self.grid[i+self.troop1.posx][j +
                                                          self.troop1.posy] = self.troop1.grid[i][j]
            troop_move_flag[0] = 1

        # ARCHERS

        if(flag_4[0] == 1 or flag_5[0] == 1):
            for k in range(no_of_archers[0]):

                print(archers_posx)
                print(archers_posy)
                print(ar_gl_vlx)
                print(ar_gl_vly)

                self.archer1 = archer_cl(
                    1, 1, archers_posx[k], archers_posy[k], ar_gl_vlx[k], ar_gl_vly[k])
                archers_list.append(self.archer1)

                for i in range(self.archer1.rows):
                    for j in range(self.archer1.cols):
                        if(within_bounds(i+self.archer1.posx, j + self.archer1.posy)):
                            self.grid[i+self.archer1.posx][j +
                                                           self.archer1.posy] = self.archer1.grid[i][j]
            archer_move_flag[0] = 1

        if(flag_7[0] == 1):
            for k in range(no_of_balloons[0]):

                self.b1 = bl_cl(
                    1, 1, bl_posx[k], bl_posy[k], bl_gl_vlx[k], bl_gl_vly[k])
                bl_list.append(self.b1)

                for i in range(self.b1.rows):
                    for j in range(self.b1.cols):
                        if(within_bounds(i+self.b1.posx, j + self.b1.posy)):
                            self.grid[i+self.b1.posx][j +
                                                      self.b1.posy] = self.b1.grid[i][j]
            bl_move_flag[0] = 1

        if(flag_bb[0] == 1):
            for k in range(no_of_barbs):
                self.barb_new = barb_cl(1, 1, barbs_posx[k], barbs_posy[k])

                barbs_list.append(self.barb_new)

                for i in range(self.barb_new.rows):
                    for j in range(self.barb_new.cols):
                        # if(within_bounds)
                        self.grid[i+self.barb_new.posx][j +
                                                        self.barb_new.posy] = self.barb_new.grid[i][j]

                # shoot bullets within the bounds of the grid
                bx = self.barb_new.rows-1+self.barb_new.posx
                by = self.barb_new.cols-12+self.barb_new.posy

        if(flag_bl[0] == 1):
            pass

    def check_king_collision(self):

        i = 0
        while(i < no_of_huts[0]):

            if(self.king.posy == huts[i].posy and self.king.posx == huts[i].posx):
                ab = input_to()
                if(ab == " "):
                    if(huts_life[i] <= 0):
                        self.grid[huts[i].posx][huts[i].posy] = background
                        del huts[i]

                        no_of_huts[0] -= 1
                        del hutx[i]
                        del huty[i]
                        # kscore += 15

                    else:
                        huts[i].life -= 1
                        huts_life[i] -= 1
                        # kscore += 10
            i += 1

    def check_king_townhall_coll(self):
        global th_life
        global kscore

        a = th_rows
        b = th_cols
        for i in range(th_rows):
            for j in range(th_cols):
                if(self.king.posx == i+th_posx and self.king.posy == j+th_posy):
                    if(input_to() == " "):

                        if(self.townH.life <= 0 or th_life[0] <= 0):
                            for i in range(th_rows):
                                for j in range(th_cols):

                                    self.grid[i+th_posx][j +
                                                         th_posy] = background

                                    kscore += 50

                        self.townH.life -= 1
                        th_life[0] -= 1

    def archer_collision(self):
        global no_of_walls

        self.find_shortest_dist()
        self.find_out_b()

        self.move_towards_x_y(True)

        # self.find_shortest_dist_backup()
        # self.move_towards_x_y_backup(True)
        for i in range(len(archers_list)):
            print(sht_dist)

            shortest_build_x[i] = 150
            shortest_build_y[i] = 150
            sht_dist[i] = 150
            sht_build_index[i] = 0
            is_townhall[i] = 0
            is_hut[i] = 0
            is_cannon[i] = 0
            is_wt[i] = 0

    def balloon_collision(self):

        self.find_shortest_dist_b()
        self.find_out_bb()

        self.bl_move_towards(True)

        for i in range(len(bl_list)):

            shortest_build_bx[i] = 150
            shortest_build_by[i] = 150
            sht_dist_b[i] = 150
            sht_build_index_b[i] = 0
            is_townhall_b[i] = 0
            is_hut_b[i] = 0
            is_cannon_b[i] = 0
            is_wt_b[i] = 0

    def find_shortest_dist(self):

        for j in range(len(archers_list)):
            i = 0

            while(i < len(buildings)):
                if(buildings[i].life >= 1):

                    dist = abs(archers_list[j].posy-building_py[i]) + \
                        abs(archers_list[j].posx-building_px[i])
                    if(dist <= sht_dist[j]):
                        sht_dist[j] = dist
                        sht_build_index[j] = i
                        shortest_build_x[j] = building_px[i]
                        shortest_build_y[j] = building_py[i]

                i += 1

    def find_shortest_dist_b(self):

        for j in range(len(bl_list)):

            if(len(cannons)+len(wizards) > 0):
                # if(th_life[0] >= 1):
                #     i = 1+no_of_huts[0]
                #     while(i < len(buildings)):
                #         if(buildings[i].life >= 1):

                #             dist = abs(bl_list[j].posy-building_py[i]) + \
                #                 abs(bl_list[j].posx-building_px[i])

                #             if(dist <= sht_dist_b[j]):
                #                 sht_dist_b[j] = dist
                #                 sht_build_index_b[j] = i
                #                 shortest_build_bx[j] = building_px[i]
                #                 shortest_build_by[j] = building_py[i]

                #         i += 1

                # else:
                #     i = no_of_huts[0]
                #     while(i < len(buildings)):
                #         if(buildings[i].life >= 1):

                #             dist = abs(bl_list[j].posy-building_py[i]) + \
                #                 abs(bl_list[j].posx-building_px[i])

                #             if(dist <= sht_dist_b[j]):
                #                 sht_dist_b[j] = dist
                #                 sht_build_index_b[j] = i
                #                 shortest_build_bx[j] = building_px[i]
                #                 shortest_build_by[j] = building_py[i]

                #         i += 1

                i = 1+no_of_huts[0]
                while(i < len(buildings)):
                    if(buildings[i].life >= 1):

                        dist = abs(bl_list[j].posy-building_py[i]) + \
                            abs(bl_list[j].posx-building_px[i])

                        if(dist <= sht_dist_b[j]):
                            sht_dist_b[j] = dist
                            sht_build_index_b[j] = i
                            shortest_build_bx[j] = building_px[i]
                            shortest_build_by[j] = building_py[i]

                    i += 1

            else:
                i = 0
                while(i < len(buildings)):
                    if(buildings[i].life >= 1):

                        dist = abs(bl_list[j].posy-building_py[i]) + \
                            abs(bl_list[j].posx-building_px[i])

                        if(dist <= sht_dist_b[j]):
                            sht_dist_b[j] = dist
                            sht_build_index_b[j] = i
                            shortest_build_bx[j] = building_px[i]
                            shortest_build_by[j] = building_py[i]

                    i += 1

    def find_shortest_dist_backup(self):

        for j in range(len(archers_list)):
            i = 0
            while(i < len(huts)):
                dist = abs(archers_list[j].posy-huty[i]) + \
                    abs(archers_list[j].posx-hutx[i])

                if(dist <= sht_dist[j]):
                    sht_dist[j] = dist

                    sht_build_index[j] = i
                    shortest_build_x[j] = hutx[i]
                    shortest_build_y[j] = huty[i]

                i += 1

    def find_out_b(self):

        for i in range(len(archers_list)):

            if(sht_build_index[i] == 0):
                if(th_life[0] > 0):

                    is_townhall[i] = 1
                    is_hut[i] = -1
                    is_cannon[i] = -1
                    is_wt[i] = -1
                    return
                elif(len(huts) > 0):
                    hut_index[i] = 1
                    is_hut[i] = 1
                    is_cannon[i] = -1
                    is_wt[i] = -1
                    is_townhall[i] = -1

                elif(len(cannons) > 0):
                    cn_index[i] = 1
                    is_hut[i] = -1
                    is_cannon[i] = 1
                    is_wt[i] = -1
                    is_townhall[i] = -1

                elif(len(wizards) > 0):
                    is_hut[i] = -1
                    is_cannon[i] = -1
                    is_wt[i] = 1
                    is_townhall[i] = -1
                    wt_index[i] = 1
                    is_wt[i] = 1

            if(sht_build_index[i] >= 1):

                if(th_life[0] > 0):

                    if(len(huts) > 0 and sht_build_index[i] < len(huts)+1):
                        hut_index[i] = sht_build_index[i]
                        is_hut[i] = 1
                        is_cannon[i] = -1
                        is_wt[i] = -1
                        is_townhall[i] = -1
                    elif(len(cannons) > 0 and sht_build_index[i] < len(huts)+len(cannons)):

                        cn_index[i] = sht_build_index[i]-len(huts)-1

                        is_hut[i] = -1
                        is_cannon[i] = 1
                        is_wt[i] = -1
                        is_townhall[i] = -1

                    elif(len(wizards) > 0 and sht_build_index[i] < len(huts)+len(cannons)+len(wizards)):
                        wt_index[i] = sht_build_index[i] - \
                            len(huts)-len(cannons)-1

                        is_wt[i] = 1
                        is_hut[i] = -1
                        is_cannon[i] = -1
                        is_townhall[i] = -1

                elif(th_life[0] <= 0):

                    if(len(huts) > 0 and sht_build_index[i] < len(huts)):
                        hut_index[i] = sht_build_index[i]
                        is_hut[i] = 1
                        is_wt[i] = -1
                        is_cannon[i] = -1
                        is_townhall[i] = -1
                    elif(len(cannons) > 0 and sht_build_index[i] < len(huts)+len(cannons)):

                        cn_index[i] = sht_build_index[i]-len(huts)

                        is_cannon[i] = 1
                        is_wt[i] = -1
                        is_hut[i] = -1
                        is_townhall[i] = -1

                    elif(len(wizards) > 0 and sht_build_index[i] < len(huts)+len(cannons)+len(wizards)):
                        wt_index[i] = sht_build_index[i]-len(huts)-len(cannons)
                        is_wt[i] = 1
                        is_hut[i] = -1
                        is_cannon[i] = -1
                        is_townhall[i] = -1

    def find_out_bb(self):

        for i in range(len(bl_list)):

            if(sht_build_index_b[i] == 0):
                if(th_life[0] > 0):

                    is_townhall_b[i] = 1
                    is_hut_b[i] = -1
                    is_cannon_b[i] = -1
                    is_wt_b[i] = -1

                elif(len(huts) > 0):
                    hut_index_b[i] = 0
                    is_hut_b[i] = 1
                    is_cannon_b[i] = -1
                    is_wt_b[i] = -1
                    is_townhall_b[i] = -1

                elif(len(cannons) > 0):
                    cn_index_b[i] = 0
                    is_hut_b[i] = -1
                    is_cannon_b[i] = 1
                    is_wt_b[i] = -1
                    is_townhall_b[i] = -1

                elif(len(wizards) > 0):
                    is_hut_b[i] = -1
                    is_cannon_b[i] = -1
                    is_wt_b[i] = 1
                    is_townhall_b[i] = -1
                    wt_index_b[i] = 0

            if(sht_build_index_b[i] >= 1):

                if(th_life[0] > 0):

                    if(len(huts) > 0 and sht_build_index_b[i] < len(huts)+1):
                        hut_index_b[i] = sht_build_index_b[i]
                        is_hut_b[i] = 1
                        is_cannon_b[i] = -1
                        is_wt_b[i] = -1
                        is_townhall_b[i] = -1
                    elif(len(cannons) > 0 and sht_build_index_b[i] < len(huts)+len(cannons)+1):

                        cn_index_b[i] = sht_build_index_b[i]-len(huts)-1

                        is_hut_b[i] = -1
                        is_cannon_b[i] = 1
                        is_wt_b[i] = -1
                        is_townhall_b[i] = -1

                    elif(len(wizards) > 0 and sht_build_index_b[i] < len(huts)+len(cannons)+len(wizards)+1):
                        wt_index_b[i] = sht_build_index_b[i] - \
                            len(huts)-len(cannons)-1

                        is_wt_b[i] = 1
                        is_hut_b[i] = -1
                        is_cannon_b[i] = -1
                        is_townhall_b[i] = -1

                elif(th_life[0] <= 0):

                    if(len(huts) > 0 and sht_build_index_b[i] < len(huts)):
                        hut_index_b[i] = sht_build_index_b[i]
                        is_hut_b[i] = 1
                        is_wt_b[i] = -1
                        is_cannon_b[i] = -1
                        is_townhall_b[i] = -1
                    elif(len(cannons) > 0 and sht_build_index_b[i] < len(huts)+len(cannons)):

                        cn_index_b[i] = sht_build_index_b[i]-len(huts)

                        is_cannon_b[i] = 1
                        is_wt_b[i] = -1
                        is_hut_b[i] = -1
                        is_townhall_b[i] = -1

                    elif(len(wizards) > 0 and sht_build_index_b[i] < len(huts)+len(cannons)+len(wizards)):
                        wt_index_b[i] = sht_build_index_b[i] - \
                            len(huts)-len(cannons)
                        is_wt_b[i] = 1
                        is_hut_b[i] = -1
                        is_cannon_b[i] = -1
                        is_townhall_b[i] = -1

    def move_towards_x_y(self, flag):
        print(sht_dist)

        if(flag == True):

            for i in range(len(archers_list)):

                if(sht_build_index[i] < len(buildings)):

                    if(archers_posx[i] + 1 < shortest_build_x[i]):

                        archers_posx[i] += ar_gl_vlx[i]
                        if(archers_posy[i] < shortest_build_y[i]):
                            archers_posy[i] += ar_gl_vly[i]

                        if(archers_posy[i] > shortest_build_y[i]):
                            archers_posy[i] -= ar_gl_vly[i]

                        if(abs(archers_posx[i] - shortest_build_x[i]) <= 2 and abs(archers_posy[i] - shortest_build_y[i]) <= 2):

                            print(sht_build_index[i])
                            if(buildings[sht_build_index[i]].life <= 1):
                                self.grid[building_px[i]
                                          ][building_py[i]] = background

                                del buildings[sht_build_index[i]]

                                if(is_townhall[i] == 1):
                                    th_life[i] = 0

                                if(is_hut[i] == 1):
                                    del huts[hut_index[i]]
                                    del hutx[hut_index[i]]
                                    del huty[hut_index[i]]

                                    no_of_huts[0] -= 1
                                if(is_cannon[i] == 1):

                                    del cannons[cn_index[i]]
                                    del can_px[cn_index[i]]
                                    del can_py[cn_index[i]]

                                    no_of_cannons[0] -= 1

                                if(is_wt[i] == 1):
                                    if(wt_index[i] < len(wizards)):
                                        del wizards[wt_index[i]]

                                        del wt_x[wt_index[i]]
                                        del wt_y[wt_index[i]]

                                        no_of_wt[0] -= 1

                            else:

                                if(is_townhall[i] == 1):
                                    th_life[0] -= 3

                                if(is_hut[i] == 1):

                                    huts_life[hut_index[i]] -= 3
                                    if(huts_life[hut_index[i]] <= 0):
                                        if(hut_index[i] < len(huts)):
                                            del huts[hut_index[i]]
                                            del hutx[i]
                                            del huty[i]

                                            no_of_huts[0] -= 1

                                if(is_cannon[i] == 1):
                                    cnn_life[cn_index[i]] -= 1
                                    if(cnn_life[cn_index[i]] <= 0):
                                        if(cn_index[i] < len(huts)):
                                            del cannons[cn_index[i]]
                                            del can_px[i]
                                            del can_py[i]

                                            no_of_cannons[0] -= 1

                                if(is_wt[i] == 1):
                                    wt_life[wt_index[i]] -= 1

                                building_life[i] -= 5

                    elif(archers_posx[i]-1 > shortest_build_x[i]):

                        archers_posx[i] -= ar_gl_vlx[i]
                        if(archers_posy[i] < shortest_build_y[i]):
                            archers_posy[i] += ar_gl_vly[i]

                        if(archers_posy[i] > shortest_build_y[i]):
                            archers_posy[i] -= ar_gl_vly[i]

                        if(abs(archers_posx[i] - shortest_build_x[i]) <= 2 and abs(archers_posy[i] - shortest_build_y[i]) <= 2):

                            if(buildings[sht_build_index[i]].life <= 1):

                                self.grid[building_px[i]
                                          ][building_py[i]] = background

                                del buildings[sht_build_index[i]]

                                if(is_townhall[i] == 1):

                                    th_life[i] = 0

                                if(is_hut[i] == 1):

                                    del huts[hut_index[i]]
                                    del hutx[hut_index[i]]
                                    del huty[hut_index[i]]
                                    no_of_huts[0] -= 1

                                if(is_cannon[i] == 1):
                                    del cannons[cn_index[i]]
                                    del can_px[cn_index[i]]
                                    del can_py[cn_index[i]]

                                    no_of_cannons[0] -= 1

                                if(is_wt[i] == 1):
                                    if(wt_index[i] < len(wizards)):
                                        del wizards[wt_index[i]]

                                        del wt_x[wt_index[i]]
                                        del wt_y[wt_index[i]]

                                        no_of_wt[0] -= 1

                            else:

                                if(is_townhall[i] == 1):
                                    th_life[0] -= 3

                                if(is_hut[i] == 1):
                                    huts_life[hut_index[i]] -= 3
                                    if(huts_life[hut_index[i]] <= 0):
                                        if(hut_index[i] < len(huts)):
                                            del huts[hut_index[i]]
                                            del hutx[i]
                                            del huty[i]

                                            no_of_huts[0] -= 1

                                if(is_cannon[i] == 1):
                                    cnn_life[cn_index[i]] -= 1
                                    if(cnn_life[cn_index[i]] <= 0):
                                        if(cn_index[i] < len(huts)):
                                            del cannons[cn_index[i]]
                                            del can_px[i]
                                            del can_py[i]

                                            no_of_cannons[0] -= 1

                                if(is_wt[i] == 1):
                                    wt_life[wt_index[i]] -= 1

                                building_life[i] -= 5

                    elif(archers_posy[i]+1 < shortest_build_y[i]):

                        archers_posy[i] += ar_gl_vly[i]

                        if(archers_posx[i] < shortest_build_x[i]):
                            archers_posx[i] += ar_gl_vlx[i]

                        if(archers_posx[i] > shortest_build_x[i]):
                            archers_posx[i] -= ar_gl_vlx[i]

                        if(abs(archers_posx[i] - shortest_build_x[i]) <= 2 and abs(archers_posy[i] - shortest_build_y[i]) <= 2):

                            if(buildings[sht_build_index[i]].life <= 1):

                                self.grid[building_px[i]
                                          ][building_py[i]] = background

                                del buildings[sht_build_index[i]]

                                if(is_townhall[i] == 1):
                                    th_life[i] = 0

                                if(is_hut[i] == 1):
                                    del huts[hut_index[i]]
                                    del hutx[hut_index[i]]
                                    del huty[hut_index[i]]

                                    no_of_huts[0] -= 1

                                if(is_cannon[i] == 1):
                                    del cannons[cn_index[i]]
                                    del can_px[cn_index[i]]
                                    del can_py[cn_index[i]]
                                    no_of_cannons[0] -= 1

                                if(is_wt[i] == 1):
                                    if(wt_index[i] < len(wizards)):
                                        del wizards[wt_index[i]]
                                        del wt_x[wt_index[i]]
                                        del wt_y[wt_index[i]]

                                        no_of_wt[0] -= 1

                            else:

                                if(is_townhall[i] == 1):
                                    th_life[0] -= 3

                                if(is_hut[i] == 1):
                                    huts_life[hut_index[i]] -= 3
                                    if(huts_life[hut_index[i]] <= 0):
                                        if(hut_index[i] < len(huts)):
                                            del huts[hut_index[i]]
                                            del hutx[i]
                                            del huty[i]

                                            no_of_huts[0] -= 1

                                if(is_cannon[i] == 1):
                                    cnn_life[cn_index[i]] -= 1
                                    if(cnn_life[cn_index[i]] <= 0):
                                        if(cn_index[i] < len(huts)):
                                            del cannons[cn_index[i]]
                                            del can_px[i]
                                            del can_py[i]

                                            no_of_cannons[0] -= 1

                                if(is_wt[i] == 1):
                                    wt_life[wt_index[i]] -= 1

                                building_life[i] -= 5

                    elif(archers_posy[i]-1 > shortest_build_y[i]):

                        archers_posy[i] -= ar_gl_vly[i]

                        if(archers_posx[i] < shortest_build_x[i]):
                            # ar_gl_vly[i] = 1
                            archers_posx[i] += ar_gl_vlx[i]

                        if(archers_posx[i] > shortest_build_x[i]):
                            # ar_gl_vly[i] = 1
                            archers_posx[i] -= ar_gl_vlx[i]

                        if(abs(archers_posx[i] - shortest_build_x[i]) <= 2 and abs(archers_posy[i] - shortest_build_y[i]) <= 2):

                            if(buildings[sht_build_index[i]].life <= 1):

                                self.grid[building_px[i]
                                          ][building_py[i]] = background

                                del buildings[sht_build_index[i]]

                                if(is_townhall[i] == 1):
                                    th_life[i] = 0

                                if(is_hut[i] == 1):
                                    del huts[hut_index[i]]
                                    del hutx[hut_index[i]]
                                    del huty[hut_index[i]]
                                    no_of_huts[0] -= 1

                                if(is_cannon[i] == 1):
                                    del cannons[cn_index[i]]
                                    del can_px[cn_index[i]]
                                    del can_py[cn_index[i]]
                                    no_of_cannons[0] -= 1

                                if(is_wt[i] == 1):
                                    if(wt_index[i] < len(wizards)):
                                        del wizards[wt_index[i]]
                                        del wt_x[wt_index[i]]
                                        del wt_y[wt_index[i]]
                                        no_of_wt[0] -= 1

                            else:

                                if(is_townhall[i] == 1):
                                    th_life[0] -= 3

                                if(is_hut[i] == 1):
                                    huts_life[hut_index[i]] -= 3
                                    if(huts_life[hut_index[i]] <= 0):
                                        if(hut_index[i] < len(huts)):
                                            del huts[hut_index[i]]
                                            del hutx[i]
                                            del huty[i]

                                            no_of_huts[0] -= 1

                                if(is_cannon[i] == 1):

                                    cnn_life[cn_index[i]] -= 1
                                    if(cnn_life[cn_index[i]] <= 0):
                                        if(cn_index[i] < len(huts)):
                                            del cannons[cn_index[i]]
                                            del can_px[i]
                                            del can_py[i]

                                            no_of_cannons[0] -= 1

                                if(is_wt[i] == 1):
                                    wt_life[wt_index[i]] -= 1

                                building_life[i] -= 5

    def bl_move_towards(self, flag):

        if(flag == True):

            for i in range(len(bl_list)):

                if(sht_build_index_b[i] < len(buildings)):

                    if(bl_posx[i] + 1 < shortest_build_bx[i]):

                        bl_posx[i] += bl_gl_vlx[i]
                        if(bl_posy[i] < shortest_build_by[i]):
                            bl_posy[i] += bl_gl_vly[i]

                        if(bl_posy[i] > shortest_build_by[i]):
                            # ar_gl_vly[i] = 1
                            bl_posy[i] -= bl_gl_vly[i]

                        # if(archers_posx[i] == shortest_build_x[i] and archers_posy[i] == shortest_build_y[i]):
                        if(abs(bl_posx[i] - shortest_build_bx[i]) <= 2 and abs(bl_posy[i] - shortest_build_by[i]) <= 2):

                            # for the faster archer the building will get deleted and for
                            # the slower archer it will now give an error
                            print(sht_build_index_b[i])
                            if(buildings[sht_build_index_b[i]].life <= 1):
                                self.grid[building_px[i]
                                          ][building_py[i]] = background

                                del buildings[sht_build_index_b[i]]

                                if(is_townhall_b[i] == 1):
                                    th_life[i] = 0

                                # if(build_index[sht_build_index[i]] >= 1 and build_index[sht_build_index[i]] <= 1+no_of_huts[0]):
                                if(is_hut_b[i] == 1):
                                    del huts[hut_index_b[i]]
                                    del hutx[hut_index_b[i]]
                                    del huty[hut_index_b[i]]

                                    no_of_huts[0] -= 1

                                # if(build_index[sht_build_index[i]] >= 1+no_of_huts[0] and build_index[sht_build_index[i]] < 1+no_of_huts[0]+no_of_cannons[0]):
                                if(is_cannon_b[i] == 1):
                                    del cannons[cn_index_b[i]]
                                    del can_px[cn_index_b[i]]
                                    del can_py[cn_index_b[i]]
                                    # huts_life[sht_build_index[i]-1] -= 3

                                    no_of_cannons[0] -= 1

                                if(is_wt_b[i] == 1):
                                    if(wt_index_b[i] < len(wizards)):
                                        del wizards[wt_index_b[i]]
                                        del wt_x[wt_index_b[i]]
                                        del wt_y[wt_index_b[i]]

                                        # huts_life[sht_build_index[i]-1] -= 3

                                        no_of_wt[0] -= 1

                            # if(build_index[sht_build_index[i]] >= 1+no_of_huts[0]+no_of_cannons[0] and build_index[sht_build_index[i]] < 1+no_of_huts[0]+no_of_cannons[0]+no_of_wt[0]):

                            else:

                                if(is_townhall_b[i] == 1):
                                    th_life[0] -= 3

                                if(is_hut_b[i] == 1):

                                    huts_life[hut_index_b[i]] -= 3
                                    if(huts_life[hut_index_b[i]] <= 0):
                                        if(hut_index_b[i] < len(huts)):
                                            del huts[hut_index_b[i]]
                                            del hutx[i]
                                            del huty[i]

                                            no_of_huts[0] -= 1

                                if(is_cannon_b[i] == 1):
                                    cnn_life[cn_index_b[i]] -= 1
                                    if(cnn_life[cn_index_b[i]] <= 0):
                                        if(cn_index_b[i] < len(huts)):
                                            del cannons[cn_index_b[i]]
                                            del can_px[i]
                                            del can_py[i]

                                            no_of_cannons[0] -= 1

                                if(is_wt_b[i] == 1):
                                    wt_life[wt_index_b[i]] -= 1

                                building_life[i] -= 5

                if(bl_posx[i] - 1 > shortest_build_bx[i]):

                    bl_posx[i] -= bl_gl_vlx[i]
                    if(bl_posy[i] < shortest_build_by[i]):
                        bl_posy[i] += bl_gl_vly[i]

                    if(bl_posy[i] > shortest_build_by[i]):
                        bl_posy[i] -= bl_gl_vly[i]

                    # if(archers_posx[i] == shortest_build_x[i] and archers_posy[i] == shortest_build_y[i]):
                    if(abs(bl_posx[i] - shortest_build_bx[i]) <= 2 and abs(bl_posy[i] - shortest_build_by[i]) <= 2):

                        print(sht_build_index_b[i])
                        if(buildings[sht_build_index_b[i]].life <= 1):
                            self.grid[building_px[i]
                                      ][building_py[i]] = background

                            del buildings[sht_build_index_b[i]]

                            if(is_townhall_b[i] == 1):
                                th_life[i] = 0

                            if(is_hut_b[i] == 1):
                                x = open("hut_track.txt", "a")
                                x.write("deleted "+str(hut_index_b[i]))
                                x.close()

                                del huts[hut_index_b[i]]
                                del hutx[hut_index_b[i]]
                                del huty[hut_index_b[i]]
                                no_of_huts[0] -= 1

                            # if(build_index[sht_build_index[i]] >= 1+no_of_huts[0] and build_index[sht_build_index[i]] < 1+no_of_huts[0]+no_of_cannons[0]):
                            if(is_cannon_b[i] == 1):
                                del cannons[cn_index_b[i]]
                                del can_px[cn_index_b[i]]
                                del can_py[cn_index_b[i]]

                                no_of_cannons[0] -= 1

                            if(is_wt_b[i] == 1):
                                if(wt_index_b[i] < len(wizards)):

                                    x = open("wiz.txt", "a")
                                    x.write("deleted "+str(wt_index_b[i]))
                                    x.close()
                                    del wizards[wt_index_b[i]]

                                    del wt_x[wt_index_b[i]]
                                    del wt_y[wt_index_b[i]]

                                    no_of_wt[0] -= 1

                        # if(build_index[sht_build_index[i]] >= 1+no_of_huts[0]+no_of_cannons[0] and build_index[sht_build_index[i]] < 1+no_of_huts[0]+no_of_cannons[0]+no_of_wt[0]):

                        else:

                            if(is_townhall_b[i] == 1):
                                th_life[0] -= 3

                            if(is_hut_b[i] == 1):
                                huts_life[hut_index_b[i]] -= 3
                                if(huts_life[hut_index_b[i]] <= 0):
                                    if(hut_index_b[i] < len(huts)):
                                        del huts[hut_index_b[i]]
                                        del hutx[i]
                                        del huty[i]

                                        no_of_huts[0] -= 1

                            if(is_cannon_b[i] == 1):
                                cnn_life[cn_index_b[i]] -= 1
                                if(cnn_life[cn_index_b[i]] <= 0):
                                    if(cn_index_b[i] < len(huts)):
                                        del cannons[cn_index_b[i]]
                                        del can_px[i]
                                        del can_py[i]

                                        no_of_cannons[0] -= 1

                            if(is_wt_b[i] == 1):
                                wt_life[wt_index_b[i]] -= 1

                            building_life[i] -= 5

                elif(bl_posy[i]+1 < shortest_build_by[i]):

                    bl_posy[i] += bl_gl_vly[i]

                    if(bl_posx[i] < shortest_build_bx[i]):
                        bl_posx[i] += bl_gl_vlx[i]

                    if(bl_posx[i] > shortest_build_bx[i]):
                        bl_posx[i] -= bl_gl_vlx[i]

                    # if(archers_posx[i] == shortest_build_x[i] and archers_posy[i] == shortest_build_y[i]):
                    if(abs(bl_posx[i] - shortest_build_bx[i]) <= 2 and abs(bl_posy[i] - shortest_build_by[i]) <= 2):
                        if(sht_build_index_b[i] < len(buildings)):
                            if(buildings[sht_build_index_b[i]].life <= 1):
                                self.grid[building_px[i]
                                          ][building_py[i]] = background

                                del buildings[sht_build_index_b[i]]

                                if(is_townhall_b[i] == 1):
                                    th_life[i] = 0

                                # if(build_index[sht_build_index[i]] >= 1 and build_index[sht_build_index[i]] <= 1+no_of_huts[0]):
                                if(is_hut_b[i] == 1):
                                    x = open("hut_track.txt", "a")
                                    x.write("deleted "+str(hut_index_b[i]))
                                    x.close()

                                    del huts[hut_index_b[i]]
                                    del hutx[hut_index_b[i]]
                                    del huty[hut_index_b[i]]
                                    no_of_huts[0] -= 1

                                # if(build_index[sht_build_index[i]] >= 1+no_of_huts[0] and build_index[sht_build_index[i]] < 1+no_of_huts[0]+no_of_cannons[0]):
                                if(is_cannon_b[i] == 1):
                                    del cannons[cn_index_b[i]]
                                    del can_px[cn_index_b[i]]
                                    del can_py[cn_index_b[i]]
                                    no_of_cannons[0] -= 1

                                if(is_wt_b[i] == 1):
                                    if(wt_index_b[i] < len(wizards)):

                                        del wizards[wt_index_b[i]]
                                        del wt_x[wt_index_b[i]]
                                        del wt_y[wt_index_b[i]]
                                        no_of_wt[0] -= 1

                            # if(build_index[sht_build_index[i]] >= 1+no_of_huts[0]+no_of_cannons[0] and build_index[sht_build_index[i]] < 1+no_of_huts[0]+no_of_cannons[0]+no_of_wt[0]):
                            #     no_of_wt[0] -= 1

                            else:

                                if(is_townhall_b[i] == 1):
                                    th_life[0] -= 3

                                if(is_hut_b[i] == 1):
                                    huts_life[hut_index_b[i]] -= 3
                                    if(huts_life[hut_index_b[i]] <= 0):
                                        if(hut_index_b[i] < len(huts)):
                                            del huts[hut_index_b[i]]
                                            del hutx[i]
                                            del huty[i]

                                            no_of_huts[0] -= 1

                                if(is_cannon_b[i] == 1):
                                    cnn_life[cn_index_b[i]] -= 1
                                    if(cnn_life[cn_index_b[i]] <= 0):
                                        if(cn_index_b[i] < len(huts)):
                                            del cannons[cn_index_b[i]]
                                            del can_px[i]
                                            del can_py[i]

                                            no_of_cannons[0] -= 1

                                if(is_wt_b[i] == 1):
                                    wt_life[wt_index_b[i]] -= 1

                                building_life[i] -= 5

                elif(bl_posy[i]-1 > shortest_build_by[i]):

                    bl_posy[i] -= bl_gl_vly[i]

                    if(bl_posx[i] < shortest_build_bx[i]):
                        bl_posx[i] += bl_gl_vlx[i]

                    if(bl_posx[i] > shortest_build_bx[i]):
                        bl_posx[i] -= bl_gl_vlx[i]

                    if(abs(bl_posx[i] - shortest_build_bx[i]) <= 2 and abs(bl_posy[i] - shortest_build_by[i]) <= 2):

                        if(buildings[sht_build_index_b[i]].life <= 1):
                            self.grid[building_px[i]
                                      ][building_py[i]] = background

                            del buildings[sht_build_index_b[i]]

                            if(is_townhall_b[i] == 1):
                                th_life[i] = 0

                            # if(build_index[sht_build_index[i]] >= 1 and build_index[sht_build_index[i]] <= 1+no_of_huts[0]):
                            if(is_hut_b[i] == 1):

                                del huts[hut_index_b[i]]
                                del hutx[hut_index_b[i]]
                                del huty[hut_index_b[i]]
                                no_of_huts[0] -= 1

                            # if(build_index[sht_build_index[i]] >= 1+no_of_huts[0] and build_index[sht_build_index[i]] < 1+no_of_huts[0]+no_of_cannons[0]):
                            #     no_of_cannons[0] -= 1
                            if(is_cannon_b[i] == 1):
                                del cannons[cn_index_b[i]]
                                del can_px[cn_index_b[i]]
                                del can_py[cn_index_b[i]]
                                no_of_cannons[0] -= 1

                            if(is_wt_b[i] == 1):
                                if(wt_index_b[i] < len(wizards)):
                                    del wizards[wt_index_b[i]]
                                    del wt_x[wt_index_b[i]]
                                    del wt_y[wt_index_b[i]]

                                    no_of_wt[0] -= 1

                        # if(build_index[sht_build_index[i]] >= 1+no_of_huts[0]+no_of_cannons[0] and build_index[sht_build_index[i]] < 1+no_of_huts[0]+no_of_cannons[0]+no_of_wt[0]):

                        else:

                            if(is_townhall_b[i] == 1):
                                th_life[0] -= 3

                            if(is_hut_b[i] == 1):
                                huts_life[hut_index_b[i]] -= 3
                                if(huts_life[hut_index_b[i]] <= 0):
                                    if(hut_index_b[i] < len(huts)):
                                        del huts[hut_index_b[i]]
                                        del hutx[i]
                                        del huty[i]

                                        no_of_huts[0] -= 1

                            if(is_cannon_b[i] == 1):
                                cnn_life[cn_index_b[i]] -= 1
                                if(cnn_life[cn_index_b[i]] <= 0):
                                    if(cn_index_b[i] < len(huts)):
                                        del cannons[cn_index_b[i]]
                                        del can_px[i]
                                        del can_py[i]

                                        no_of_cannons[0] -= 1

                            if(is_wt_b[i] == 1):
                                wt_life[wt_index_b[i]] -= 1

                            building_life[i] -= 5

    def archer_collision_backup(self):
        global no_of_huts
        global no_of_walls

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

    def calculate_aoe(self):

        if(up[0] == True):
            print("up is true")
            ax1 = queen_px[0]-(8+2)
            ax2 = queen_px[0]-(8+2)
            ax3 = queen_px[0]-(8-2)
            ax4 = queen_px[0]-(8-2)

            ay1 = queen_py[0]-2
            ay2 = queen_py[0]+2
            ay3 = queen_py[0]-2
            ay4 = queen_py[0]+2

            aoe[0][0] = ax1
            aoe[0][1] = ay1
            aoe[1][0] = ax2
            aoe[1][1] = ay2
            aoe[2][0] = ax3
            aoe[2][1] = ay3
            aoe[3][0] = ax4
            aoe[3][1] = ay4

        if(down[0] == True):
            print("down is true")

            ax1 = queen_px[0]+8-2
            ax2 = queen_px[0]+8-2
            ax3 = queen_px[0]+8+2
            ax4 = queen_px[0]+8+2

            ay1 = queen_py[0]-2
            ay2 = queen_py[0]+2
            ay3 = queen_py[0]-2
            ay4 = queen_py[0]+2

            aoe[0][0] = ax1
            aoe[0][1] = ay1
            aoe[1][0] = ax2
            aoe[1][1] = ay2
            aoe[2][0] = ax3
            aoe[2][1] = ay3
            aoe[3][0] = ax4
            aoe[3][1] = ay4

        if(left[0] == True):
            print("left is true")

            ax1 = queen_px[0]-2
            ax2 = queen_px[0]-2
            ax3 = queen_px[0]+2
            ax4 = queen_px[0]+2

            ay1 = queen_py[0]-8-2
            ay2 = queen_py[0]-8+2
            ay3 = queen_py[0]-8-2
            ay4 = queen_py[0]-8+2

            aoe[0][0] = ax1
            aoe[0][1] = ay1
            aoe[1][0] = ax2
            aoe[1][1] = ay2
            aoe[2][0] = ax3
            aoe[2][1] = ay3
            aoe[3][0] = ax4
            aoe[3][1] = ay4

        if(right[0] == True):
            print("right is true")

            ax1 = queen_px[0]-2
            ax2 = queen_px[0]-2
            ax3 = queen_px[0]+2
            ax4 = queen_px[0]+2

            ay1 = queen_py[0]-8-2
            ay2 = queen_py[0]-8+2
            ay3 = queen_py[0]-8-2
            ay4 = queen_py[0]-8+2

            aoe[0][0] = ax1
            aoe[0][1] = ay1
            aoe[1][0] = ax2
            aoe[1][1] = ay2
            aoe[2][0] = ax3
            aoe[2][1] = ay3
            aoe[3][0] = ax4
            aoe[3][1] = ay4

    def calculate_aoe_w(self):
        i = 0
        while(i < len(wizards)):

            x1 = wt_x[i]-2
            y1 = wt_y[i]-2

            x2 = wt_x[i]-2
            y2 = wt_y[i]+2

            x3 = wt_x[i]+2
            y3 = wt_y[i]-2

            x4 = wt_x[i]+2
            y4 = wt_y[i]+2

            wz_aoe[i] = [[x1, y1], [x2, y2], [x3, y3], [x4, y4]]

            i += 1

    def aoe_attack(self):

        i = 0
        while(i < len(huts)):

            if(hutx[i] <= aoe[2][0] and hutx[i] >= aoe[0][0] and huty[i] >= aoe[0][1] and huty[i] <= aoe[1][1]):

                if(huts_life[i] <= 1):
                    self.grid[huts[i].posx][huts[i].posy] = background
                    del huts[i]

                    no_of_huts[0] -= 1
                    del hutx[i]
                    del huty[i]
                    # kscore += 15

                else:
                    huts[i].life -= 5
                    huts_life[i] -= 5

            i += 1

        for i in range(th_rows):
            for j in range(th_cols):
                if(i+th_posx <= aoe[2][0] and i+th_posx >= aoe[0][0] and j+th_posy >= aoe[0][1] and j+th_posy <= aoe[1][1]):

                    if(th_life[0] > 0):
                        th_life[0] -= 5

        for i in range(no_of_cannons[0]):
            if(can_px[i] <= aoe[2][0] and can_px[i] >= aoe[0][0] and can_py[i] >= aoe[0][1] and can_py[i] <= aoe[1][1]):

                if(cnn_life[i] > 0):
                    cnn_life[i] -= 5

                else:
                    no_of_cannons[0] -= 1

                # if(cnn_life[0] <= 0):
                #     del cannons[i]
                #     del can_px[i]
                #     del can_py[i]

        for i in range(no_of_wt[0]):
            print("blehbleh\n")
            print(no_of_wt[0])
            print(wt_life)
            if(wt_x[i] <= aoe[2][0] and wt_x[i] >= aoe[0][0] and wt_y[i] >= aoe[0][1] and wt_y[i] <= aoe[1][1]):
                print("aaaah\n")
                if(wt_life[i] > 0):
                    wt_life[i] -= 5

                else:
                    no_of_wt[0] -= 1

        # check townhall loc

    def barb_coll_with_wall(self):
        global barbs_list

        for i in range(no_of_barbs):
            for j in range(no_of_walls):
                if(barbs_list[i].posx == walls[j].posx and barbs_list[i].posy == walls[j].posy):

                    walls[j].life -= 1
                    wall_lifes[j] -= 1
                    self.wall_list[j].life -= 1

                    if(wall_lifes[j] <= 0):
                        self.grid[walls[j].posx][walls[j].posy] = background
                        del walls[j]
                        del self.wall_list[j]
                        del wall_px[i]
                        del wall_py[i]
                        no_of_walls[0] -= 1

    def isvictory(self):
        huts_destroyed = 0
        townh_destroyed = 0
        ans = False

        for i in range(no_of_huts[0]):
            if(huts_life[i] <= 0):
                huts_destroyed = 1

        if(th_life[0] <= 0):
            townh_destroyed = 1
        # check toenhall

        if(townh_destroyed == 1 and huts_destroyed == 1):
            ans = True

        return ans

    def move_towards_x_y_backup(self, flag):

        if(flag == True):

            for i in range(len(archers_list)):

                if(archers_posx[i]+2 < shortest_build_x[i]):

                    archers_posx[i] += ar_gl_vlx[i]
                    if(archers_posy[i] < shortest_build_y[i]):
                        archers_posy[i] += ar_gl_vly[i]

                    if(archers_posy[i] > shortest_build_y[i]):
                        archers_posy[i] -= ar_gl_vly[i]

                    if(abs(archers_posx[i] - shortest_build_x[i]) <= 2 and abs(archers_posy[i] - shortest_build_y[i]) <= 2):

                        if(huts[sht_build_index[i]].life <= 1):

                            self.grid[hutx[i]][huty[i]] = background

                            del huts[sht_build_index[i]]

                            del hutx[sht_build_index[i]]
                            del huty[sht_build_index[i]]

                            no_of_huts[0] -= 1

                        else:
                            huts[sht_build_index[i]].life -= 3
                            huts_life[sht_build_index[i]] -= 3

                if(archers_posx[i]-2 > shortest_build_x[i]):
                    archers_posx[i] -= ar_gl_vlx[i]
                    if(archers_posy[i] < shortest_build_y[i]):
                        # ar_gl_vly[i] = 1
                        archers_posy[i] += ar_gl_vly[i]

                    if(archers_posy[i] > shortest_build_y[i]):
                        # ar_gl_vly[i] = 1
                        archers_posy[i] -= ar_gl_vly[i]

                    if(abs(archers_posx[i] - shortest_build_x[i]) <= 2 and abs(archers_posy[i] - shortest_build_y[i]) <= 2):

                        # dont move
                        if(huts_life[sht_build_index[i]] <= 1):
                            self.grid[huts[i].posx][huts[i].posy] = background
                            del huts[sht_build_index[i]]

                            del hutx[sht_build_index[i]]
                            del huty[sht_build_index[i]]

                            no_of_huts[0] -= 1

                            del huts_life[sht_build_index[i]]

                        else:
                            huts[sht_build_index[i]].life -= 3
                            huts_life[sht_build_index[i]] -= 3

                if(archers_posy[i]+2 < shortest_build_y[i]):

                    archers_posy[i] += ar_gl_vly[i]

                    if(archers_posx[i] < shortest_build_x[i]):
                        # ar_gl_vly[i] = 1
                        archers_posx[i] += ar_gl_vlx[i]

                    if(archers_posx[i] > shortest_build_x[i]):
                        # ar_gl_vly[i] = 1
                        archers_posx[i] -= ar_gl_vlx[i]
                    if(abs(archers_posx[i] - shortest_build_x[i]) <= 2 and abs(archers_posy[i] - shortest_build_y[i]) <= 2):

                        # dont move
                        if(huts_life[sht_build_index[i]] <= 1):
                            self.grid[huts[i].posx][huts[i].posy] = background
                            del huts[sht_build_index[i]]

                            del hutx[sht_build_index[i]]
                            del huty[sht_build_index[i]]

                            no_of_huts[0] -= 1

                            del huts_life[sht_build_index[i]]

                        else:
                            huts[sht_build_index[i]].life -= 3
                            huts_life[sht_build_index[i]] -= 3

                if(archers_posy[i]-2 > shortest_build_y[i]):

                    archers_posy[i] -= ar_gl_vly[i]

                    if(archers_posx[i] < shortest_build_x[i]):
                        # ar_gl_vly[i] = 1
                        archers_posx[i] += ar_gl_vlx[i]

                    if(archers_posx[i] > shortest_build_x[i]):
                        # ar_gl_vly[i] = 1
                        archers_posx[i] -= ar_gl_vlx[i]

                    if(abs(archers_posx[i] - shortest_build_x[i]) <= 2 and abs(archers_posy[i] - shortest_build_y[i]) <= 2):

                        if(huts_life[sht_build_index[i]] <= 1):
                            self.grid[huts[i].posx][huts[i].posy] = background
                            del huts[sht_build_index[i]]

                            del hutx[sht_build_index[i]]
                            del huty[sht_build_index[i]]

                            no_of_huts[0] -= 1

                            del huts_life[sht_build_index[i]]
                            # kscore += 15

                        else:
                            huts[sht_build_index[i]].life -= 3
                            huts_life[sht_build_index[i]] -= 3


def check_troop_wall_collision(grid):

    for i in range(len(troops_list)):
        left = troops_list[i].posy-1
        right = troops_list[i].posy+1
        # just change the troop position
        troops_list[i].posx -= 1


def check_wall_life(scene, grid):
    for wall in scene.wall_list:
        if(wall.life <= 0):
            grid[wall.posx][wall.posy] = background
            del wall


def check_barb_wall_collision(scene, grid):

    # decrease wall life
    # for each troop check each wall

    for i in range(len(barbs_list)):
        left = troops_list[i].posy-1
        right = troops_list[i].posy+1
        if(grid[left] == wall_col):
            for j in range(len(scene.wall_list)):
                if(scene.wall_list[j].posx == left):
                    # remove
                    grid[left] = background

                    # del wall_list[i]


# here list is common for the bullets troops and barb
def check_bounds(grid, list):
    for i in range(len(list)):
        if(within_bounds(list[i].posx, list[i].posy)):
            pass
        else:
            del list[i]
            grid[list[i].posx][list[i].posy] = background


def check_cannons():
    global king_health
    global king_life
    global cannons
    global king_px
    global king_py
    for i in range(len(cannons)):
        pcx = cannons[i].posx
        pcy = cannons[i].posy

        if(abs(king_px[0]-pcx)+abs(king_py[0]-pcy) <= 6):
            king_health[0] -= 1

        if(abs(queen_px[0]-pcx)+abs(queen_py[0]-pcy) <= 6):
            queen_health[0] -= 1

        for i in range(len(archers_list)):
            if(abs(archers_posx[i]-pcx)+abs(archers_posy[i]-pcy) <= 6):
                archers_health[i] -= 1


def wt_attack():

    i = -1
    attacked = 0
    while(i < len(wizards)):
        i += 1

        if(i < len(wizards)):

            for j in range(len(archers_list)):
                if(archers_posx[j] <= wz_aoe[i][2][0] and archers_posx[j] >= wz_aoe[i][0][0] and archers_posy[j] >= wz_aoe[i][0][1] and archers_posy[j] <= wz_aoe[i][1][1]):
                    archers_health[j] -= 10
                    attacked = 1

                    if(archers_health[j] <= 0):

                        del archers_posx[j]
                        del archers_posy[j]
                        del archers_list[j]

                    break

            if(queen_px[0] <= wz_aoe[i][2][0] and queen_px[0] >= wz_aoe[i][0][0] and queen_py[0] >= wz_aoe[i][0][1] and queen_py[0] <= wz_aoe[i][1][1]):
                queen_health[0] -= 5
                attacked = 1

                break

            if(king_px[0] <= wz_aoe[i][2][0] and king_px[0] >= wz_aoe[i][0][0] and king_py[0] >= wz_aoe[i][0][1] and king_py[0] <= wz_aoe[i][1][1]):
                king_health[0] -= 5
                attacked = 1

                break

            if(attacked == 1):
                break


def heal_spell():
    global troop_lives
    global king_health
    global king_life
    for i in range(no_of_troops):
        troop_lives[i] += 5
        king_health[0] += 10
        king_life[0] += 10


def rage_spell():

    for i in range(len(troops_list)):
        # tx.vel_x += 1
        tr_gl_vly[i] += 1
        ar_gl_vlx[i] += 1
        ar_gl_vly[i] += 1


def have_lost():
    pass
    # check king and troops
