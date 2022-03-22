import constants

from game.casting.cast import Cast
from game.casting.score import Score 
from game.scripting.script import Script
from game.scripting.control_actors_action import ControlActorsAction,ControlActorsAction_2
from game.scripting.move_actors_action import MoveActorsAction
from game.casting.actor import Actor
from game.scripting.draw_actors_action import DrawActorsAction
from game.directing.director import Director
from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService
from game.shared.color import Color
from game.shared.point import Point
from game.services.sound_service import Sound_service



def main():
    # just a test for now
    
    

    # create the cast
    cast = Cast()
    cast.sounds.play_sound('open')
    cast.add_actor("scores", Score())
    
    # start the game
    keyboard_service = KeyboardService()
    video_service = VideoService()

    script = Script()
    script.add_action("input", ControlActorsAction(keyboard_service))
    #adding the controls for the second snake :Omarlin
    script.add_action("input", ControlActorsAction_2(keyboard_service))
    
    script.add_action("update", MoveActorsAction())
    script.add_action("output", DrawActorsAction(video_service))
    
    director = Director(video_service)
    director.start_game(cast, script)

    




if __name__ == "__main__":
    main()