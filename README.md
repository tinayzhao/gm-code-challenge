# gm-code-challenge

This is a Tic-Tac-Toe game for the Giant Machines coding challenge. 

## Dev Environment
`python3 -m virtualenv venv` - creates virtual environment
`source venv/bin/activate` - activates venv
`pip3 install -r requirements.txt` - install requirements.txt
To test changes by running the game, run `python3 src/game.py`. 

To convert game.py into executable, run `pyinstaller -F src/game.py`
and game executable should be under `dist` directory.

## Instructions to Play Game
Run `./game` in command line to start game.

## Game Rules
This is a two-player game.
The rules are:
1. The game is played on a grid that's 3 squares by 3 squares.
2. First Player is X, second player is O. Players take turns marking empty squares by inputting position of the square (see diagram below).
3. The first player to get 3 of their marks in a row (up, down, across, or diagonally) is the winner.
4. When all 9 squares are full, the game is over. If no player has 3 marks in a row, the game ends in a tie.

Input positions:
```
 1 | 2 | 3
---+---+---
 4 | 5 | 6  
---+---+---
 7 | 8 | 9
```