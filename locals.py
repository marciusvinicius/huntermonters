#! /usr/bin/env python2.7-32
#encoding: utf-8

import pygame

#Color

BLACK = (  0,  0,  0)
WHITE = (255,255,255)
BLUE =  (  0,  0,255)
GREEN = (  0,255,  0)
RED =   (255,  0,  0)
DEFAULT_SCREEN_COLOR = BLACK


move_map = {pygame.K_LEFT: (-1, 0),
    pygame.K_RIGHT: (1, 0),
    pygame.K_UP: (0, -1),
    pygame.K_DOWN: (0, 1)}