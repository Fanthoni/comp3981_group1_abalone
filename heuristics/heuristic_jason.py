import board


class HeuristicJason:
    """
    The heuristic used to measure agent performance.

    Takes into account the groupings of marbles, the total possible moves available to the agent, control of the center
    of the board and the number of marbles in 'danger'.
    """
    def __init__(self, game_board: board.Board):
        self.board = game_board
        self.black_groups = self.board.get_marble_groups(board.BoardTile.BLUE)
        self.white_groups = self.board.get_marble_groups(board.BoardTile.RED)
        self.black_total = 0
        self.white_total = 0

    # Redundant with callable but leaving in for now.
    def evaluate_board(self) -> int:
        """
        Calculate the heuristic value of the board.

        :return: an int, the heuristic value of the board relative to the black/blue player.
        """
        self._evaluate_control()
        self._evaluate_groupings()
        self._evaluate_score()
        return self.black_total - self.white_total

    def _evaluate_control(self):
        """
        Adds the heuristic values of board control.

        Marbles in the center score a small number of points. Marbles on the edge grant the opponent a large number of
        points.
        """
        center_tiles = [('C', 3), ('C', 4), ('C', 5), ('D', 3), ('D', 4), ('D', 5), ('D', 6), ('E', 3), ('E', 4),
                        ('E', 5), ('E', 6), ('E', 7), ('F', 3), ('F', 4), ('F', 5), ('F', 6), ('G', 3), ('G', 4),
                        ('G', 5)]
        edge_tiles = [('A', 1), ('A', 2), ('A', 3), ('A', 4), ('A', 5), ('B', 1), ('C', 1), ('D', 1), ('E', 1),
                      ('F', 2), ('G', 3), ('H', 4), ('I', 5), ('I', 6), ('I', 7), ('I', 8), ('I', 9), ('H', 9),
                      ('G', 9), ('F', 9), ('D', 8), ('C', 7), ('B', 6)]

        # Checks each colour and adds a heuristic total accordingly.
        for tile, value in self.board.board:
            if self.board.board[tile] == board.BoardTile.BLUE and self.board.board[tile] in center_tiles:
                self.black_total += 5
            elif self.board.board[tile] == board.BoardTile.BLUE and self.board.board[tile] in edge_tiles:
                self.white_total += 50
            elif self.board.board[tile] == board.BoardTile.RED and self.board.board[tile] in center_tiles:
                self.white_total += 5
            elif self.board.board[tile] == board.BoardTile.RED and self.board.board[tile] in edge_tiles:
                self.black_total += 50

    def _evaluate_groupings(self):
        """
        Adds heuristic values based on number marble groupings and the moves available to each.
        """
        totals = (self.white_total, self.black_total)

        # Assess the total possible number of groupings for each colour.
        for colour in totals:
            for grouping in self.black_groups:
                match len(grouping):
                    case 1:
                        colour += len(self.board.generate_moves(grouping))
                    case 2:
                        self.black_total += len(self.board.generate_moves(grouping)) + 10
                    case 3:
                        self.black_total += len(self.board.generate_moves(grouping)) + 20

    def _evaluate_score(self):
        """
        Adds heuristic values based on the resulting scores.

        Agent will move heavily in favour of not being scored on.
        """
        self.black_total += self.board.blue_score * 200
        self.white_total += self.board.red_score * 200

    def __call__(self):
        """
        When called returns the heuristic value of the input board.

        :return: an int
        """
        self._evaluate_control()
        self._evaluate_groupings()
        self._evaluate_score()
        return self.black_total - self.white_total
