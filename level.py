#! /usr/bin/env python2.7-32
#encoding: utf-8

import pygame

class Level (object):

    def __init__ (self, file, map):
        self.grid = self.map(map[0], map[1])
        self._file = file

    def map (self, x, y):
        grid = []
        for row in range(x):
            grid.append([])
            for column in range(y):
                grid[row].append(0)
        return grid

    def load_level (self):
        file = open(os.path.join("data/levels", self.file))
        for line in file
            for row in list(self.grid):
                Block(row, line)
