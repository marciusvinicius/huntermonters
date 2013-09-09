#! /usr/bin/env python2.7-32
#encoding: utf-8

import pygame
from pygame.locals import *


class CollisionObject (object):
    '''
    Vamos fazer a collisao aconter

    '''
    @staticmethod
    def isPointInsideRect(x, y, rect):
        if (x >= rect.left) and (x <= rect.right) and (y >= rect.top) and (y <= rect.bottom):
            return True
        else:
            return False

    @staticmethod
    def sprite_collision (sprite, other_sprite):
        if sprite.is_collider == False or other_sprite.is_collider == False:
            return False

        rect = sprite.rect
        other_rect = other_sprite.rect

        for a, b in [(rect, other_rect), (other_rect, rect)]:
            if ((CollisionObject.isPointInsideRect(a.left, a.top, b)) or
                (CollisionObject.isPointInsideRect(a.left, a.bottom, b)) or
                (CollisionObject.isPointInsideRect(a.right, a.top, b)) or
                (CollisionObject.isPointInsideRect(a.right, a.bottom, b))):
                    return True
        return False