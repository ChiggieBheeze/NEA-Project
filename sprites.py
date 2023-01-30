import pygame
from config import *
import math
import random

class spriteSheet:
    def __init__(self, file):
        self.sheet = pygame.image.load(file).convert()

    def get_sprite(self, x, y, width, height):
        sprite = pygame.Surface([width, height])
        sprite.blit(self.sheet, (0,0), (x, y, width, height))
        sprite.set_colorkey(WHITE)
        return sprite

class Player(pygame.sprite.Sprite):
    #Player class contins attributes of the player
    def __init__(self, game, x, y):

        self.game = game
        self._layer = p_Layer
        self.groups = self.game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tile_size
        self.y = y * tile_size
        self.width = tile_size
        self.height = tile_size

        self.x_change = 0
        self.y_change = 0

        self.facing = 'down'
        self.animation_loop = 1

        self.image = self.game.character_spritesheet.get_sprite(0, 64, self.width, self.height)
                    

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y
    
    def update(self):
        self.movement()
        self.animate()

        self.rect.x += self.x_change
        self.collide('x')
        self.rect.y += self.y_change
        self.collide('y')

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            self.x_change -= p_Speed
            self.facing = 'left'
        if keys[pygame.K_d]:
            self.x_change += p_Speed
            self.facing = 'right'
        if keys[pygame.K_w]:
            self.y_change -= p_Speed
            self.facing = 'up'
        if keys[pygame.K_s]:
            self.y_change += p_Speed
            self.facing = 'down'

    def collide(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.wall, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
        
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.wall, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
    
    def animate(self):
        animations = [self.game.character_spritesheet.get_sprite(0, 64, self.width, self.height),
                      self.game.character_spritesheet.get_sprite(32, 64, self.width, self.height),
                      self.game.character_spritesheet.get_sprite(64, 64, self.width, self.height),
                      self.game.character_spritesheet.get_sprite(96, 64, self.width, self.height),
                      self.game.character_spritesheet.get_sprite(128, 64, self.width, self.height),
                      self.game.character_spritesheet.get_sprite(160, 64, self.width, self.height),
                      self.game.character_spritesheet.get_sprite(192, 64, self.width, self.height),
                      self.game.character_spritesheet.get_sprite(224, 64, self.width, self.height),
                      self.game.character_spritesheet.get_sprite(256, 64, self.width, self.height),
                      self.game.character_spritesheet.get_sprite(288, 64, self.width, self.height)]

        if self.y_change == 0:
            self.image = self.game.character_spritesheet.get_sprite(0, 64, self.width, self.height)
        else:
            self.image = animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 10:
                self.animation_loop = 1
        
        if self.x_change == 0:
            self.image = self.game.character_spritesheet.get_sprite(0, 64, self.width, self.height)
        else:
            self.image = animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 10:
                self.animation_loop = 1

class Wall(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = w_LAYER
        self.groups = self.game.allSprites, self.game.wall
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tile_size
        self.y = y * tile_size
        self.width = tile_size
        self.height = tile_size

        self.image = self.game.terrain_spritesheet.get_sprite(0, 64, self.width, self.height)


        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

class Ground(pygame.sprite.Sprite):
    def __init__(self, game, x, y):
        self.game = game
        self._layer = g_Layer
        self.groups = self.game.allSprites
        pygame.sprite.Sprite.__init__(self, self.groups)
        
        self.x = x * tile_size
        self.y = y * tile_size 
        self.width = tile_size
        self.height = tile_size

        self.image = self.game.floor_spritesheet.get_sprite(0, 0, self.width, self.height)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y


