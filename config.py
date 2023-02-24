import pygame
#Screen size
w_Width = 1920
w_Height = 1080

#Frames per second
FPS = 60

#Size of tiles
tile_size = 32
tile_size2 = 16

#Colours
BLACK = (0, 0, 0)
RED = (255, 0, 0)
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)

#Layer of sprites
e_Layer = 4
p_Layer = 3
w_LAYER = 2
g_Layer = 1

#speed of the player
p_Speed = 2
e_Speed = 1

#The code for the layout of the tilemap
TileMap = [
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    'W..........E...........................W',
    'W......................................W',
    'WWWWWWWWWWWWWWWWWWWWW..................W',
    'W......................................W',
    'W.....E................................W',
    'W..................WWWWWWWWWWWWWWWWWWWWW',
    'W......................................W',
    'W..............E.......................W',
    'WWWWWWWWWWWWWWWWWWWWW..................W',
    'W....E..........................E......W',
    'W......................................W',
    'W..................WWWWWWWWWWWWWWWWWWWWW',
    'W......................................W',
    'W......................................W',
    'WWWWWWWWWWWWWWWWWWWWW..................W',
    'W......................................W',
    'W......................................W',
    'W..................WWWWWWWWWWWWWWWWWWWWW',
    'W......................................W',
    'W....................................P.W',
    'WWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWWW',
    #....................
]

#keys = pygame.key.get_pressed()
#any_button = [keys[pygame.K_KP_ENTER], keys[pygame.K_w], keys[pygame.K_s], keys[pygame.K_d], keys[pygame.K_a]]