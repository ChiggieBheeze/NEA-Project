import pygame
from config import *
import math
import random

class Player(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = p_Layer
        self.groups = self.game.all.sprites
        pygame.sprite.Sprite.__init__(self, self.groups)