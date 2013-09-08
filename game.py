#! /usr/bin/env python2.7-32
#encoding: utf-8

import pygame
from locals import *

from sprites import SpriteBasic, AnimatedSprite
from level import Level


class Game (object):
    '''
        Classe principal responsavel em inicializar as variaveis do pygame
        Cria a screen e controlar o loop game
    '''
    
    def __init__ (self, size, display_name):
        pygame.init()
        self.clock = pygame.time.Clock()
        self.objects_in_scene = []
        self.done = False
        self.FPS = 60
        self.clock = pygame.time.Clock()
        self.playtime = 0
        self.screenrect = None
        self.allgroup = pygame.sprite.Group()
        self.initialization(size, display_name)

    def write(self, msg="pygame is cool"):
        myfont = pygame.font.SysFont("None", 32)
        mytext = myfont.render(msg, True, (0,0,0))
        mytext = mytext.convert_alpha()
        return mytext
    
    def initialization (self, size, display_name):
        self.size = size
        self.display_name = display_name
        self.screen (size, display_name)
        self.background = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        self.background = pygame.Surface((self.screen.get_width(), self.screen.get_height()))
        self.background.fill(DEFAULT_SCREEN_COLOR)     # fill white
        self.background = self.background.convert()  # jpg can not have transparency
        self.screen.blit(self.background, (0,0))     # blit background on screen (overwriting all)

    def events (self):
        for event in pygame.event.get(): # User did something
            if event.type == pygame.QUIT:
                self.done = True
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.done = True

    def main (self, level):
        self.level = level
        while self.done == False:
            self.events ()
            #Games Variables
            milliseconds = self.clock.tick(self.FPS)  # milliseconds passed since last frame
            seconds = milliseconds / 1000.0 # seconds passed since last frame (float)
            self.playtime += seconds

            #control update and Draw
            self.update (self.playtime)
            level.update(self.playtime)
            self.draw ()
            pygame.display.flip()
        pygame.quit()
    
    def screen (self, size, display_name):
        pygame.display.set_caption(display_name)
        self.screen = pygame.display.set_mode(size)
        self.screenrect = self.screen.get_rect()
        return self.screen
    
    def update (self, playtime):
        # Clear the screen and set the screen background
        self.screen.fill(DEFAULT_SCREEN_COLOR)
        self.allgroup.update(self.playtime)

    def draw (self):
        font = pygame.font.Font(None, 18)
        text = font.render("Tempo de Jogo: %s" % self.playtime,True, RED)
        self.screen.blit(text, [0,10])
        self.level.draw ()
        self.allgroup.clear(self.screen, self.background)
        self.allgroup.draw(self.screen)

if __name__ == '__main__':
    size = (800, 600)

    game = Game (size, "Hanter Monters")
    level = Level ("level0.text", [800, 600], game)
    sp = AnimatedSprite ([200, 200], "player.png", game)
    level.load_level ()
    game.main (level)
