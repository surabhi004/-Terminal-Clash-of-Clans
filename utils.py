from colorama import Fore, Back, Style


reset = "\033[0m"
background = Back.BLACK + Fore.GREEN+'.'+reset

troops_list = []
archers_list = []
barbs_list = []
bl_list = []

troop_col = Back.BLUE + Fore.BLACK+'T'+reset
barb_col = Back.RED + Fore.BLACK+'B'+reset


def print_listo_ar(list_ar):
    rows_l = len(list_ar)
    cols_l = len(list_ar[0])
    x = ''
    for i in range(rows_l):
        # print(list_ar[i])
        # print("", end="\n")
        # for j in range(cols_l):
        print(x.join(list_ar[i]))
        # print(Back.BLACK + Fore.WHITE+"ok1", end="")

        # print(Back.BLACK + Fore.WHITE+"ok1", end="")
    # print("\n")


in_ok = ""

scene_rows = 40
scene_cols = 150


def check_collision_with_wall(x, y):

    if(x >= scene_rows-1 or x <= 0 or y <= 0 or y >= scene_cols-1):
        return True
    else:
        return False


def within_bounds(x, y):
    if(x >= 0 and x < scene_rows and y >= 0 and y < scene_cols):
        return True
    else:
        return False


# def print_troops_pos():
#     for i in range(len(troops_list)):
#         print("troop-"+i)
#         print("posx-"+troops_list[i].posx)
#         print("posx-"+troops_list[i].posy)
