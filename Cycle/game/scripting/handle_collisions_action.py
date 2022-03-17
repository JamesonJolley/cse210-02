import constants
from game.casting.actor import Actor
from game.scripting.action import Action
from game.shared.point import Point

class HandleCollisionsAction(Action):
    """
    An update action that handles interactions between the actors.
    
    The responsibility of HandleCollisionsAction is to handle the situation when the snake collides
    with the food, or the snake collides with its segments, or the game is over.

    Attributes:
        _is_game_over (boolean): Whether or not the game is over.
    """

    def __init__(self):
        """Constructs a new HandleCollisionsAction."""
        self._is_game_over = False
        self._player1_win = False
        self._player2_win = False

    def execute(self, cast, script):
        """Executes the handle collisions action.

        Args:
            cast (Cast): The cast of Actors in the game.
            script (Script): The script of Actions in the game.
        """
        if not self._is_game_over:
            self._handle_trail_collision(cast)
            self._handle_game_over(cast)
        
        if self._player1_win:
            snake2 = cast.get_first_actor("snake2")
            self._handle_color_change(snake2) 
            
        if self._player2_win:
            snake1 = cast.get_first_actor("snakes")
            self._handle_color_change(snake1)

    def _handle_trail_collision(self, cast):
        """Sets the game over flag if the snake collides with the segments from the other snake.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        snake1 = cast.get_first_actor("snakes")
        segments1 = snake1.get_segments()
        head1 = snake1.get_head()
        score1 = cast.get_first_actor("scores")

        snake2 = cast.get_first_actor("snake2")
        segments2 = snake2.get_segments()
        head2 = snake2.get_head()
        score2 = cast.get_first_actor("scores2")
        
        for seg1 in segments1:
            if head2.get_position().equals(seg1.get_position()):
                self._is_game_over = True
                self._player2_win = True
                score2.add_points(1)
                break


        for seg2 in segments2:
            if head1.get_position().equals(seg2.get_position()):
                self._is_game_over = True
                self._player1_win = True
                score1.add_points(1)
                break
        

    def _handle_game_over(self, cast):
        """Shows the 'game over' message and turns the snake and food white if the game is over.
        
        Args:
            cast (Cast): The cast of Actors in the game.
        """
        if self._is_game_over:
            snake = cast.get_first_actor("snakes")
            segments = snake.get_segments()
            food = cast.get_first_actor("foods")

            x = int(constants.MAX_X / 2)
            y = int(constants.MAX_Y / 2)
            position = Point(x, y)

            message = Actor()

            if self._player1_win:
                message.set_text(f"Game Over! player 1 wins")
            elif self._player2_win:
                message.set_text(f"Game Over! player 2 wins")
            else:
                 message.set_text(f"?")

            message.set_position(position)
            cast.add_actor("messages", message)

    def _handle_color_change(self,player,color = constants.WHITE):
        """handels the color change for the players
        
        Args:
            player (snake) : the players obj 
            color : the color that the segment will turn
        """
        for segments in player.get_segments():
            segments.set_color(color)


            