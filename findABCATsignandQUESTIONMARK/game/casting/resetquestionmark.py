import random
import constants
from game.casting.cast import Cast
from game.shared.point import Point


class ResetQuestionMark(Cast):

    def reset_actor(self, actor):
        x = random.randint(1, self._cols - 1)
        y = random.randint(1, self._rows - 1)
        position = Point(x, y)
        position = position.scale(self._cell_size)
        actor.set_position(position)
