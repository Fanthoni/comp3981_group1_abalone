"""
Contains the various move classes.

NOTE: Abalone move types:
in-line: marbles are moved as a column
sidestep: marbles are moved sideways (only possible with 2-3 marbles)
"""

from abc import ABC
import doctest


class Move(ABC):
    """
    Generic move class.

    Moves are Singleton callable objects that validate a move and return a list of changed board co-ordinates.
    """
    __instance = None

    def __init__(self):
        pass

    def move(self, formation, board):
        """
        Method to be overridden depending on the type of move.

        :param board: a Board object
        :param formation: a Formation object (potentially) that carries the co-ordinate(s) of the marbles to be moved.
        :return: None
        """
        pass

    def validate(self, formation, board):
        """
        Method to be overridden depending on the type of move.

        Each type of move will have its own validation criteria.

        :return: None
        """
        pass

    def __call__(self, formation, board):
        if self.validate(formation, board) is True:
            self.move(formation, board)


class TrioMove(Move):
    """
    Represents the movement of three marbles.
    """

    def __init__(self):
        super().__init__()
        pass

    def move(self, formation, board):
        pass

    def validate(self, formation, board):
        pass


class DuoMove(Move):
    """
    Represents the movement of two marbles.
    """

    def __init__(self):
        super().__init__()
        pass

    def move(self, formation, board):
        pass

    def validate(self, formation, board):
        pass