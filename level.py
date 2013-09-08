#! /usr/bin/env python2.7-32
#encoding: utf-8

import os
import pygame
import pickle
import random

from sprites import Block

class Level (object):

    def __init__ (self, file, map, game):
        self.grid = self.map (map[0], map[1])
        self._file = file
        self.game = game
        self.groupblocks = pygame.sprite.Group ()

    def map (self, x, y):
        grid = []
        for row in range (x):
            grid.append ([])
            for column in range(y):
                grid[row].append(0)
        return grid

    def load_level (self):
        linha, coluna = (0, 0)
        try:
            file = open (os.path.join("data/levels", self._file))
        except IOError:
            self.build_word ()

        file = open (os.path.join("data/levels", self._file))
        grid = pickle.load (file)
        file.close ()
        for i, line in enumerate(grid):
            for j, row in enumerate(line):
                bl = Block([i, j], row, False, self.game)
                bl.group = self.groupblocks


    def build_word (self, w=100, h=100):
        grid = []
        
        for row in range (w):
            grid.append ([])
            for column in range (h):
                grid [row].append (random.randint(0, 1))
        file = open(os.path.join ("data/levels", self._file), 'w')
        pickle.dump (grid, file)
        file.close ()

    def update (self, playtime):
        pass

    def draw (self):
        self.groupblocks.clear(self.game.screen, self.game.background)
        self.groupblocks.draw (self.game.screen)


#
#Criar level usando o pickle tbm, ainda nao sei como vou fazer isso
#
#
#