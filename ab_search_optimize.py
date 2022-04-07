import enum
import sys
import time
import datetime

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
        self.seconds_passed = 0
        self.is_paused = False
        self.past = None

    def terminal_test(self, state):
        """
        Test to terminate recursion based on the scores of the game.

        To-do: Implement timer in the future
        """
        if state.red_score == 6 or state.blue_score == 6:
            return True
        return False

    def ab_search(self, state: Board, current_player: str, heuristic: Heuristic):
        """
        "Starter" for the alpha-beta search, includes variable represent depth searched by minimax.
        :param state: Board object
        :param current_player: a String
        :param heuristic: a Heuristic object
        """
        self.past = time.time()
        depth = 4  # If changing this value, change START value in Depth Enum to match
        if current_player == "Black":
            value = self.max_value(state, InfiniteValues.NEG_INF, InfiniteValues.POS_INF, depth, heuristic)
        else:
            value = self.min_value(state, InfiniteValues.NEG_INF, InfiniteValues.POS_INF, depth, heuristic)
        action = self.dict.get(value)
        self.reset()
        return action

    @staticmethod
    def _order_nodes(state: Board, valid_moves: list, heuristic: Heuristic) -> list:
        """
        Helper function used to order nodes.

        :param state: a Board object
        :param valid_moves: a List of Move objects
        """
        ordered_nodes = []
        actions = []
        for action in valid_moves:
            new_state = state.get_board_after_move(action)
            node_value = heuristic.evaluate_board(new_state)

            ordered_nodes.append((node_value, action))
        ordered_nodes = sorted(ordered_nodes, key=lambda tup: tup[0], reverse=True)

        for node_value, action in ordered_nodes:
            actions.append(action)
        return actions

    def max_value(self, state: Board, alpha: int, beta: int, depth: int, heuristic: Heuristic) -> int:
        """
        Alpha beta search for the Max.

        :param state: Board object
        :param alpha: Alpha value for minimax
        :param beta: Beta value for minimax
        :param depth: depth used in depth iterative search
        :param heuristic: a Heuristic object
        """
        # Test for pause state; is so count time passes until un-paused
        start_time = time.time()
        while self.is_paused:
            time.sleep(1)
            self.seconds_passed += 1

        if self.terminal_test(state) or depth == Depth.COMPLETE:
            return heuristic.evaluate_board(state)

        groups = state.get_marble_groups(BoardTile.BLUE)
        valid_moves = state.generate_moves(groups)

        value = InfiniteValues.NEG_INF

        if depth > Depth.NODE_ORDERING_ACTIVATED:  # Node ordering at certain depths, otherwise ordering takes too long
            valid_moves = self._order_nodes(state, valid_moves, heuristic)
        for action in valid_moves:
            if time.time() - start_time >= 9:  # TODO: Change to player time limit; Currently limited to 9 seconds.
                return value
            new_state = state.get_board_after_move(action)
            temp = self.min_value(new_state, alpha, beta, depth - 1, heuristic)
            value = max(value, temp)
            if depth == Depth.START:
                self.dict[temp] = action
            if value > beta:
                return value
            alpha = max(alpha, value)
        return value

    def min_value(self, state: Board, alpha: int, beta: int, depth: int, heuristic: Heuristic) -> int:
        """
        Alpha beta search for Min.

        :param state: Board object
        :param alpha: Alpha value for minimax
        :param beta: Beta value for minimax
        :param depth: depth used in depth iterative search
        :param heuristic: a Heuristic object
        """
        # Test for pause state; is so count time passes until un-paused
        start_time = time.time()
        while self.is_paused:
            time.sleep(1)
            self.seconds_passed += 1

        if self.terminal_test(state) or depth == Depth.COMPLETE:
            return heuristic.evaluate_board(state)

        value = InfiniteValues.POS_INF

        groups = state.get_marble_groups(BoardTile.RED)
        valid_moves = state.generate_moves(groups)

        if depth > Depth.NODE_ORDERING_ACTIVATED:  # Order nodes
            valid_moves = self._order_nodes(state, valid_moves, heuristic)
        for action in valid_moves:
            if time.time() - start_time >= 9:
                break
            new_state = state.get_board_after_move(action)
            temp = self.max_value(new_state, alpha, beta, depth - 1, heuristic)
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
