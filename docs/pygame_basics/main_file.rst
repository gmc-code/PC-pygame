====================================================
main file
====================================================

__main__.py
--------------

| The __main__.py file is the expected starting point; other coders will understand that it is the place to start.
| It can be run from within an IDE, such as VScode.
| It allows the folder name to be used to launch the project from the command line.
| e.g if the folder name for the project is my_game, then ``python my_game`` in the command line wil run the game.

| The __main__.py file content is very simple.
| It imports the module, **game** with the class that will run the game, **Game**.
| The **Game** class has a method, **run**, which carries out the game loop.

.. code-block:: python

    from game import Game


    if __name__ == '__main__':
        game = Game()
        game.run()


