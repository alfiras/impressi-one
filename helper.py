import pygame as pg
from pygame.math import Vector2

class Helper():

    def __init__(self):
        self.v2 = Vector2

    def change_title(self, title):
        pg.display.set_caption(title)
