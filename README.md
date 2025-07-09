# Bishop B-8 Chess

It's a fun project to create an UCI chess engine (in other words it's a bot that is capable of playing chess).

The goal is not to make a Graphical User Interface, I'm only focusing on the logic to select the best moves.

To play against the engine you can select any Chess GUI that supports UCI chess Engine - UCI is the Universal Chess Interface protocol
that make things easy for everyone to implement their own engine while still having the same way of interacting with!
There is a list of Chess GUI on the Stockfish documentation: https://official-stockfish.github.io/docs/stockfish-wiki/Download-and-usage.html#download-a-chess-gui 
I personnaly use "En-croissant".


This engine project is actually made with python, it uses the module "chess" for managing the rules and legal moves and parsing position.
