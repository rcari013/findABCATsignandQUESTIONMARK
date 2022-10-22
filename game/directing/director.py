from cgitb import reset
from game.casting.actor import Actor
from game.casting.resetquestionmark import ResetQuestionMark
from game.casting.cast import Cast
import constants
import random
from game.shared.point import Point
class Director:
    """A person who directs the game. 
    
    The responsibility of a Director is to control the sequence of play.

    Attributes:
        _keyboard_service (KeyboardService): For getting directional input.
        _video_service (VideoService): For providing video output.
    """

    def __init__(self, keyboard_service, video_service):
        """Constructs a new Director using the specified keyboard and video services.
        
        Args:
            keyboard_service (KeyboardService): An instance of KeyboardService.
            video_service (VideoService): An instance of VideoService.
            game_score (int): Keeps track of the score
        """
        self._keyboard_service = keyboard_service
        self._video_service = video_service
        self._game_score = 500
        
        
    def start_game(self, cast):
        """Starts the game using the given cast. Runs the main game loop.

        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.open_window()
        while self._video_service.is_window_open():
            self._get_inputs(cast)
            self._do_updates(cast)
            self._do_outputs(cast)
        self._video_service.close_window()

    def _get_inputs(self, cast):
        """Gets directional input from the keyboard and applies it to the robot.
        
        Args:
            cast (Cast): The cast of actors.
        """
        robot = cast.get_first_actor("robots")
        
        velocity = self._keyboard_service.get_direction()
        robot.set_velocity(velocity)

      
    def _do_updates(self, cast):
        """Updates the robot's position and resolves any collisions with artifacts.
        
        Args:
            cast (Cast): The cast of actors.
        """
        score = cast.get_first_actor("scores")
        robot = cast.get_first_actor("robots")
        bullet = cast.get_actors("bullets")
        artifacts = cast.get_actors("artifacts")
        
        max_x = self._video_service.get_width()
        max_y = self._video_service.get_height()
        robot.move_next(max_x, max_y)
        
        #rules of the game
        for artifact in artifacts:
            artifact.move_next(max_x, max_y)
            
            random_number = random.randint(1, 2)
            random_number_2 = random.randint(1, 2)
            if robot.get_position().equals(artifact.get_position()):                
                if artifact.get_text() == "A":
                    self._game_score += artifact.get_points()
                elif artifact.get_text() == "B":
                    self._game_score += artifact.get_points()
                elif artifact.get_text() == "C":
                    self._game_score += artifact.get_points()
                elif artifact.get_text() == "a":
                    self._game_score += artifact.get_points()
                elif artifact.get_text() == "b":
                    self._game_score += artifact.get_points()
                elif artifact.get_text() == "c":
                    self._game_score += artifact.get_points()                    
                elif artifact.get_text() == "@" and random_number == 2:
                    self._game_score = self._game_score + 100
                elif artifact.get_text() == "@" and random_number != 2:
                    self._game_score = self._game_score - 80
                elif artifact.get_text() == "?" and random_number_2 == 1:
                    self._game_score = self._game_score + 20
                elif artifact.get_text() == "?" and random_number_2 == 2:
                    self._game_score = self._game_score - 5
               
                else:
                    self._game_score = self._game_score - 20
                    
                score.set_text(f"Score: {self._game_score}")                
                cast.reset_actor(artifact)
            if artifact.get_position().get_y() >= 585 and artifact.get_text() == "?":
                #polymorphism part
                obj_move = ResetQuestionMark(constants.COLS, constants.ROWS, constants.CELL_SIZE)
                obj_move.reset_actor(artifact)
                self._game_score = self._game_score - 5
                score.set_text(f"Score: {self._game_score}")

            elif artifact.get_position().get_y() >= max_y:
                cast.reset_actor(artifact)

            if self._game_score <= 0:
                x = int(constants.MAX_X / 2)
                y = int(constants.MAX_Y / 2)
                position = Point(x, y)
                message = Actor()
                message.set_text("Game Over!")
                message.set_position(position)
                cast.add_actor("messages", message)
                for artifact in artifacts:
                    artifact.set_color(constants.WHITE)

                
     

        
    def _do_outputs(self, cast):
        """Draws the actors on the screen.
        
        Args:
            cast (Cast): The cast of actors.
        """
        self._video_service.clear_buffer()
        actors = cast.get_all_actors()
        self._video_service.draw_actors(actors)
        self._video_service.flush_buffer()
