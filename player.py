##Hilo is played according to the following rules.

##The player starts the game with 300 points.
class player:
    def __init__(self):
        self.points = 300

        #for the game loop
        self.playing = True
        self.loses = lambda points : points == 0   

        ## fore losing and ggaining points
        self.earns = False 
        self.guess = 0


    def score(self):
        if self.earns == True:
            self.points += 100
        else:
            self.points -= 75




##Individual cards are represented as a number from 1 to 13.
##The current card is displayed.
##The player guesses if the next one will be higher or lower.
##The the next card is displayed.
##The player earns 100 points if they guessed correctly.
##The player loses 75 points if they guessed incorrectly.
##If a player reaches 0 points the game is over.
##If a player has more than 0 points they decide if they want to keep playing.
##If a player decides not to play again the game is over.