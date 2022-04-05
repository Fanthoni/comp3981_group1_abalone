from board import BoardTile


class Heuristic2:

    board = None
    black_groups = None
    white_groups = None
    black_score = 0
    white_score = 0
    black_marble_count = 0
    white_marble_count = 0

    CENTER_OF_MASS_WEIGHT = 2
    PROXIMITY_WEIGHT = 3
    MOBILITY_WEIGHT = 1
    MARBLE_COUNT_WEIGHT = 4

    @staticmethod
    def evaluate_board(board) -> int:
        """
        Evaluates this board
        :return: a score (int) of how favourable is this board state to a the player
        """
        # Reset
        Heuristic2.board = board
        Heuristic2.black_groups = board.get_marble_groups(BoardTile.BLUE)
        Heuristic2.white_groups = board.get_marble_groups(BoardTile.RED)
        Heuristic2.black_score = 0
        Heuristic2.white_score = 0
        Heuristic2.black_marble_count = len({key for key, value in Heuristic2.board.board.items() if value in [BoardTile.BLUE]})
        Heuristic2.white_marble_count = len({key for key, value in Heuristic2.board.board.items() if value in [BoardTile.RED]})

        Heuristic2._evaluate_center_of_mass()
        Heuristic2._evaluate_proximity()
        Heuristic2._evaluate_mobility()
        Heuristic2._evaluate_marble_count()

        total_evaluation_score = Heuristic2.black_score - Heuristic2.white_score
        # print("Board Overall Evaluation", total_evaluation_score)
        return total_evaluation_score

    @staticmethod
    def _evaluate_center_of_mass():
        """
        Evaluate the center of mass of a board

        Evaluation process calculates for both sides and returns the difference:
        center_of_mass(BLACK) - center_of_mass(WHITE)
        """
        center_tile = ('E', 5)
        black_center_score = 0
        white_center_score = 0
        board = Heuristic2.board.board

        non_empty_tiles = {key for key, value in board.items() if value in [BoardTile.RED, BoardTile.BLUE]}
        for tile in non_empty_tiles:
            if board[tile] == BoardTile.BLUE:
                black_center_score += 10 - Heuristic2._calculate_manhattan_distance(tile, center_tile)
            else:
                white_center_score += 10 - Heuristic2._calculate_manhattan_distance(tile, center_tile)

        # print("Black center score", black_center_score)
        # print("White center score", white_center_score)
        Heuristic2.black_score += (black_center_score / Heuristic2.black_marble_count) * Heuristic2.CENTER_OF_MASS_WEIGHT
        Heuristic2.white_score += (white_center_score / Heuristic2.white_marble_count) * Heuristic2.CENTER_OF_MASS_WEIGHT

    # @staticmethod
    # def _calculate_manhattan_distance(tile1, tile2) -> int:
    #     """
    #     Calculates the manhattan distance of cell1 from cell2
    #     :param tile1: a Tuple - board coordinate
    #     :param tile2: a Tuple - board coordinate
    #     :return: a positive integer
    #     """
    #     return abs(ord(tile1[0]) - ord(tile2[0])) + abs(tile1[1] - tile2[1])

    @staticmethod
    def _calculate_manhattan_distance(tile1, tile2) -> int:
        """
        Calculates the manhattan distance of cell1 from cell2
        :param tile1: a Tuple - board coordinate
        :param tile2: a Tuple - board coordinate
        :return: a positive integer
        """
        distance = abs(ord(tile1[0]) - ord(tile2[0])) + abs(tile1[1] - tile2[1])
        distance = distance * 2 if tile1[0] == 'E' or tile1[1] == 5 else distance
        return distance

    @staticmethod
    def _evaluate_proximity():
        """
        Evaluates how close is one marble to another fellow marble surrounding it

        black_proximity_score - white_proximity_score

        :return: proximity evaluation score
        """
        black_proximity_score = Heuristic2._calculate_proximity_score(Heuristic2.black_groups)
        white_proximity_score = Heuristic2._calculate_proximity_score(Heuristic2.white_groups)

        # print("Black Prox Score", black_proximity_score)
        # print("White Prox Score", white_proximity_score)
        Heuristic2.black_score += (black_proximity_score / Heuristic2.black_marble_count) * Heuristic2.PROXIMITY_WEIGHT
        Heuristic2.white_score += (white_proximity_score / Heuristic2.white_marble_count) * Heuristic2.PROXIMITY_WEIGHT

    @staticmethod
    def _calculate_proximity_score(marble_groups: set):
        proximity_score = 0
        for group in marble_groups:
            if Heuristic2._is_group_of_two(group):
                proximity_score += 2
            elif Heuristic2._is_group_of_three(group):
                proximity_score += 3
        return proximity_score

    @staticmethod
    def _is_single_marble(group):
        return type(group[0]) == str

    @staticmethod
    def _is_group_of_two(group):
        return len(group) == 2 and type(group[0]) == tuple

    @staticmethod
    def _is_group_of_three(group):
        return len(group) == 3

    @staticmethod
    def _evaluate_mobility():
        black_mobility_score = 0
        white_mobility_score = 0

        single_marbles_black = set(filter(Heuristic2._is_single_marble, Heuristic2.black_groups))
        duo_marbles_black = set(filter(Heuristic2._is_group_of_two, Heuristic2.black_groups))
        trio_marbles_black = set(filter(Heuristic2._is_group_of_three, Heuristic2.black_groups))

        single_marbles_white = set(filter(Heuristic2._is_single_marble, Heuristic2.white_groups))
        duo_marbles_white = set(filter(Heuristic2._is_group_of_two, Heuristic2.white_groups))
        trio_marbles_white = set(filter(Heuristic2._is_group_of_three, Heuristic2.white_groups))

        for group in single_marbles_black:
            black_mobility_score += len(Heuristic2.board._generate_single_moves(group)) * 0
        for group in duo_marbles_black:
            black_mobility_score += len(Heuristic2.board._generate_duo_moves(group)) * 2
        for group in trio_marbles_black:
            black_mobility_score += len(Heuristic2.board._generate_trio_moves(group)) * 5

        for group in single_marbles_white:
            white_mobility_score += len(Heuristic2.board._generate_single_moves(group)) * 0
        for group in duo_marbles_white:
            white_mobility_score += len(Heuristic2.board._generate_duo_moves(group)) * 2
        for group in trio_marbles_white:
            white_mobility_score += len(Heuristic2.board._generate_trio_moves(group)) * 5

        # print("Black Mobility", black_mobility_score)
        # print("White Mobility", white_mobility_score)
        Heuristic2.black_score += (black_mobility_score / Heuristic2.black_marble_count) * Heuristic2.MOBILITY_WEIGHT
        Heuristic2.white_score += (white_mobility_score / Heuristic2.white_marble_count) * Heuristic2.MOBILITY_WEIGHT

    @staticmethod
    def _evaluate_marble_count():
        black_marble_count = len({key for key, value in Heuristic2.board.board.items() if value in [BoardTile.BLUE]})
        white_marble_count = len({key for key, value in Heuristic2.board.board.items() if value in [BoardTile.RED]})
        # print("Marble count difference", black_marble_count - white_marble_count)
        Heuristic2.black_score += black_marble_count * Heuristic2.MARBLE_COUNT_WEIGHT
        Heuristic2.white_score += white_marble_count * Heuristic2.MARBLE_COUNT_WEIGHT