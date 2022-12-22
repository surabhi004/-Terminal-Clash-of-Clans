import colorama
from colorama import Fore, Back, Style
import numpy as np

from king import *
from townhall import townhall_cl
from scenery import *
from input import *
from utils import *
from other import *
from globals import *

import subprocess as sp
import time
import sys
import os

colorama.init(autoreset=True)

flagg = 0
victory = False

level = 1

is_level1 = 1
is_level2 = 0
is_level3 = 0

l1_cannons = 2
l2_cannons = 3
l3_cannons = 4

l1_wt = 2
l2_wt = 3
l3_wt = 4

queen_max_life = 100
king_max_life = 100


def clear_sc():
    print(chr(27)+'[2j')
    print('\033c')
    print('\x1bc')


x = input("Press q to choose Queen and k to choose King\n")
if(x == "q"):
    queen_flag[0] = True
    print(queen_flag)
if(x == "k"):
    king_flag[0] = True


def move_b():
    global flagg
    flag_t[0] = 1
    if(flagg == 2):
        flagg = 0
    if(flagg == 1):
        flagg = 2
    if(troops_posy[i] >= scene_cols-1 and flagg == 0):
        troops_posy[i] += 1
        flagg = 1

    else:
        troops_posy[i] -= 1


def move_t():
    if(troops_posy[i] >= scene_cols-1 and flagg == 0):
        troops_posy[i] += 1
        flagg = 1

    else:
        troops_posy[i] -= 1


def move2():
    if(barbs_posy[i] < 0):
        print("barb collided with the left boundary")
    else:
        barbs_posy[i] = round(barbs_posy[i]-1)


no_of_cannons[0] = 2
no_of_wt[0] = 2


def health_bar_queen(barLength, barComplete, barMax, filled="|", unfilled="*", caps=("[", "]")):
    if queen_health[0] > 0:
        perComplete = int(barLength*queen_health[0]/barMax)
        print("QUEEN HEALTH")
        print(caps[0], end=""),
        print(filled*perComplete, end=""),
        print(unfilled*(barLength-perComplete), end=""),
        print(caps[1])
    else:
        print(caps[0], end=""),
        print("DEAD", end=""),
        print(caps[1])


def display_score_health():
    # clearConsole()

    # print('\033[H')
    print("LEVEL: "+str(level)+"\n")

    if(queen_flag[0] == True):
        health_bar_queen(20, queen_health[0], 100)

    if(king_flag[0] == True):
        health = king_health[0]
        print("health---           " + str(health) +
              "        score--"+str(kscore[0]))


def reset_level():
    king_health[0] = king_max_life
    king_life[0] = king_max_life
    queen_health[0] = queen_max_life
    queen_life[0] = queen_max_life

    hutx = perm_hutx
    huty = perm_huty
    wt_x = perm_wt_x
    wt_y = perm_wt_y
    can_px = perm_can_px
    can_py = perm_can_py

    huts_life = perm_huts_life
    cnn_life = perm_cnn_life
    wt_life = perm_wt_life
    wall_lifes = perm_wall_life


if __name__ == "__main__":

    while(1):
        scene = scenery(scene_rows, scene_cols)

        in_ok = input_to()
        print(in_ok)
        if(in_ok == "q"):
            break
        for i in range(no_of_troops):

            if(within_bounds(troops_posx[i], troops_posy[i]) == False):
                pass

            if(check_collision_with_wall(troops_posx[i], troops_posy[i])):
                pass

            if(in_ok == "t"):
                flag_t[0] = 1

                if(troops_posy[i] <= scene_cols-1):

                    troops_posy[i] -= 1

            if(troop_move_flag[0] == 1):
                troops_posy[i] -= tr_gl_vly[i]

        if(in_ok == "4"):
            flag_4[0] = 1
            if(no_of_archers[0] <= total_archers[0]):
                no_of_archers[0] += 1
                no_of_archers_4[0] += 1

                archers_posx.append(7)
                archers_posy.append(100)

                ar_gl_vlx.append(1)
                ar_gl_vly.append(1)

        if(in_ok == "5"):
            flag_5[0] = 1
            if(no_of_archers[0] <= total_archers[0]):

                no_of_archers[0] += 1
                no_of_archers_5[0] += 1

                archers_posx.append(25)
                archers_posy.append(100)

                ar_gl_vlx.append(1)
                ar_gl_vly.append(1)

        if(in_ok == "6"):
            flag_5[0] = 1
            if(no_of_archers[0] <= total_archers[0]):
                no_of_archers[0] += 1

                archers_posx.append(25)
                archers_posy.append(35)

                ar_gl_vlx.append(1)
                ar_gl_vly.append(1)

        if(in_ok == "7"):
            flag_7[0] = 1
            if(no_of_balloons[0] <= total_balloons[0]):
                bl_posx.append(25)
                bl_posy.append(70)

                bl_gl_vlx.append(1)
                bl_gl_vly.append(1)

                no_of_balloons[0] += 1

        if(in_ok == "8"):
            flag_7[0] = 1
            if(no_of_balloons[0] <= total_balloons[0]):
                bl_posx.append(25)
                bl_posy.append(35)

                bl_gl_vlx.append(1)
                bl_gl_vly.append(1)

                no_of_balloons[0] += 1

        if(in_ok == "9"):
            flag_7[0] = 1
            if(no_of_balloons[0] <= total_balloons[0]):
                bl_posx.append(6)
                bl_posy.append(70)

                bl_gl_vlx.append(1)
                bl_gl_vly.append(1)

                no_of_balloons[0] += 1

        if(in_ok == "b"):
            flag_bb[0] = 1

        if(in_ok == "j"):
            flag_bl[0] = 1

