import enum
import sys
import time

from board import Board, BoardTile
from heuristic import Heuristic


class InfiniteValues(enum.IntEnum):
    NEG_INF = sys.maxsize * -1
    POS_INF = sys.maxsize


class Depth(enum.IntEnum):
    COMPLETE = 0
    NODE_ORDERING_ACTIVATED = 2
    START = 2


class Search:
    def __init__(self):
        self.dict = {}

    def terminal_test(self, state):
        """
        Test to terminate recursion based on the scores of the game.

        To-do: Implement timer in the future
        """
        if state.red_score == 6 or state.blue_score == 6:
            return True
        return False

    def ab_search(self, state, current_player):
        """
        "Starter" for the alpha-beta search, includes variable represent depth searched by minimax.
        :param state: Board object
        """
        depth = 2  # If changing this value, change START value in Depth Enum to match
        if current_player == "Black":
            value = self.max_value(state, InfiniteValues.NEG_INF, InfiniteValues.POS_INF, depth)
        else:
            value = self.min_value(state, InfiniteValues.NEG_INF, InfiniteValues.POS_INF, depth)
        action = self.dict.get(value)
        self.reset()
        return action

    def max_value(self, state, alpha, beta, depth):
        """
        Alpha beta search for the maximum part.
        :param state: Board object
        :param alpha: Alpha value for minimax
        :param beta: Beta beta for minimax
        :param depth: depth used in depth iterative search
        """
        if self.terminal_test(state) or depth == Depth.COMPLETE:
            return Heuristic.evaluate_board(state)

        groups = state.get_marble_groups(BoardTile.BLUE)
        valid_moves = state.generate_moves(groups)

        value = InfiniteValues.NEG_INF

        if depth > Depth.NODE_ORDERING_ACTIVATED:  # Node ordering at certain depths, otherwise ordering takes too long
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

                if depth == Depth.START:
                    self.dict[temp] = action

                if value > beta:
                    return value
                alpha = max(alpha, value)
            return value
        else:
            for action in valid_moves:
                new_state = state.get_board_after_move(action)
                temp = self.min_value(new_state, alpha, beta, depth - 1)
                value = max(value, temp)

                if depth == Depth.START:
                    self.dict[temp] = action

                if value > beta:
                    return value
                alpha = max(alpha, value)
            return value

    def min_value(self, state, alpha, beta, depth):
        """
        Alpha beta search for the minimum part.
        :param state: Board object
        :param alpha: Alpha value for minimax
        :param beta: Beta beta for minimax
        :param depth: depth used in depth iterative search
        """
        if self.terminal_test(state) or depth == Depth.COMPLETE:
            return Heuristic.evaluate_board(state)

        value = InfiniteValues.POS_INF

        groups = state.get_marble_groups(BoardTile.RED)
        valid_moves = state.generate_moves(groups)

        if depth > Depth.NODE_ORDERING_ACTIVATED:
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

                if depth == Depth.START:
                    self.dict[temp] = action

                if value < alpha:
                    return value
                beta = min(beta, value)
            return value
        else:
            for action in valid_moves:
                new_state = state.get_board_after_move(action)
                temp = self.max_value(new_state, alpha, beta, depth - 1)
                value = min(value, temp)

                if depth == Depth.START:
                    self.dict[temp] = action

                if value < alpha:
                    return value
                beta = min(beta, value)
            return value

    def reset(self):
        """
        Resets stored actions after an action is returned.
        """
        self.dict = {}
