import abalone
from board import Board, BoardTile


class AnsonHeuristic:
    def __init__(self, state):
        self.state = state

    def evaluate_board(self):
        score = self.groups_of_3() + self.protected_marbles() + self.marbles_on_edge() \
                + self.centeredness() + self.number_of_marbles()

        return score

    def groups_of_3(self):
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
        black_score = 0
        white_score = 0

        for key, value in self.state.board.items():
            if value == BoardTile.BLUE:
                black_score += 1
            if value == BoardTile.RED:
                white_score += 1

        if black_score > white_score:
            black_score += 20
        elif white_score > black_score:
            white_score += 20

        return black_score - white_score
