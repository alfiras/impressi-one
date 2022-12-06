import pygame as pg

class Particle():

    def __init__(self, game, color = '#222f3e'):
        self.game = game
        self.color = color
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

    def draw_circle(self):
        for particle in self.particles:
            pg.draw.circle(self.game.game_surface, self.color, [int(particle['pos'][0]), int(particle['pos'][1])], int(particle['width']))

    def draw_rect(self):
        for particle in self.particles:
            rect = pg.Rect((int(particle['pos'][0]), int(particle['pos'][1])), (10, 10))
            pg.draw.rect(self.game.game_surface, self.color, rect, int(particle['width']))

    def update(self):
        for particle in self.particles:
            particle['pos'][0] += particle['multiplier'][0]
            particle['pos'][1] += particle['multiplier'][1]
            particle['width'] -= 0.01
            particle['multiplier'][1] += 0.15

            if particle['width'] <= 0:
                self.destroy(particle)

    def create_and_update(self, x, y, mx, my, w, color = None):
        if color and self.color != color:
            self.color = color
        self.create(x, y, mx, my, w)
        self.update()
