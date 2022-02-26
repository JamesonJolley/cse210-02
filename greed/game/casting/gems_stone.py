from game.casting.actor import Actor
from game.shared.color import Color
class gems(Actor):
    def __init__(self):
        super().__init__()
        self._text = "A"
        self._color = Color(112,209,244)
        
class stone(Actor):
    def __init__(self):
        super().__init__()
        self._text = "@"
        self._color = Color(255,0,0)