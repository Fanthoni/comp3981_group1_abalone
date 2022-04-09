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
from move_directions import MoveDirections


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

    @staticmethod
    def from_string(move_string: str):
        """
        Takes a string input and converts it to a move object.

        Must be in the format: 'marbles,move_direction' with no spaces after the commas.
        eg. 'A1,A2,1,1'

        :param move_string: a string
        :return: a Move object
        """
        move_arr = move_string.split(',')
        direction_arr = move_arr[-2:]
        marble_group_arr = move_arr[:-2]

        marble_group = Move.get_marble_group_from_array(marble_group_arr)
        direction = Move.get_move_direction_from_array(direction_arr)

        return Move(marble_group, direction)

        # print("Direction", direction_arr)
        # print("Marble Group", marble_group_arr)

    @staticmethod
    def get_marble_group_from_array(arr):
        """
        Marble group, a list of tuples
        :param arr: array of string, ex: ['A1','A2']
        :return: a tuple
        """
        group = list()
        for tile in arr:
            new_tile = (tile[0], int(tile[1]))
            group.append(new_tile)
        return sorted(group)

    @staticmethod
    def get_move_direction_from_array(arr):
        """
        Return a MoveDirections enum from an array.

        :param arr: a 2 length array of integers between -1 and 1
        :return: a MoveDirections enum.
        """
        direction_arr = []
        for number in arr:
            direction_arr.append(int(number))
        direction_arr = tuple(direction_arr)

        for direction in MoveDirections:
            if direction.value == direction_arr:
                return direction

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
        return f"{self._marble_group} {self.direction.value}"


def main():
    move_string = "A1,B2,C3,0,-1"
    move = Move.from_string(move_string)
    print(move)


if __name__ == "__main__":
    main()