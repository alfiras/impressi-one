import pygame as pg

class Level1():

    def __init__(self, game):
        self.game = game

    def draw(self):
        self.game.player.draw()

    def update(self):
        self.game.player.update()
