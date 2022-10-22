import random

from game.casting.actor import Actor
from game.casting.artifact import Artifact
from game.casting.cast import Cast

from game.directing.director import Director

from game.services.keyboard_service import KeyboardService
from game.services.video_service import VideoService

from game.shared.color import Color
from game.shared.point import Point
from game.casting.robot import Robot

FRAME_RATE = 18
MAX_X = 900
MAX_Y = 600
CELL_SIZE = 30
FONT_SIZE = 15
COLS = 60
ROWS = 40
CAPTION = "Find A-B-C-@-?"
WHITE = Color(255, 255, 255)
DEFAULT_ARTIFACTS = 100


def main():
    
    # create the cast
    cast = Cast(COLS, ROWS, CELL_SIZE)
    
    # create the score
    score = Actor()
    score.set_text("Score: 500")
    score.set_font_size(FONT_SIZE)
    score.set_color(WHITE)
    score.set_position(Point(CELL_SIZE, 0))
    cast.add_actor("scores", score)
    
    # create the robot Using pixels here, not the scaled position
    x = int(MAX_X / 2)
    y = int(MAX_Y - FONT_SIZE*2)
    position = Point(x, y)    

    

    robot = Robot()
    robot.set_text("#")
    robot.set_font_size(FONT_SIZE)
    robot.set_color(WHITE)
    robot.set_position(position)
    
    cast.add_actor("robots", robot)



    for n in range(DEFAULT_ARTIFACTS):

        text = chr(random.randint(33, 126))
        if text == "j" or text == "J":
            text = "?"
        elif text == "M" or text == "m":
            text = "A"
        elif text == "N" or text == "n":
            text = "B"
        elif text == "O" or text == "o":
            text = "C"
        elif text == "|" or text == "*":
            text = "@"

            
        x_for_artifacts = random.randint(1, COLS - 1)
        y_for_artifacts = random.randint(1, 3)
        

        position = Point(x_for_artifacts, y_for_artifacts)
        position = position.scale(CELL_SIZE)
        
        r = random.randint(0, 255)
        g = random.randint(0, 255)
        b = random.randint(0, 255)
        color = Color(r, g, b)        

        #Load an artifact
        artifact = Artifact()
        artifact.set_text(text)
        artifact.set_font_size(FONT_SIZE)
        artifact.set_color(color)
        artifact.set_position(position)
        speed = random.randint(1, 5)
        artifact.set_velocity(Point(0, speed))
              
        cast.add_actor("artifacts", artifact)

        x = int(MAX_X / 2)
        y = int(MAX_Y - FONT_SIZE*2)
        position = Point(x, y)

    
    # start the game
    keyboard_service = KeyboardService(CELL_SIZE)
    video_service = VideoService(CAPTION, MAX_X, MAX_Y, CELL_SIZE, FRAME_RATE)
    director = Director(keyboard_service, video_service)
    director.start_game(cast)
    
    
if __name__ == "__main__":
    main()