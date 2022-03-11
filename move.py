"""
Contains the various move classes.

NOTE: Abalone move types:
in-line: marbles are moved as a column
sidestep: marbles are moved sideways (only possible with 2-3 marbles)

Moves:
(Letter Value, Number Value)
(1, 1) Up and to the right
    Ex. B4 -> C5
(1, 0) Up and to the left
    Ex. B4 -> C4
(0, 1) To the right
    Ex. B4 -> B5
(0, -1) To the left
    Ex. B4 -> B3
(-1, 0) Down to the right
    Ex. B4 -> A4
(-1, -1) Down to the left
    Ex. B4 -> A3
"""

from abc import ABC


class Move(ABC):
    """
    Generic move class.

    Moves are Singleton callable objects that validate a move and return a list of changed board co-ordinates.
    """

    def __init__(self, marble_group, direction):
        self._marble_group = marble_group
        self._direction = direction

    @property
    def marble_group(self):
        return self._marble_group

    @property
    def direction(self):
        return self._direction

    def move(self, formation, board):
        """
        Method to be overridden depending on the type of move.

        :param board: a Board object
        :param formation: a Formation object (potentially) that carries the co-ordinate(s) of the marbles to be moved.
        :return: None
        """
        pass

    def validate(self, formation, board: dict):
        """
        Method to be overridden depending on the type of move.

        Each type of move will have its own validation criteria.

        :return: None
        """
        pass

    def __call__(self, formation, board):
        if self.validate(formation, board) is True:
            self.move(formation, board)

    def __str__(self):
        return f"Move marble: {self._marble_group}" \
               f"\nDirection: {self.direction}"


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


class SingleMove(Move):
    """
    Represents the movement of a single marble.
    """

    def __init__(self):
        super().__init__()
        pass

    def move(self, formation, board):
        pass

    def validate(self, formation, board):
        if board.get(formation[1]) == 0:
            return True
        else:
            return False
