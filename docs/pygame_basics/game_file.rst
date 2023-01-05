====================================================
game file
====================================================

Simple Game loop
-------------------

| The game loop has been organised in the **Game** class.

| The Game class is first called using ``game = Game()`` in the **__main__.py** file
| ``game = Game()`` calls the ``__init__`` method which initializes pygame, sets up the screen size, sets the frame per second and set up the clock.

| The simple game loop is called by ``game.run()``. 
| It has a **while True** loop.
| It carries out 3 methods: **draw**, **check_event**, **update**.


.. code-block:: python

    import sys

    import pygame as pg


    class Game:
        def __init__(self):
            pg.init()
            self.WINDOW_WIDTH = 1200
            self.WINDOW_HEIGHT = 800
            self.screen = pg.display.set_mode((self.WINDOW_WIDTH, self.WINDOW_HEIGHT))
            self.FPS = 60
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

        def update(self):
            pg.display.flip()
            self.clock.tick(self.FPS)

        def draw(self):
            self.screen.fill((170, 238, 187))

        def run(self):
            while True:
                self.draw()
                self.check_event()
                self.update()
                

----

pygame.init()
---------------

| Use pygame.init() for convenience, rather than initializing sperate pygame modules.

.. py:method::  pygame.init()
    
    | Initialize all imported pygame modules

| See: https://www.pygame.org/docs/ref/pygame.html#pygame.init

----

pygame.display.set_mode
------------------------

| Use pg.display.set_mode to set the window screen size.

.. py:method::  pygame.display.set_mode(size=(0, 0), flags=0, depth=0, display=0, vsync=0)
    
    | Initialize a window or screen for display
    | Returns a display Surface object.
    | If no size is passed or is set to (0, 0), the created Surface will have the same size as the current screen resolution. 

| See: https://www.pygame.org/docs/ref/display.html#pygame.display.set_mode

----

pg.time.Clock()
--------------------

| Use pg.time.Clock() to set create a Clock object to control the game framerate.

.. py:method::  pygame.time.Clock()
    
    | Creates a new Clock object that can be used to track an amount of time. 
    | The clock also provides several functions to help control a game's framerate.

| See: https://www.pygame.org/docs/ref/time.html#pygame.time.Clock

----

clock.tick
--------------------

| Use pg.time.Clock() to set create a Clock object to control the game framerate.

.. py:method::  clock.tick(framerate=0)

    | Call if once per game loop (frame). 
    | If no argument is passed, it returns the milliseconds since the last call
    | If a framerate argument is passed, it will delay to keep the game running slower than the given ticks per second. 
    | By calling Clock.tick(60) once per frame, the program will never run at more than 60 frames per second.

| See: https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick

----

