import pygame as pg
from random import randint

class Particle():

    def __init__(self, game):
        self.game = game
        self.particles = []

    def create(self, x, y, mx, my, w):
        particle = {
           'pos': [x, y],
           'multiplier': [mx, my],
           'width': w,
        }
        self.particles.append(particle)

    def destroy(self, particle):
        self.particles.remove(particle)

    def update(self):
        for particle in self.particles:
            particle['pos'][0] += particle['multiplier'][0]
            particle['pos'][1] += particle['multiplier'][1]
            particle['width'] -= 0.1
            particle['multiplier'][1] += 0.15

            if particle['width'] <= 0:
                self.destroy(particle)

    def draw(self):
        for particle in self.particles:
            pg.draw.circle(self.game.game_surface, '#3d3d3d', (int(particle['pos'][0]), int(particle['pos'][1])), int(particle['width']))

    def create_and_update(self, x, y, mx, my, w):
        self.create(x, y, mx, my, w)
        self.update()

    def create_sample(self):
        self.create_and_update(self.game.mouse_pos[0], self.game.mouse_pos[1], (randint(0, 20) / 10 - 1), -5, randint(6, 11))
