import sys

import pygame as pg


class Game:
    def __init__(self):
        pg.init()
        self.WINDOW_WIDTH = 1200
        self.WINDOW_HEIGHT = 800
        self.FPS = 60
        self.screen = pg.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        self.clock = pg.time.Clock()

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                pg.quit()
                sys.exit()
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE or event.key == pg.K_q:
                    pg.quit()
                    sys.exit()

    def draw(self):
        self.screen.fill((170, 238, 187))

    def update(self):
        pg.display.flip()
        self.clock.tick(self.FPS)

    def run(self):
        while True:
            self.check_event()
            self.draw()
            self.update()
            
