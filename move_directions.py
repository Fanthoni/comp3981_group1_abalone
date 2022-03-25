from enum import Enum


class MoveDirections(Enum):
    """
    Contains all possible movement directions in a hex grid.
    """
    NW = (1, 0)
    NE = (1, 1)
    W = (0, -1)
    E = (0, 1)
    SW = (-1, -1)
    SE = (-1, 0)