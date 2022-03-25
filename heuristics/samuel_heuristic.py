from board import Board, BoardTile


class SamuelHeuristic:
    """
    Samuel's proposed heuristic function.
    """

    def __init__(self):
        pass

    @staticmethod
    def evaluate_board(self, board) -> int:
        """
        Returns a minimax score of the passed in board object
        """
        return self.sam_minimax(board)

    def heuristic_distance_from_center(self, board):
        """
        Returns a heuristic value based on block marbles proximity to the center vs the white marbles
        """
        player_color = BoardTile.BLUE
        my_board = board.board
        heuristic_score = [0, 0]
        for iteration in range(0, 2):
            for index in range(5, 9):
                if my_board[('H', index)] == player_color:
                    heuristic_score[iteration] += 1
            for index in range(5, 8):
                if my_board[('G', index)] == player_color:
                    heuristic_score[iteration] += 2
            for index in range(5, 7):
                if my_board[('F', index)] == player_color:
                    heuristic_score[iteration] += 3

            if my_board[('E', 5)] == player_color:
                heuristic_score[iteration] += 4

            for index in range(4, 6):
                if my_board[('D', index)] == player_color:
                    heuristic_score[iteration] += 3
            for index in range(3, 6):
                if my_board[('C', index)] == player_color:
                    heuristic_score[iteration] += 2
            for index in range(2, 6):
                if my_board[('B', index)] == player_color:
                    heuristic_score[iteration] += 1
            #
            for index in range(4, 9, 4):
                if my_board[('G', index)] == player_color:
                    heuristic_score[iteration] += 1

            for index in range(3, 9, 5):
                if my_board[('F', index)] == player_color:
                    heuristic_score[iteration] += 1
            for index in range(4, 8, 3):
                if my_board[('F', index)] == player_color:
                    heuristic_score[iteration] += 2

            for index in range(2, 9, 6):
                if my_board[('E', index)] == player_color:
                    heuristic_score[iteration] += 1
            for index in range(3, 8, 4):
                if my_board[('E', index)] == player_color:
                    heuristic_score[iteration] += 2
            for index in range(4, 7, 2):
                if my_board[('E', index)] == player_color:
                    heuristic_score[iteration] += 3

            for index in range(2, 9, 5):
                if my_board[('D', index)] == player_color:
                    heuristic_score[iteration] += 1
            for index in range(3, 7, 3):
                if my_board[('D', index)] == player_color:
                    heuristic_score[iteration] += 2

            for index in range(2, 7, 4):
                if my_board[('C', index)] == player_color:
                    heuristic_score[iteration] += 1

            player_color = BoardTile.RED

        ultimate_heuristic_score = heuristic_score[0] - heuristic_score[1]
        return ultimate_heuristic_score

    def heuristic_compactness(self, board) -> int:
        """
        Returns a heuristic value based on how many grouped marbles there are with black marbles vs white marbles.
        """
        player_color = BoardTile.BLUE
        marble_groups = board.get_marble_groups(player_color)
        dou_groups = Board._get_duo_group(marble_groups)
        triple_groups = Board._get_trio_group(marble_groups)

        num_duo_groups_blue = len(dou_groups)
        num_triple_groups_blue = len(triple_groups)

        player_color = BoardTile.RED
        marble_groups = board.get_marble_groups(player_color)
        dou_groups = Board._get_duo_group(marble_groups)
        triple_groups = Board._get_trio_group(marble_groups)

        num_duo_groups_red = len(dou_groups)
        num_triple_groups_red = len(triple_groups)
        return ((num_duo_groups_blue * 2) + (num_triple_groups_blue * 3)) - \
               ((num_duo_groups_red * 2) + (num_triple_groups_red * 3))

    def utility(self, board):
        """
        Utility function based on number of marbles captured
        """
        agent_score = board.blue_score
        enemy_score = board.red_score

        if agent_score - enemy_score == 0:
            return 0

        if agent_score == 6:
            return 9999999
        if enemy_score == 6:
            return -9999999
        if agent_score - enemy_score == 1:
            return 200
        if agent_score - enemy_score == 2:
            return 400
        if agent_score - enemy_score == 3:
            return 600
        if agent_score - enemy_score == 4:
            return 800
        if agent_score - enemy_score == 5:
            return 1000

        if agent_score - enemy_score == -1:
            return -200
        if agent_score - enemy_score == -2:
            return -400
        if agent_score - enemy_score == -3:
            return -600
        if agent_score - enemy_score == -4:
            return -800
        if agent_score - enemy_score == -5:
            return -1000

    def sam_minimax(self, board):
        """
        minimax value which draws values from all heuristic functions implemented
        """
        return self.heuristic_distance_from_center(board) + self.heuristic_compactness(board) + \
               self.utility(board)
