.. Hangman documentation master file, created by
   sphinx-quickstart on Sat Nov  6 02:07:27 2021.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Hangman's documentation!
===================================

.. warning:: This game is still in development. The code is horribly incomplete and the nowhere about finished. Expect massive bugs! |:sweat_smile:|

This is the documentation for the Hangman game that I have developed. Rules of hangman are pretty simple, we have all played this game when we were younger. 

`Click here <https://github.com/TheButcherOfBlaviken/hangman>`_  to view the full source code in my github repository. 

To read up how the whole thing works :ref:`click here <link_Explanation>`. If you want to install the console application vist the :ref:`Installation <link_Installation>` section.

.. _link_Explanation:

Explanation
-----------
The function first uses the :py:meth:`game.Hangman.generate_word()` to generate a word for the game. Next the static method :py:meth:`game.Hangman._word_analyzer()` is called to action. The analyzed word is then passed on to :py:meth:`game.Hangman.show_hint()` to show the hint to the player and some blank spaces where the word is going to be filled in eventually. Once the player makes an entry it is checked to see if the input is valid by :py:meth:`game.Hanagman._input_validator()`. 

    1. If ``invalid``, the player is informed that an invalid entry was made. 
    2. If ``valid``, the blanks are updated and the players are again shown the hint and updated situation using :py:meth:`game.Hangman.show_hint()`.

The game ends when the player finishes up all of his available chances or guesses the word correctly. At the end of the game the player is prompted to play the game another time. The player can choose to either replay to end it there.

Thanks for reaching the bottom of this documentation. x

Hope you play and enjoy the game! |:smiley|

.. _link_Installation:

Installation
-------------

.. toctree::
   :maxdepth: 2
   :caption: Contents:



Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

.. autoclass:: game.Hangman

.. automethod:: game.Hangman.generate_word()
.. automethod:: game.Hangman._word_analyzer()
.. automethod:: game.Hangman.show_hint()
.. automethod:: game.Hangman._hint_builder()
.. automethod:: game.Hangman.print_hint()
.. automethod:: game.Hangman._input_validator()
.. automethod:: game.Hangman._guess_matcher()
.. automethod:: game.Hangman._update_letters()
.. automethod:: game.Hangman.hangman()

Modules
======= 
  
.. autosummary::
   :toctree: generated

   game
