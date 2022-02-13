## Game Overview

Jumper is a game in which the player seeks to solve a puzzle by guessing the letters of a secret word one at a time.

## Game requirement

Jumper is played according to the following rules.

The puzzle is a secret word randomly chosen from a list.
The player guesses a letter in the puzzle.
If the guess is correct, the letter is revealed.
If the guess is incorrect, a line is cut on the player's parachute.
If the puzzle is solved the game is over.
If the player has no more parachute the game is over.

## Project Structure

---
The project files and folders are organized as follows:
```
root                    (project root folder)
+-- jumper                (source code for game)
  +-- game              (specific classes)
  +-- __main__.py       (program entry point)
  +-- parachute.py      
  +-- word.py           (word generator)
  +-- player
+-- README.md           (general info)
```

## Authors

* Nestor Rivera (riv21007@byui.edu)
* Jameson Jolley (jol21004@byui.edu)
* Omarlin Parra (omarlinp@byui.edu)


## Define classes and encapsulation:
start_game : this class will start the game, compute the answers of the user, and determine wether he won or lost. 
parachute : this class contains the different stages of the parachute with a method to display them. 
player_1: this class will the check the gueses of the user and make sure is not something that he has given before and is a valid answer. 
word_gen : this class represent the word generator. 
