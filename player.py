import pygame as pg
from pygame.math import Vector2 as vec2

class Player():

    def __init__(self, game, pos):
        self.game = game
        self.image = pg.Surface((60, 80))
        self.image.fill('#474787')
        self.rect = self.image.get_rect(center = pos)
        self.position = vec2(self.rect.center)
        self.move = vec2(0, 0)
        self.speed = 200

    def _input(self):
        keys = pg.key.get_pressed()
        self.move.x = int(keys[pg.K_d]) - int(keys[pg.K_a])
        self.move.y = int(keys[pg.K_s]) - int(keys[pg.K_w])
        if self.move.magnitude() > 0:
            self.move = self.move.normalize()

    def _move(self):
        self.position += self.move * self.speed * self.game.delta_time
        self.rect.center = round(self.position.x), round(self.position.y)

    def draw(self):
        self.game.game_surface.blit(self.image, self.rect)

    def update(self):
        self._input()
        self._move()
