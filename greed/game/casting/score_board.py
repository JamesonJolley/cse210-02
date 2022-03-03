from game.casting.actor import Actor
##this is the 
class board(Actor):
    def __init__(self):
        super().__init__()
        self.score='100'

    def set_score(self,score):
        """updates the score 
        
            args(score) how much the score is rased"""
        self.score += score

    def get_score(self):
        """get the score"""
        return self.score


    
