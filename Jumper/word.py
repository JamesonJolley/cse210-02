# pip install Random-Word
# pip install pyyaml

from random_word import RandomWords




# this class is to generate words
class word_gen:

    def __init__(self):
        """this function creates an instace of an object
            self: this represents the object
            _word: this is a private attribute of the object
        """
        self._word = '' # creates the object.

    def get_word(self):
        """
        get_word returns a random word (string)
        args: self this has to be an object
        """
        self._word = RandomWords()
        return self._word.get_random_word()