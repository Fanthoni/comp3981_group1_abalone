import enum
import sys

from abalone import Abalone
from board import Board, BoardTile
from heuristic import Heuristic


class InfiniteValues(enum.IntEnum):
    NEG_INF = sys.maxsize * -1
    POS_INF = sys.maxsize


class Search:
    def __init__(self, state):
        self.state = state  # State is a board object
        self.dict = {}

        self.count = 0

    def terminal_test(self):
        return False

    def ab_search(self):
        depth = 3
        value = self.max_value(self.state, InfiniteValues.NEG_INF, InfiniteValues.POS_INF, depth)
        print(self.dict.get(value))
        return value

    def max_value(self, state, alpha, beta, depth):
        if self.terminal_test() or depth == 0:
            return Heuristic.evaluate_board(state)

        groups = state.get_marble_groups(BoardTile.BLUE)
        valid_moves = state.generate_moves(groups)

        value = InfiniteValues.NEG_INF

        for action in valid_moves:
            new_state = state.get_board_after_move(action)
            temp = self.min_value(new_state, alpha, beta, depth - 1)
            value = max(value, temp)

            self.dict[temp] = action

            if value > beta:
                return value
            alpha = max(alpha, value)
        return value

    def min_value(self, state, alpha, beta, depth):
        if self.terminal_test() or depth == 0:
            return Heuristic.evaluate_board(state)

        value = InfiniteValues.POS_INF

        groups = state.get_marble_groups(BoardTile.RED)
        valid_moves = state.generate_moves(groups)

        for action in valid_moves:
            new_state = state.get_board_after_move(action)
            value = min(value, self.max_value(new_state, alpha, beta, depth - 1))

            if value < alpha:
                return value
            beta = min(beta, value)
        return value

    def reset(self):
        self.dict = {}



def main():
    abalone = Abalone()
    abalone.setup_from_input_file("Test1.input")
    board = abalone.board
    board.print_board()

    ab_search = Search(board)
    ab_search.ab_search()

if __name__ == "__main__":
    main()
