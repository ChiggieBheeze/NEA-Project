import pygame
from main import *


g = Game()
g.intro_screen()
g.new()
while g.running:
    g.main()
    g.gameEnd()

pygame.quit()
sys.exit()