from os import posix_fadvise
import colorama
from colorama import Fore, Back, Style
import numpy as np
import random
import time

from utils import *

bullets_b = []
bullets_t = []


class wall:
    def __init__(self, pos_x, pos_y, lifex):
        self.posx = pos_x
        self.posy = pos_y

        self.life = lifex


class bullet:
    def __init__(self, posx, posy):
        self.posx = posx
        self.posy = posy
        self.used = 0