# -------------------------------------CHANGE THIS TO ACCOMAODATE ALL CONSDITIONS
        # for i in range(no_of_archers[0]):
        #     if(archer_move_flag[0] == 1):
        #         # troops_posy[i] -= troops_list[i].vel_x
        #         archers_posy[i] -= ar_gl_vly[i]

        if(in_ok == "h"):
            heal_spell()

        if(in_ok == "r"):
            rage_spell()

        if(king_flag[0] == True):

            if(in_ok == "w" or in_ok == 'W'):
                scene.king.move_up()
                # print(scene.king.posx)
            if(in_ok == "s" or in_ok == 'S'):
                scene.king.move_down()

            if(in_ok == "a" or in_ok == 'A'):
                scene.king.move_left()

            if(in_ok == "d" or in_ok == 'D'):
                scene.king.move_right()

        if(queen_flag[0] == True):

            if(in_ok == "w" or in_ok == 'W'):
                scene.queen.move_up()
                left[0] = False
                right[0] = False
                up[0] = True
                down[0] = False

            if(in_ok == "s" or in_ok == 'S'):
                scene.queen.move_down()

                left[0] = False
                right[0] = False
                up[0] = False
                down[0] = True

            if(in_ok == "a" or in_ok == 'A'):
                scene.queen.move_left()

                left[0] = True
                right[0] = False
                up[0] = False
                down[0] = False

            if(in_ok == "d" or in_ok == 'D'):
                scene.queen.move_right()

                left[0] = False
                right[0] = True
                up[0] = False
                down[0] = False

        # spawn troops
        if(in_ok == "p" or in_ok == 'P'):
            flag_t[0] = 1

        # scene.king.move_x()
        # print(king_posx)
        if(king_flag[0] == True):
            scene.check_king_collision()
            scene.check_king_townhall_coll()

        if(queen_flag[0] == True):
            scene.calculate_aoe()
            if(input_to() == " "):
                print("yesssss queeen")
                scene.aoe_attack()

        if(flag_4[0] == 1 or flag_5[0] == 1):
            if (no_of_huts[0] > 0):
                scene.archer_collision()

        if(flag_7[0] == 1):
            if (no_of_huts[0] > 0):
                scene.balloon_collision()

        scene.calculate_aoe_w()
        wt_attack()

        check_cannons()

        display_score_health()

        if(input_to() == "2"):
            level = 2
            is_level2 = 1

        if(input_to() == "3"):
            level = 3
            is_level3 = 1

        # if(level == 1):
        #     no_of_cannons[0] = 2
        #     no_of_wt[0] = 2

        # if(level == 1):
        #     print(no_of_cannons[0], no_of_wt[0], no_of_huts[0])
        #     if(no_of_cannons[0] <= 2 and no_of_wt[0] <= 0 and no_of_huts[0] <= 1 and th_life[0] <= 1):
        #         level = 2
        #         is_level2 = 1

        elif(level == 2):

            if(is_level2 == 1):

                no_of_cannons[0] = 3
                no_of_wt[0] = 3
                is_level2 = 0
                reset_level()

            if(no_of_cannons[0] <= 0 and no_of_wt[0] <= 0 and no_of_huts[0] <= 0 and th_life[0] <= 1):
                level = 3
                is_level3 = 1

        elif(level == 3):

            if(is_level3 == 1):

                no_of_cannons[0] = 4
                no_of_wt[0] = 4
                is_level3 = 0
                reset_level()

        print('\033[H')
        print("\n\n")

        if(scene.isvictory() == True and level == 3):
            print("YOU WON")
        # if(scene.lost() == True):
        #     print("YOU LOST")

        print_listo_ar(scene.grid)
        huts.clear()

        troops_list.clear()
        barbs_list.clear()
        archers_list.clear()
        buildings.clear()
        building_px.clear()
        building_py.clear()
        build_index.clear()
        cannons.clear()
        wizards.clear()
        bl_list.clear()

        if(victory == True):
            clear_sc()
            print('\033[H')

            print("YOU WON\n")
            break

        # print("End-------------------")
