from player import player_1
from word import word_gen
from parachute import parachute
import sys
class start_game:
    def __init__(self):
        self.player = player_1()
        self.word = word_gen()
        self.lives = -1
        self.stage = parachute()
        self.run()

    def reveal(self,guesses,word,word_printed = ''):
        for _ in word:
            if _ in guesses:
                word_printed += _
            else:
                word_printed += '_'
        print(word_printed)
    
    def compute_guess(self,guess,word):
        if str(guess) not in word:
            try:
                self.lives += 1
                self.stage.display_parachute(self.lives)
            except KeyError:
                print('the game is over. you lost')
                sys.exit()

    def compute_win(self,word):
        counter = 0
        for _ in word:
            if _ in self.player.guesses:
                counter += 1
        if counter == len(word):
            self.player.playing = False
            print('you win')
        ##add soot functionalty
    def run(self):
        ##The puzzle is a secret word randomly chosen from a list.
        word = self.word.get_word()
          
        while self.player.playing:
                ##If the guess is correct, the letter is revealed.
            self.reveal(self.player.guesses,word)
                ##The player guesses a letter in the puzzle.
            guess = self.player.guess_letter()
                ##If the guess is incorrect, a line is cut on the player's parachute.
            self.compute_guess(guess,word)
                ##If the puzzle is solved the game is over.
                ##If the player has no more parachute the game is over.
            self.compute_win(word)



   


