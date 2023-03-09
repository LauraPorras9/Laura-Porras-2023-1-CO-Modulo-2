import random
import pygame
from dino_runner.components.power_ups.power_up import PoweUp
from dino_runner.utils.constants import HAMMER, HAMMER_TYPE, HEART, SWORD_TYPE

class Hammer(PoweUp):

    def __init__(self):
        super().__init__(HAMMER, HAMMER_TYPE)
