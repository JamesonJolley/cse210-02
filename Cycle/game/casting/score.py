from game.casting.actor import Actor
import constants
from game.shared.point import Point

class Score(Actor):
    """
    A record of points made or lost. 
    
    The responsibility of Score is to keep track of the points the player has earned by eating food.
    It contains methods for adding and getting points. Client should use get_text() to get a string 
    representation of the points earned.

    Attributes:
        _points (int): The points earned in the game.
    """
    def __init__(self):
        super().__init__()
        self._points = 0
        self.add_points(0)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"player 1: {self._points}")

class Score_2(Score):
    def __init__(self):
        super().__init__()
        self._prepare()
    
    def _prepare(self):
        x = int(800)
        y = int(0)
        
        position = Point(x, y)
        self.set_position(position)

    def add_points(self, points):
        """Adds the given points to the score's total points.
        
        Args:
            points (int): The points to add.
        """
        self._points += points
        self.set_text(f"player 2: {self._points}")