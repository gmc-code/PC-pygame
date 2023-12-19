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
| It carries out 3 methods: **check_event**, **draw**, **update**.

| **check_event** checks for user interaction, including mosue and keyboard.
| In the starter code below it handles 3 ways to close the python program.

| **draw** prepares any objects such as rects and sprites to be drawn to the screen.
| In the starter code below it prepares to fills the screen surface with a solid colour.

| **update** is for updating the screen and the clock.
| In the starter code below it updates the screen and updates the clock.

.. code-block:: python

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


| Each part of the code above is explained below.


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

pg.display.set_caption()
-----------------------------------

| Use pg.display.set_caption to set the window caption that appears in the top left of the window.

.. py:method::  pygame.display.set_caption(title)
    
    | Change the name on the window.

| See: https://www.pygame.org/docs/ref/display.html#pygame.display.set_caption

----

pg.time.Clock()
--------------------

| Use pg.time.Clock() to set create a Clock object to control the game framerate.

.. py:method::  pygame.time.Clock()
    
    | Creates a new Clock object that can be used to track an amount of time. 
    | The clock also provides several functions to help control a game's framerate.

| See: https://www.pygame.org/docs/ref/time.html#pygame.time.Clock

----

clock.tick()
--------------------

| After using pg.time.Clock() to set create a Clock object called clock, delay the game.

.. py:method::  clock.tick(framerate=0)

    | Call if once per game loop (frame). 
    | If no argument is passed, it returns the milliseconds since the last call
    | If a framerate argument is passed, it will delay to keep the game running slower than the given ticks per second. 
    | By calling Clock.tick(60) once per frame, the program will never run at more than 60 frames per second.

| See: https://www.pygame.org/docs/ref/time.html#pygame.time.Clock.tick

----

check_event
-------------------
  
| ``check_event`` has starter code to make sure that exiting the game works well.
| The game can be exited by clicking the window close box or by pressing the **q** or **escape** buttons.

----

pg.event.get()
--------------------

| Use pg.event.get() to get the events for checking using actions.

.. py:method::  pygame.event.get()

    | get all the messages and remove them from the queue.

| See: https://www.pygame.org/docs/ref/event.html#pygame.event.get

----

event.type and event.key
--------------------------

| ``event.type == pg.QUIT`` responds to closing the window by clicking on the X button in the top right.
| ``event.type == pg.KEYDOWN`` responds to key presses.
| ``event.key == pg.K_ESCAPE`` is True if the escape key is pressed.
| ``event.key == pg.K_q`` is True if the "q" key is pressed.

| For lists of various event types see: https://www.pygame.org/docs/ref/event.html#pygame.event.get

----

pg.quit()
--------------------

| Use ``pg.quit()`` before exiting the program with ``sys.exit()``.

.. py:method::  pygame.quit()

    | Uninitialize all pygame modules that have previously been initialized. 
    | When the Python interpreter shuts down, this method is called regardless, 
    so the program should not need it, except to terminate the pygame resources and continue. 
    | It will not exit the program.

| See: https://www.pygame.org/docs/ref/pygame.html#pygame.quit

----

sys.exit()
--------------------

| Use ``sys.exit()`` to exit the python program.

.. py:method::  sys.exit()

    | Exit the program. Exit from python.

| See: https://docs.python.org/2/library/sys.html#sys.exit


----

update definition
------------------

| ``update`` has starter code to update the screen and update the clock.

----

pg.display.flip()
--------------------

.. py:method::  pygame.display.flip()

    | Update the full display Surface to the screen

| See: https://www.pygame.org/docs/ref/display.html#pygame.display.flip

----

draw definition
------------------

| ``draw`` has starter code to draw to the screen.

----

screen.fill()
-------------------------------

.. py:method::  fill(color, rect=None, special_flags=0)

    | Fill the Surface with a solid color. 
    | If no rect argument is given the entire Surface will be filled. 
    | The rect argument will limit the fill to a specific area.
    | The color argument can be either a RGB sequence, a RGBA sequence or a mapped color index. 
    | If using RGBA, the Alpha (A part of RGBA) is ignored unless the surface uses per pixel alpha (Surface has the SRCALPHA flag).

| See: https://www.pygame.org/docs/ref/surface.html?highlight=fill#pygame.Surface.fill



