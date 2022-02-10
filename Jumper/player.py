

class player_1:
    def __init__(self):
        self.guesses = []
        self.playing = True
        

    def get_guesses(self):
        return self.guesses

    def set_guesses(self,set):
        self.guesses.append(set)

    def guess_letter(self):
        ## Will ask for a guess in the form of a letter if the player gives a number, a letter they've already guessed, or multiple letters the function will recur
        guess = input('guess a letter:')
        if guess in self.guesses:
            print('you allredy guessed that try again')
            self.guess_letter()
        elif guess.isnumeric():
            print(f'{guess} is a number try again')
            self.guess_letter()
        elif len(guess) > 1:
            print(f'{guess} is more than one letter try again')
            self.guess_letter()
        else:
            self.set_guesses(guess)
            return guess
    
    




    