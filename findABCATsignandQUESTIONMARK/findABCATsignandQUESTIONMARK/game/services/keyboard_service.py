import constants
from game.casting.actor import Actor
import pyray
from game.shared.point import Point
from game.casting.cast import Cast

class KeyboardService:
    """Detects player input. 
    
    The responsibility of a KeyboardService is to detect player key presses and translate them into 
    a point representing a direction.

    Attributes:
        cell_size (int): For scaling directional input to a grid.
    """

    def __init__(self, cell_size = 1):
        """Constructs a new KeyboardService using the specified cell size.
        
        Args:
            cell_size (int): The size of a cell in the display grid.
        """
        self._cell_size = cell_size
        


    def get_direction(self):
        """Gets the selected direction based on the currently pressed keys.

        Returns:
            Point: The selected direction.
        """
        dx = 0
        dy = 0

        if pyray.is_key_down(pyray.KEY_A):
            dx = -1
        
        if pyray.is_key_down(pyray.KEY_D):
            dx = 1
        
        if pyray.is_key_down(pyray.KEY_W):
            dy = -1
        
        if pyray.is_key_down(pyray.KEY_S):
            dy = 1

        direction = Point(dx, dy)
        direction = direction.scale(self._cell_size)
        
        return direction
    
    def fire_the_bullet(self):

        if pyray.is_key_down(pyray.KEY_J):
            dy = -1

        
            