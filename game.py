import pygame as pg, sys
from config import Config
from helper import Helper

from player import Player
from levels.level1 import Level1

class Game():

    def __init__(self, title, show_fps = False):
        pg.init()
        self.config = Config()
        self.helper = Helper()
        self.default_surface = pg.display.set_mode(self.config.FULLSCREEN)
        self.game_surface = pg.Surface(self.config.FULLSCREEN)
        self.game_run = True
        self.event = None
        self.delta_time = 0
        self.tick_last_frame = 0
        self.clock = pg.time.Clock()
        self.fps = 0
        self.mouse_pos = (0, 0)
        self.title = title
        self.show_fps = show_fps

        self._setup()
        self.setup()

    def _setup(self):
        pass

    def _update(self):
        self.helper.change_title(f"{self.title} | ({int(self.fps)})" if self.show_fps else self.title)

    def _draw(self):
        self.game_surface.fill('#00d2d3')
        self.default_surface.fill('#2f3640')

    def _after_draw(self):
        self.default_surface.blit(self.game_surface, (0, 0))

    def _delta_time(self):
        tick = pg.time.get_ticks()
        self.delta_time = (tick - self.tick_last_frame) / 1000.0
        self.tick_last_frame = tick

    def _input(self):
        self.mouse_pos = pg.mouse.get_pos()
        for evt in self.event:
            if evt.type == pg.QUIT or (evt.type == pg.KEYDOWN and evt.key == pg.K_ESCAPE):
                self.game_run = False

    def main_loop(self):
        while(self.game_run):
            self.event = pg.event.get()
            self._delta_time()
            self.clock.tick(self.config.SET_FPS)
            self.fps = self.clock.get_fps()
            self._input()

            self._update()
            self.update()

            self._draw()
            self.draw()

            self._after_draw()
            self.before_flip()

            pg.display.flip()

    def run(self):
        self.main_loop()

        pg.quit()
        sys.exit()

    def setup(self):
        self.player = Player(self, self.config.HALFSCREEN)
        self.level1 = Level1(self)

    def update(self):
        self.level1.update()

    def draw(self):
        self.level1.draw()

    def before_flip(self):
        pass
