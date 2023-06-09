import pygame, sys
from setting import *

class Game: 
    def _init_(self)
        pygame.init()
        self.screen = pygame.display.set_mode ((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.display.set_caption('Sprout land')
        self.clock = pygame.time.clock()

    def run(self):
        while True:
            for event in pygame.event.get():
                if event.type == pygame.QUIT
