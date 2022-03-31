import abc


class Player(abc.ABC):

    @abc.abstractmethod
    def make_move(self, board):
        pass


class AIPlayer(Player):

    def __init__(self):
        self._total_time_moved = 0

    def make_move(self, board):
        pass

    def __str__(self):
        return "AI Player"


class HumanPlayer(Player):

    def make_move(self, board):
        pass

    def __str__(self):
        return "Human Player"
