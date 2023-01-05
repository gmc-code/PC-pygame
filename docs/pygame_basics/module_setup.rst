====================================================
Module setup
====================================================

| Pygame files are often organised into folders for images, sounds and separate code modules.
| A typical structure is below.

my_pygame_project/
* |
* ├── __main__.py
* |
* ├── assets/
* │   ├── sounds/
* │   │   └── .wav files
* │   └── sprites/
* │       └── .png files
* |
* ├── my_game/
* │   ├── game.py
* │   ├── player.py
* │   ├── sprites.py
* │   └── game_utils.py
* |
* └── requirements.txt

----

__main__.py
--------------

| The __main__.py file is the expected starting point.
| It can be run from within an IDE, such as VScode.
| It allows the folder name to be used to launch the project from the command line.

.. code-block:: 

    python my_pygame_project


| See: https://docs.python.org/3/library/__main__.html#main-py-in-python-packages
