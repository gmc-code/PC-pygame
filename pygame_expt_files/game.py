import sys

import pygame as pg


class Game:
    def __init__(self):
        pg.init()
        self.WINDOW_WIDTH = 1200
        self.WINDOW_HEIGHT = 800
        self.FPS = 60
        self.screen = pg.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
        pg.display.set_caption("My Game")
        self.clock = pg.time.Clock()
        self.running = False

    def check_event(self):
        for event in pg.event.get():
            if event.type == pg.QUIT:
                self.run = False
            elif event.type == pg.KEYDOWN:
                if event.key == pg.K_ESCAPE or event.key == pg.K_q:
                    self.running = False     

    def draw(self):
        self.screen.fill((170, 238, 187))

    def update(self):
        pg.display.flip()
        self.clock.tick(self.FPS)

    def run(self):
        self.running = True
        while self.running:
            self.check_event()
            self.draw()
            self.update()
        pg.quit()
        sys.exit()    
