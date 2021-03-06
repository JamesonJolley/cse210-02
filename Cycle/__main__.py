import constants

from game.casting.cast import Cast
from game.casting.score import Score , Score_2
from game.casting.snake import Snake , snake_2
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction,ControlActorsAction_2
from game.scripting.move_actors_action import MoveActorsAction
from game.scripting.handle_collisions_action import HandleCollisionsAction
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point


def main():
    
    # create the cast
    cast = Cast()
    #cast.add_actor("foods", Food())
    cast.add_actor("snakes", Snake())
    #creaing the second snake :Omarlin
    cast.add_actor("snake2", snake_2())
    cast.add_actor("scores", Score())
    cast.add_actor('scores2', Score_2())
   
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    #adding the controls for the second snake :Omarlin
    script.add_action("input", ControlActorsAction_2(keyboard_service))
    
    script.add_action("update", MoveActorsAction())
    script.add_action("update", HandleCollisionsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)


if __name__ == "__main__":
    main()