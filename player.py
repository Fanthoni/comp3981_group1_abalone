import abc


class Player(abc.ABC):

    def __init__(self, move_limit, turn_time_limit):
        self.move_remaining = move_limit
        self.turn_limit = turn_time_limit

    @abc.abstractmethod
    def make_move(self, board):
        pass


class AIPlayer(Player):

    def make_move(self, board):
        pass

    def __str__(self):
        return f"AI Player with {self.move_remaining} moves " \
               f"remaining and {self.turn_limit} seconds " \
               f"for each round"


class HumanPlayer(Player):

    def make_move(self, board):
        pass

    def __str__(self):
        return f"Human Player with {self.move_remaining} moves " \
               f"remaining and {self.turn_limit} seconds " \
               f"for each round"
