import pygame
from sprites import *
from config import *
import sys
from pygame import mixer

class Game:
    #Class for the entire game
    def __init__(self):
        pygame.init()
        mixer.init()
        pygame.display.set_caption('Chalice Of Mind')
        self.screen = pygame.display.set_mode((w_Width, w_Height))
        self.clock = pygame.time.Clock()
        self.running = True
        self.font = pygame.font.Font('WildBreath.ttf', 32)
        

        self.character_spritesheet = spriteSheet('img/player.png')
        self.terrain_spritesheet = spriteSheet('img/terrain.png')
        self.floor_spritesheet = spriteSheet('img/floor.png')
        self.enemy_spritesheet = spriteSheet('img/enemy.png')
        self.intro_background = pygame.image.load('img/title.jpg')
        self.text_background = pygame.image.load('img/title2.jpg')
        self.endgame_screen = pygame.image.load('img/gameOver.jpg')

    def new(self):
        # Used when starting a new game
        self.playing = True

        self.allSprites = pygame.sprite.LayeredUpdates()
        self.players = pygame.sprite.LayeredUpdates()
        self.enemies = pygame.sprite.LayeredUpdates()
        self.wall = pygame.sprite.LayeredUpdates()

        self.createTilemap()

        mixer.music.load('music/rx.mp3')

        mixer.music.play()
    
    def createTilemap(self):
        for i, row in enumerate(TileMap):
            for j, column in enumerate(row):
                Ground(self, j, i)
                if column == "W":
                    Wall(self, j, i)
                if column == "P":
                    Player(self, j, i)
                if column == "E":
                    Enemy(self, j, i)

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

    def TurnBased(self):
        pass

    def gameEnd(self):
        #Used when the game ends/player dies
        restart_button = Button(1200, 720, 230, 65, RED, BLACK, 'RESTART', 64)
        quit_button = Button(1200, 820, 230, 65, RED, BLACK, 'QUIT', 64)

        for sprite in self.allSprites:
            sprite.kill()

        while self.running:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if restart_button.is_pressed(mouse_pos, mouse_pressed):
                self.new()
                self.main()
            if quit_button.is_pressed(mouse_pos, mouse_pressed):
                self.running = False

            self.screen.blit(self.endgame_screen, (0,0))
            self.screen.blit(restart_button.image, restart_button.rect)
            self.screen.blit(quit_button.image, quit_button.rect)
            mixer.music.stop()
            self.clock.tick(FPS)
            pygame.display.update()
        



    def intro_screen(self):
        #Used to help display cover/intro screen
        intro = True

        play_button = Button(900, 720, 130, 65, RED, BLACK, 'PLAY', 64)

        while intro:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    intro = False
                    self.running = False

            mouse_pos = pygame.mouse.get_pos()
            mouse_pressed = pygame.mouse.get_pressed()

            if play_button.is_pressed(mouse_pos, mouse_pressed):
                intro = False
            

            self.screen.blit(self.intro_background, (0,0))
            self.screen.blit(play_button.image, play_button.rect)
            self.clock.tick(FPS)
            pygame.display.update()
        
        
        


