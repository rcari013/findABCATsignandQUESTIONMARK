from game.casting.actor import Actor

# TODO: Implement the Artifact class here. Don't forget to inherit from Actor!
class Artifact(Actor):
    """A visible, moveable thing that participates in the game. 
    
    The responsibility of Artifact is to keep track of its points.

    Attributes:
        _points (int): The points to add to the score        
    """

    def __init__(self):
        """Constructs a new Artifact."""
        self._points = 20        

    def get_points(self):
        """Gets the artifact's points.
        
        Returns:
            points: The artifact's points.
        """
        return self._points

    def set_points(self, points):
        """Gets the artifact's points.
        
        Returns:
            points: The artifact's points.
        """
        return self._points
        