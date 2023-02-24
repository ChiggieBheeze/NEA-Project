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
        self.collideEnemies()

        self.rect.x += self.x_change
        self.collide('x')
        self.rect.y += self.y_change
        self.collide('y')

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        keys = pygame.key.get_pressed()
        if keys[pygame.K_a]:
            for sprite in self.game.allSprites:
                sprite.rect.x += p_Speed
            self.x_change -= p_Speed
            self.facing = 'left'
        if keys[pygame.K_d]:
            for sprite in self.game.allSprites:
                sprite.rect.x -= p_Speed
            self.x_change += p_Speed
            self.facing = 'right'
        if keys[pygame.K_w]:
            for sprite in self.game.allSprites:
                sprite.rect.y += p_Speed
            self.y_change -= p_Speed
            self.facing = 'up'
        if keys[pygame.K_s]:
            for sprite in self.game.allSprites:
                sprite.rect.y -= p_Speed
            self.y_change += p_Speed
            self.facing = 'down'
        
    
    def collideEnemies(self):
        hits = pygame.sprite.spritecollide(self, self.game.enemies, False)
        if hits:
            self.kill()
            self.game.playing = False

    def collide(self, direction):
        if direction == "x":
            hits = pygame.sprite.spritecollide(self, self.game.wall, False)
            if hits:
                if self.x_change > 0:
                    self.rect.x = hits[0].rect.left - self.rect.width
                    for sprite in self.game.allSprites:
                        sprite.rect.x += p_Speed

                if self.x_change < 0:
                    self.rect.x = hits[0].rect.right
                    for sprite in self.game.allSprites:
                        sprite.rect.x -= p_Speed
        
        if direction == "y":
            hits = pygame.sprite.spritecollide(self, self.game.wall, False)
            if hits:
                if self.y_change > 0:
                    self.rect.y = hits[0].rect.top - self.rect.height
                    for sprite in self.game.allSprites:
                        sprite.rect.y += p_Speed
                if self.y_change < 0:
                    self.rect.y = hits[0].rect.bottom
                    for sprite in self.game.allSprites:
                        sprite.rect.y -= p_Speed
    
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

        if self.y_change == 0 and self.x_change == 0:
            self.image = self.game.character_spritesheet.get_sprite(0, 64, self.width, self.height)
        else:
            self.image = animations[math.floor(self.animation_loop)]
            self.animation_loop += 0.1
            if self.animation_loop >= 10:
                self.animation_loop = 1

class Enemy(pygame.sprite.Sprite):
    def __init__(self, game, x, y):

        self.game = game
        self._layer = e_Layer
        self.groups = self.game.allSprites, self.game.enemies
        pygame.sprite.Sprite.__init__(self, self.groups)

        self.x = x * tile_size
        self.y = y * tile_size
        self.width = 36
        self.height = 34

        self.x_change = 0
        self.y_change = 0

        self.facing = random.choice(['left', 'right'])
        self.animation_loop = 1
        self.movement_loop = 0
        self.max_travel = random.randint(7, 30)

        self.image = self.game.enemy_spritesheet.get_sprite(6, 112, self.width, self.height)
        self.image.set_colorkey(WHITE)

        self.rect = self.image.get_rect()
        self.rect.x = self.x
        self.rect.y = self.y

    def update(self):
        self.movement()
        self.animate()

        self.rect.x += self.x_change
        self.rect.y += self.y_change

        self.x_change = 0
        self.y_change = 0

    def movement(self):
        if self.facing == 'left':
            self.x_change -= e_Speed
            self.movement_loop -= 1
            if self.movement_loop <= -self.max_travel:
                self.facing = 'right'
            
        if self.facing == 'right':
            self.x_change += e_Speed
            self.movement_loop += 1
            if self.movement_loop >= self.max_travel:
                self.facing = 'left'

    def animate(self):
        animations = [self.game.enemy_spritesheet.get_sprite(6, 112, self.width, self.height),
                      self.game.enemy_spritesheet.get_sprite(54, 112, self.width, self.height),
                      self.game.enemy_spritesheet.get_sprite(100, 112, self.width, self.height),
                      self.game.enemy_spritesheet.get_sprite(148, 112, self.width, self.height),
                      self.game.enemy_spritesheet.get_sprite(196, 112, self.width, self.height),
                      self.game.enemy_spritesheet.get_sprite(246, 112, self.width, self.height),
                      self.game.enemy_spritesheet.get_sprite(294, 112, self.width, self.height),
                      self.game.enemy_spritesheet.get_sprite(344, 112, self.width, self.height),
                      self.game.enemy_spritesheet.get_sprite(390, 112, self.width, self.height),
                      self.game.enemy_spritesheet.get_sprite(438, 112, self.width, self.height)]

        if self.y_change == 0 and self.x_change == 0:
            self.image = self.game.enemy_spritesheet.get_sprite(6, 112, self.width, self.height)
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


class Button:
    def __init__(self, x, y, width, height, fg, bg, content, fontsize):
            self.font = pygame.font.Font('WildBreath.ttf', fontsize)
            self.content = content

            self.x = x
            self.y = y
            self.width = width
            self.height = height
            
            
            self.fg = fg
            self.bg = bg
            

            self.image = pygame.Surface((self.width, self.height))
            self.image.fill(self.bg)
            self.rect = self.image.get_rect()

            self.rect.x = self.x
            self.rect.y = self.y

            self.text = self.font.render(self.content, True, self.fg)
            self.text_rect = self.text.get_rect(center=(self.width/2, self.height/2))
            self.image.blit(self.text, self.text_rect)

    def is_pressed(self, pos, pressed):
        if self.rect.collidepoint(pos):
            if pressed[0]:
                return True
            return False
        return False
