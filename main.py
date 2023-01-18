import pygame
from sprites import *
from config import *
import sys

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((w_Width, w_Height))
        self.clock = pygame.time.Clock()
        self.font = pygame.font.Font('Arial', 32)
        self.running = True

def new(self):
    self.playing = True

    self.allSprites = pygame.sprite.LayeredUpdates()