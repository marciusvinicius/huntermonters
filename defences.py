#! /usr/bin/env python2.7-32
#encoding: utf-8

import game

class BasicDefence (game.BasicDrawableObject)

    def __init__ (self, game):
        game.objects_in_scene.add(self)

    def update (self, time):
        raise NotImplemented