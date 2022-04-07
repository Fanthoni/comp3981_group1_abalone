from board import BoardTile


class Heuristic:

    board = None
    black_groups = None
    white_groups = None
    black_score = 0
    white_score = 0
    black_marble_count = 0
    white_marble_count = 0

    CENTER_OF_MASS_WEIGHT = 3
    PROXIMITY_WEIGHT = 2
    MOBILITY_WEIGHT = 1
    MARBLE_COUNT_WEIGHT = 8

    # CENTER_OF_MASS_WEIGHT = 3
    # PROXIMITY_WEIGHT = 3
    # MOBILITY_WEIGHT = 1
    # MARBLE_COUNT_WEIGHT = 6

    @staticmethod
    def evaluate_board(board) -> int:
        """
        Evaluates this board
        :return: a score (int) of how favourable is this board state to a the player
        """
        # Reset
        Heuristic.board = board
        Heuristic.black_groups = board.get_marble_groups(BoardTile.BLUE)
        Heuristic.white_groups = board.get_marble_groups(BoardTile.RED)
        Heuristic.black_score = 0
        Heuristic.white_score = 0
        Heuristic.black_marble_count = len({key for key, value in Heuristic.board.board.items() if value in [BoardTile.BLUE]})
        Heuristic.white_marble_count = len({key for key, value in Heuristic.board.board.items() if value in [BoardTile.RED]})

        Heuristic._evaluate_center_of_mass()
        Heuristic._evaluate_proximity()
        Heuristic._evaluate_mobility()
        Heuristic._evaluate_marble_count()

        total_evaluation_score = Heuristic.black_score - Heuristic.white_score
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
        board = Heuristic.board.board

        non_empty_tiles = {key for key, value in board.items() if value in [BoardTile.RED, BoardTile.BLUE]}
        for tile in non_empty_tiles:
            if board[tile] == BoardTile.BLUE:
                black_center_score += 10 - Heuristic._calculate_manhattan_distance(tile, center_tile)
            else:
                white_center_score += 10 - Heuristic._calculate_manhattan_distance(tile, center_tile)

        # print("Black center score", black_center_score)
        # print("White center score", white_center_score)
        Heuristic.black_score += (black_center_score / Heuristic.black_marble_count) * Heuristic.CENTER_OF_MASS_WEIGHT
        Heuristic.white_score += (white_center_score / Heuristic.white_marble_count) * Heuristic.CENTER_OF_MASS_WEIGHT

    @staticmethod
    def _calculate_manhattan_distance(tile1, tile2) -> int:
        """
        Calculates the manhattan distance of cell1 from cell2
        :param tile1: a Tuple - board coordinate
        :param tile2: a Tuple - board coordinate
        :return: a positive integer
        """
        return abs(ord(tile1[0]) - ord(tile2[0])) + abs(tile1[1] - tile2[1])

    # @staticmethod
    # def _calculate_manhattan_distance(tile1, tile2) -> int:
    #     """
    #     Calculates the manhattan distance of cell1 from cell2
    #     :param tile1: a Tuple - board coordinate
    #     :param tile2: a Tuple - board coordinate
    #     :return: a positive integer
    #     """
    #     distance = abs(ord(tile1[0]) - ord(tile2[0])) + abs(tile1[1] - tile2[1])
    #     distance = distance * 2 if tile1[0] == 'E' or tile1[1] == 5 else distance
    #     return distance

    @staticmethod
    def _evaluate_proximity():
        """
        Evaluates how close is one marble to another fellow marble surrounding it

        black_proximity_score - white_proximity_score

        :return: proximity evaluation score
        """
        black_proximity_score = Heuristic._calculate_proximity_score(Heuristic.black_groups)
        white_proximity_score = Heuristic._calculate_proximity_score(Heuristic.white_groups)

        # print("Black Prox Score", black_proximity_score)
        # print("White Prox Score", white_proximity_score)
        Heuristic.black_score += (black_proximity_score / Heuristic.black_marble_count) * Heuristic.PROXIMITY_WEIGHT
        Heuristic.white_score += (white_proximity_score / Heuristic.white_marble_count) * Heuristic.PROXIMITY_WEIGHT

    @staticmethod
    def _calculate_proximity_score(marble_groups: set):
        proximity_score = 0
        for group in marble_groups:
            if Heuristic._is_group_of_two(group):
                proximity_score += 2
            elif Heuristic._is_group_of_three(group):
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

        single_marbles_black = set(filter(Heuristic._is_single_marble, Heuristic.black_groups))
        duo_marbles_black = set(filter(Heuristic._is_group_of_two, Heuristic.black_groups))
        trio_marbles_black = set(filter(Heuristic._is_group_of_three, Heuristic.black_groups))

        single_marbles_white = set(filter(Heuristic._is_single_marble, Heuristic.white_groups))
        duo_marbles_white = set(filter(Heuristic._is_group_of_two, Heuristic.white_groups))
        trio_marbles_white = set(filter(Heuristic._is_group_of_three, Heuristic.white_groups))

        for group in single_marbles_black:
            black_mobility_score += len(Heuristic.board._generate_single_moves(group)) * 0
        for group in duo_marbles_black:
            black_mobility_score += len(Heuristic.board._generate_duo_moves(group)) * 2
        for group in trio_marbles_black:
            black_mobility_score += len(Heuristic.board._generate_trio_moves(group)) * 5

        for group in single_marbles_white:
            white_mobility_score += len(Heuristic.board._generate_single_moves(group)) * 0
        for group in duo_marbles_white:
            white_mobility_score += len(Heuristic.board._generate_duo_moves(group)) * 2
        for group in trio_marbles_white:
            white_mobility_score += len(Heuristic.board._generate_trio_moves(group)) * 5

        # print("Black Mobility", black_mobility_score)
        # print("White Mobility", white_mobility_score)
        Heuristic.black_score += (black_mobility_score / Heuristic.black_marble_count) * Heuristic.MOBILITY_WEIGHT
        Heuristic.white_score += (white_mobility_score / Heuristic.white_marble_count) * Heuristic.MOBILITY_WEIGHT

    @staticmethod
    def _evaluate_marble_count():
        black_marble_count = len({key for key, value in Heuristic.board.board.items() if value in [BoardTile.BLUE]})
        white_marble_count = len({key for key, value in Heuristic.board.board.items() if value in [BoardTile.RED]})
        # print("Marble count difference", black_marble_count - white_marble_count)
        Heuristic.black_score += black_marble_count * Heuristic.MARBLE_COUNT_WEIGHT
        Heuristic.white_score += white_marble_count * Heuristic.MARBLE_COUNT_WEIGHT