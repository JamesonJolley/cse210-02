import os
import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point
from threading import Timer

from game.casting.score_board import board
from game.casting.gems_stone import stone,gems



FRAME_RATE = 12
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 15
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Robot Finds Kitten"
DATA_PATH = os.path.dirname(os.path.abspath(__file__)) + "/data/messages.txt"
WHITE = Color(255, 255, 255)
GEM_ARTIFACTS = 1
STONE_ARTIFACTS = 2


def main():
    
    # create the cast
    cast = Cast()
    
    # create the banner
    banner = board()
    banner.set_text(f"{banner.get_score()}")
    banner.set_font_size(FONT_SIZE)
    banner.set_color(WHITE)
    banner.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("banners", board)
    
    # create the robot
    x = int(MAX_X / 2)
    y = int(MAX_Y / 2)
    position = Point(x, y)

    robot = Actor()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    cast.add_actor("robots", robot)
    
    # create the artifacts
    def create_artifacts():
        

        for n in range(GEM_ARTIFACTS):
            
            

            x = random.randint(1, COLS - 1)
            y = 1
            position = Point(x, y)
            position = position.scale(CELL_SIZE)


            
            gem = gems()
            gem.set_font_size(FONT_SIZE)
            gem.set_position(position)
            
            cast.add_actor("gems", gem)

        for n in range(STONE_ARTIFACTS):
            
            

            x = random.randint(1, COLS - 1)
            y = 1
            position = Point(x, y)
            position = position.scale(CELL_SIZE)

            
            
            
            stones = stone()
            stones.set_font_size(FONT_SIZE)
            stones.set_position(position)
            
            cast.add_actor("stones", stones)
        Timer(1,create_artifacts).start()

    
    # start the game
    create_artifacts()
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)


if __name__ == "__main__":
    main()