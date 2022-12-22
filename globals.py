no_of_troops = 5
no_of_archers = []
no_of_archers.append(0)

no_of_archers_4 = []
no_of_archers_4.append(0)

no_of_archers_5 = []
no_of_archers_5.append(0)

no_of_balloons = []
no_of_balloons.append(0)
no_of_barbs = 5

total_archers = []
total_archers.append(6)

total_balloons = []
total_balloons.append(6)

total_huts = []
total_huts.append(10)

archers_posx = []
archers_posy = []

perm_archers_posx = []
perm_archers_posy = []


bl_posx = []
bl_posy = []

perm_bl_posx = []
perm_bl_posy = []

ar_gl_vlx = []
ar_gl_vly = []

archer_move_flag = []
archer_move_flag.append(0)

bl_gl_vlx = []
bl_gl_vly = []

bl_move_flag = []
bl_move_flag.append(0)

# king_posx = 4
# king_posy = 4

king_flag = []
king_flag.append(False)
queen_flag = []
queen_flag.append(False)


king_px = []
king_px.append(4)

king_py = []
king_py.append(4)

king_life = []
king_life.append(10)


queen_px = []
queen_px.append(8)

queen_py = []
queen_py.append(60)

queen_life = []
queen_life.append(50)

flag_t = []
flag_t.append(0)

# barbs spawn flag
flag_bb = []
flag_bb.append(0)

# balloons
flag_bl = []
flag_bl.append(0)

# flag for archer spawning

flag_4 = []
flag_4.append(0)

flag_5 = []
flag_5.append(0)

flag_7 = []
flag_7.append(0)

no_of_huts = []
no_of_huts.append(10)
huts = []
hutx = [10, 11, 10, 10, 20, 20, 24, 10, 13, 4]
# y==cols
huty = [50, 50, 51, 52, 50, 80, 80, 80, 82, 7]


perm_hutx = [10, 11, 10, 10, 20, 20, 24, 10, 13, 4]
# y==cols
perm_huty = [50, 50, 51, 52, 50, 80, 80, 80, 82, 7]


huts_life = []
perm_huts_life = []
for i in range(no_of_huts[0]):
    huts_life.append(5)
    perm_huts_life.append(5)


# huts_life = [3, 3, 3, 3, 3, 3, 3]
no_of_cannons = []
no_of_cannons.append(2)

can_px = [20, 20, 20, 15]
can_py = [100, 70, 30, 30]

perm_can_px = [20, 20, 20, 15]
perm_can_py = [100, 70, 30, 30]

cannons = []
# wizrd tower
no_of_wt = []
no_of_wt.append(2)

wt_life = []
perm_wt_life = []

# change this to 5 or 3 in the final code
for i in range(4):
    wt_life.append(1)
    perm_wt_life.append(1)

cnn_life = []
perm_cnn_life = []

for i in range(4):
    cnn_life.append(1)
    perm_cnn_life.append(1)


wz_aoe = [[], [], [], []]


wt_x = [9, 14, 14, 16]
wt_y = [95, 95, 100, 100]

perm_wt_x = [9, 14, 14, 16]
perm_wt_y = [95, 95, 100, 100]

wizards = []

walls = []
no_of_walls = []
no_of_walls.append(10)
wall_lifes = []
perm_wall_life = []

for i in range(no_of_walls[0]):
    wall_lifes.append(3)
    perm_wall_life.append(3)


spawns = 3
spawn_pts = []

kscore = []
kscore.append(0)

q_score = []
q_score.append(0)
king_health = []
king_health.append(2000)


queen_health = []
queen_health.append(100)

troop_lives = [10, 10, 10, 10, 10]


buildings = []
defence_builds = []
defence_build_index = []
normal_builds = []
build_index = []

building_px = []
building_py = []

building_life = []


hut_index = []
cn_index = []
wt_index = []
is_townhall = []

is_cannon = []

is_wt = []

is_hut = []

hut_index_b = []
cn_index_b = []
wt_index_b = []
is_townhall_b = []

is_cannon_b = []

is_wt_b = []

is_hut_b = []
archers_health = []
bl_health = []

for i in range(total_archers[0]):

    hut_index.append(-1)
    cn_index.append(-1)
    wt_index.append(-1)
    is_cannon.append(-1)
    is_townhall.append(-1)
    is_hut.append(-1)
    is_wt.append(-1)
    archers_health.append(20)


for i in range(total_balloons[0]):

    hut_index_b.append(-1)
    cn_index_b.append(-1)
    wt_index_b.append(-1)
    is_cannon_b.append(-1)
    is_townhall_b.append(-1)
    is_hut_b.append(-1)
    is_wt_b.append(-1)
    bl_health.append(20)

king_hit = []
queen_hit = []
king_hit.append(5)
queen_hit.append(5)


king_damage = []
queen_damage = []
king_damage.append(6)
queen_damage.append(4)
