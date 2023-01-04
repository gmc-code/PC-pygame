====================================================
main file
====================================================

__main__.py
--------------

| The __main__.py file is the expected starting point.
| It can be run from within an IDE, such as VScode.
| It allows the folder name to be used to launch the project from the command line.

| The file content is very simple.
| It imports the module (such as **gamename** below) with the function or class that will run the game (**run_game** below).

.. code-block:: 

    from gamename import run_game

    if __name__ == '__main__':
        game = run_game()


