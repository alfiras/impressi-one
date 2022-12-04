import pygame as pg, sys
from config import Config
from helper import Helper

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
        self.fps = 0
        self.clock = pg.time.Clock()

        self.title = title
        self.show_fps = show_fps

        self._setup()
        self.setup()

    def _setup(self):
        pass

    def _draw(self):
        self.game_surface.fill('#40739e')
        self.default_surface.fill('#2f3640')
        self.default_surface.blit(self.game_surface, (0, 0))

    def _update(self):
        self.helper.change_title(f"{self.title} | ({int(self.fps)})" if self.show_fps else self.title)

    def _input(self):
        for evt in self.event:
            if evt.type == pg.QUIT or (evt.type == pg.KEYDOWN and evt.key == pg.K_ESCAPE):
                self.game_run = False

    def main_loop(self):
        while(self.game_run):
            self.event = pg.event.get()
            self.delta_time = self.clock.tick(self.config.SET_FPS) / 1000
            self.fps = self.clock.get_fps()
            self._input()

            self._update()
            self.update()

            self._draw()
            self.draw()

            pg.display.flip()

    def run(self):
        self.main_loop()

        pg.quit()
        sys.exit()

    def setup(self):
        pass

    def draw(self):
        pass

    def update(self):
        pass
