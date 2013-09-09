#! /usr/bin/env python2.7-32
#encoding: utf-8

import os
import copy
import pygame


from locals import *
from collision import CollisionObject

class SpriteBasic (object):

    def __init__ (self, position, fsprite, game):
        '''
            Monta o objeto sprite sheet de forma que se eu quiser passar apenas o indix 
            do sprite ele deve me retornar apenas o sprite que eu selecionei.
        '''
        self.game = game
        self.image = pygame.image.load(os.path.join("data",fsprite))
        self.rect = self.image.get_rect()
        self.pos = [0, 0]
        self.speed = 4.5
        self.is_collider = True

    def update (self, playtime):
        raise NotImplemented


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


class AnimatedSprite (SpriteBasic, pygame.sprite.Sprite):
    
    def __init__ (self, position, fsprite, game):
        SpriteBasic.__init__(self, position, fsprite, game)
        self.game = game
        self.fsprite = fsprite
        self.pos = [0, 0]
        self.speed = 4.5
        # Track the time we started, and the time between updates.
        # Then we can figure out when we have to switch the image.
        self._start = pygame.time.get_ticks()
        self._delay = 1000 / game.FPS
        self._last_update = 0
        self._frame = 10
        
        self._images = load_sliced_sprites (32, 32, fsprite)
        self.image = self._images[self._frame]
        self.rect = self.image.get_rect ()
        self.centerx = position[0]
        self.centery = position[1]
        self.groups = game.allgroup
        pygame.sprite.Sprite.__init__(self, self.groups)


    def update(self, t):
        # Note that this doesn't work if it's been more that self._delay
        # time between calls to update(); we only update the image once
        # then, but it really should be updated twice.
        pressed = pygame.key.get_pressed()
        move_vector = (0, 0)
        for m in (move_map[key] for key in move_map if pressed[key]):
            #verificar a area que o personagem esta tentando ir
            area = self.game.screen.get_rect()
            nextMoveX = self.rect.centerx + m[0] * MOVE_SPEED
            nextMoveY = self.rect.centery + m[1] * MOVE_SPEED
            other_sprite = \
                self.game.get_sprite_in ((nextMoveX, nextMoveY))

            #criando uma copia para validar o possivel movimento futuro
            sprite = copy.copy(self)
            sprite.rect = pygame.Rect (nextMoveX, nextMoveY, 32, 32)
            if other_sprite and not CollisionObject.sprite_collision (sprite, other_sprite):
                self.rect.centerx = nextMoveX
                self.rect.centery = nextMoveY 

"""        if t - self._last_update > self._delay:
            self._frame += 1
            if self._frame >= len(self._images): self._frame = 0
            self.image = self._images[self._frame]
            self._last_update = t
"""
class Block (SpriteBasic, pygame.sprite.Sprite):
    '''
       Classe que representa os blocos, onde o personagem caminha
    '''
    
    
    SPRITEMAP = {
        0: "grass.png",
        1: "water.png",
        2: "stone.png",
        3: "sand.png",
    }

    BLOCKDEFAULT = "grass.png"
    COLLIDERS = [1, 2]
    
    def __init__ (self, position, int_type, is_collider, game):
        try:
            fsprite = Block.SPRITEMAP[int_type]
        except KeyError:
            fsprite = Block.BLOCKDEFAULT

        SpriteBasic.__init__(self, position, fsprite, game)
        self.is_collider = False
        if int_type in self.COLLIDERS:
            self.is_collider = True
        self.rect.x = position[0] * self.rect.w
        self.rect.y = position[1] * self.rect.h
        self.groups = game.blockgroup
        pygame.sprite.Sprite.__init__(self, self.groups)

    def update (self, playtime):
        pass
