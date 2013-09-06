#! /usr/bin/env python2.7-32
#encoding: utf-8

import os
import pygame

from locals import *


class SpriteBasic (pygame.sprite.Sprite):

    def __init__ (self, position, fsprite, game):
        '''
            Monta o objeto sprite sheet de forma que se eu quiser passar apenas o indix 
            do sprite ele deve me retornar apenas o sprite que eu selecionei.
        '''
        print "DSJHD"
        self.game = game
        self.image = pygame.image.load(os.path.join("data",fsprite))
        self.rect = pygame.Rect (position[0], position[1], 10, 10)
        self.pos = [0, 0]
        self.speed = 4.5
        self.groups = game.allgroup
        pygame.sprite.Sprite.__init__(self, self.groups)

    def update (self, playtime):
        pressed = pygame.key.get_pressed()
        move_vector = (0, 0)
        '''
            Change for state player
        '''
        for m in (move_map[key] for key in move_map if pressed[key]):
            area = self.game.screen.get_rect()
            self.rect.centerx += m[0] * self.speed
            self.rect.centery += m[1] * self.speed


def load_sliced_sprites(w, h, fsprite):
        '''
            Specs :
            Master can be any height.
            Sprites frames width must be the same width
            Master width must be len(frames)*frame.width
            Assuming you ressources directory is named "ressources"
            '''
        images = []
        master_image = pygame.image.load(
                                         os.path.join("data",fsprite)).convert_alpha()
        master_width, master_height = master_image.get_size()
        for i in xrange(int(master_width/w)):
            images.append(master_image.subsurface((i*w,0,w,h)))
        return images


class AnimatedSprite (SpriteBasic):
    
    def __init__ (self, position, fsprite, game):
        self.game = game
        self.fsprite = fsprite
        self.rect = pygame.Rect (position[0], position[1], 10, 10)
        self.pos = [0, 0]
        self.speed = 4.5
        self.groups = game.allgroup
        
        # Track the time we started, and the time between updates.
        # Then we can figure out when we have to switch the image.
        self._start = pygame.time.get_ticks()
        self._delay = 1000 / game.FPS
        self._last_update = 0
        self._frame = 0
        SpriteBasic.__init__(self, position, fsprite, game)
        self.image = load_sliced_sprites (16, 16, fsprite)


    def update(self, t):
        # Note that this doesn't work if it's been more that self._delay
        # time between calls to update(); we only update the image once
        # then, but it really should be updated twice.
        
        if t - self._last_update > self._delay:
            self._frame += 1
            if self._frame >= len(self._images): self._frame = 0
            self.image = self._images[self._frame]
            self._last_update = t

class Block (SpriteBasic):
    '''
       Classe que representa os blocos, onde o personagem caminha
    '''
    
    
    def __init__ (self, position, fsprite, is_collider, game):
        SpriteBasic.__init__(self, position, fsprite, game)
        self.is_collider = is_collider