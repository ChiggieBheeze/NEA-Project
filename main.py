import pygame
from sprites import *
from config import *
import sys

class Game:
    #Class for the entire game
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((w_Width, w_Height))
        self.clock = pygame.time.Clock()
        #self.font = pygame.font.Font('Arial', 32)
        self.running = True

        self.character_spritesheet = spriteSheet('img/player.png')
        self.terrain_spritesheet = spriteSheet('img/terrain.png')
        self.floor_spritesheet = spriteSheet('img/floor.png')
        
        

    def new(self):
        # Used when starting a new game
        self.playing = True

        self.allSprites = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.wall = pygame.sprite.LayeredUpdates()

        self.createTilemap()
    
    def createTilemap(self):
        for i, row in enumerate(TileMap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "W":
                    Wall(self, j, i)
                if column == "P":
                    Player(self, j, i)

    def events(self):
        #Any events (inputs like keyboard press)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.playing = False
                self.running = False

    def update(self):
        #Used to refresh the screen constantly
        self.allSprites.update()

    def draw(self):
        #Display images
        self.screen.fill(BLACK)
        self.allSprites.draw(self.screen)
        self.clock.tick(FPS)
        pygame.display.update()

    def main (self):
        #Main Game Loop
        while self.playing:
            self.update()
            self.draw()
            self.events()
        self.running = False

    def gameEnd(self):
        #Used when the game ends/player dies
        pass

    def intro(self):
        #Used to help display cover/intro screen
        pass

