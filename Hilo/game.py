##Hilo is played according to the following rules.

##The player starts the game with 300 points.
##Individual cards are represented as a number from 1 to 13.
##The current card is displayed.
##The player guesses if the next one will be higher or lower.
##The the next card is displayed.
##The player earns 100 points if they guessed correctly.
##The player loses 75 points if they guessed incorrectly.
##If a player reaches 0 points the game is over.
##If a player has more than 0 points they decide if they want to keep playing.
##If a player decides not to play again the game is over.
from player import player
import random

class Hilo:
    def __init__(self):
        self.player1 = player()
        ##cards[0] is the new card .cars[1] is the last card
        self.cards =lambda :[random.randrange(1,13),random.randrange(1,13)] 


    def loop(self):
        

        def keep_playing():
            answer = input('do you want to keep playing? (y/n)')
            if answer == 'n':
                self.player1.playing = False

        def guess():
                answer = input('will the next card be lower or higher or lower? respond with (h/l)')
                if answer == 'h':
                    return True
                else:
                    return False

        def guess_check(answer,cards):
            if answer == False:
                if cards[0] > cards[1]:
                    return True
                else:
                    return False
            else:
                if cards[0] < cards[1]:
                    return True
                else:
                    return False

        while self.player1.playing == True:
            if self.player1.loses(self.player1.points) == True:
                print('you lost all your points, game over')
                break
            ##The current card is displayed.
            cards = self.cards()
            print(f'points:{self.player1.points}')
            print(cards[0])
            
            ##The player guesses if the next one will be higher or lower.
            answer = guess()

            ##The the next card is displayed.
            print(cards[1])

            ##The player earns 100 points if they guessed correctly.
            ##The player loses 75 points if they guessed incorrectly.
            self.player1.earns = guess_check(answer,cards)
            self.player1.score()
            keep_playing()
            
            
