import enum
import sys
import time

from abalone import Abalone
from board import Board, BoardTile
from heuristic import Heuristic


class InfiniteValues(enum.IntEnum):
    NEG_INF = sys.maxsize * -1
    POS_INF = sys.maxsize


class Search:
    def __init__(self):
        self.dict = {}

    def terminal_test(self):
        return False

    def ab_search(self, state):
        depth = 2
        value = self.max_value(state, InfiniteValues.NEG_INF, InfiniteValues.POS_INF, depth)
        print(self.dict.get(value))
        return value

    def max_value(self, state, alpha, beta, depth):
        if self.terminal_test() or depth == 0:
            return Heuristic.evaluate_board(state)

        groups = state.get_marble_groups(BoardTile.BLUE)
        valid_moves = state.generate_moves(groups)

        value = InfiniteValues.NEG_INF

        node_order = []

        for action in valid_moves:
            new_state = state.get_board_after_move(action)
            node_value = Heuristic.evaluate_board(new_state)

            node_order.append((node_value, action))

        node_order = sorted(node_order, key=lambda tup: tup[0], reverse=True)

        for node_value, action in node_order:
            new_state = state.get_board_after_move(action)
            temp = self.min_value(new_state, alpha, beta, depth - 1)
            value = max(value, temp)

            if depth == 2:
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

        node_order = []

        for action in valid_moves:
            new_state = state.get_board_after_move(action)
            node_value = Heuristic.evaluate_board(new_state)

            node_order.append((node_value, action))

        node_order = sorted(node_order, key=lambda tup: tup[0])

        for node_value, action in node_order:
            new_state = state.get_board_after_move(action)
            temp = self.max_value(new_state, alpha, beta, depth - 1)
            value = min(value, temp)

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

    ab_search = Search()

    t = time.time()
    ab_search.ab_search(board)
    t2 = time.time() - t
    print(t2)


if __name__ == "__main__":
    main()
