import abalone
from board import Board, BoardTile


class AnsonHeuristic:
    """
    Anson's heuristic function.

    Note: Development of this heuristic stopped pretty early on.
    """
    def __init__(self, state):
        self.state = state

    def evaluate_board(self):
        """
        Returns total score of the given board.
        """
        score = self.groups_of_3() + self.protected_marbles() + self.marbles_on_edge() \
                + self.centeredness() + self.number_of_marbles() + self.eliminate_marble()

        return score

    def groups_of_3(self):
        """
        Returns score based off of groups of three marbles (push power).
        """
        black_score = 0
        white_score = 0

        white_group = self.state.get_marble_groups(BoardTile.RED)
        black_group = self.state.get_marble_groups(BoardTile.BLUE)

        for group in white_group:
            if len(group) == 3:
                white_score += 5

        for group in black_group:
            if len(group) == 3:
                black_score += 5

        return black_score - white_score

    def protected_marbles(self):
        """
        Returns score based on how protected the player's marbles are.
        """
        directions = [(0, -1), (1, 0), (1, 1), (0, 1), (-1, 0), (-1, -1)]

        black_score = 0
        white_score = 0

        for key, value in self.state.board.items():
            if value == BoardTile.BLUE:
                for direction in directions:
                    if self.state.board.get(chr(ord(key[0]) + direction[0]), key[1] + direction[1]) == BoardTile.BLUE:
                        black_score += 1
            if value == BoardTile.RED:
                for direction in directions:
                    if self.state.board.get(chr(ord(key[0]) + direction[0]), key[1] + direction[1]) == BoardTile.RED:
                        black_score += 1

        return black_score - white_score

    def centeredness(self):
        """
        Returns score based off of the security of having marbles in the center, away from threat.
        """
        black_score = 0
        white_score = 0
        center_marble = ('E', 5)

        for key, value in self.state.board.items():
            if value == BoardTile.BLUE:
                distance = (abs(ord(key[0]) - ord(center_marble[0])), key[1] - center_marble[1])
                black_score += (3 - distance[0] + 5 - distance[1])
            if value == BoardTile.RED:
                distance = (abs(ord(key[0]) - ord(center_marble[0])), key[1] - center_marble[1])
                white_score += (3 - distance[0] + 5 - distance[1])

        return black_score - white_score

    def marbles_on_edge(self):
        """
        Subtracts points from score if marbles are on the edge of the board, they are threatened.
        """
        edges = {('A', 1), ('A', 2), ('A', 3), ('A', 4), ('A', 5), ('B', 1), ('C', 1), ('D', 1), ('E', 1),
                 ('F', 2), ('G', 3), ('H', 4), ('I', 5), ('I', 6), ('I', 7), ('I', 8), ('I', 9), ('H', 9),
                 ('G', 9), ('F', 9), ('D', 8), ('C', 7), ('B', 6)}

        black_score = 0
        white_score = 0

        for key, value in self.state.board.items():
            if key in edges:
                if value == BoardTile.BLUE:
                    black_score -= 5
                if value == BoardTile.RED:
                    white_score -= 5

        return black_score - white_score

    def number_of_marbles(self):
        """
        Returns score for number of marbles.
        """
        black_score = 0
        white_score = 0

        for key, value in self.state.board.items():
            if value == BoardTile.BLUE:
                black_score += 1
            if value == BoardTile.RED:
                white_score += 1

        return black_score - white_score

    def eliminate_marble(self):
        """
        Returns score for scoring a point by pushing an opponent's marble off.
        """
        black_score = 0
        white_score = 0

        border = {
            ('A', 0): BoardTile.BORDER, ('A', 6): BoardTile.BORDER, ('B', 0): BoardTile.BORDER,
            ('B', 7): BoardTile.BORDER, ('C', 0): BoardTile.BORDER, ('C', 8): BoardTile.BORDER,
            ('D', 0): BoardTile.BORDER, ('D', 9): BoardTile.BORDER, ('E', 0): BoardTile.BORDER,
            ('E', 10): BoardTile.BORDER, ('F', 1): BoardTile.BORDER, ('F', 10): BoardTile.BORDER,
            ('G', 2): BoardTile.BORDER, ('G', 10): BoardTile.BORDER, ('H', 3): BoardTile.BORDER,
            ('H', 10): BoardTile.BORDER, ('I', 4): BoardTile.BORDER, ('I', 10): BoardTile.BORDER,
            ('J', 5): BoardTile.BORDER, ('J', 6): BoardTile.BORDER, ('J', 7): BoardTile.BORDER,
            ('J', 8): BoardTile.BORDER, ('J', 9): BoardTile.BORDER, ('J', 10): BoardTile.BORDER,
            ('@', 0): BoardTile.BORDER, ('@', 1): BoardTile.BORDER, ('@', 2): BoardTile.BORDER,
            ('@', 3): BoardTile.BORDER, ('@', 4): BoardTile.BORDER,
            ('@', 5): BoardTile.BORDER
        }

        for key, value in self.state.board.items():
            if key in border and value != BoardTile.BORDER:
                if value == BoardTile.BLUE:
                    white_score += 25
                if value == BoardTile.RED:
                    black_score += 25

        return black_score - white_score

