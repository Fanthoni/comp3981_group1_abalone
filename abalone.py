from board import StartingPositions, Board


class Abalone:
    """
    WIP - ac
    """

    def __init__(self):
        self._board = None
        self._players = {"Black": None, "White": None}  # Player class not implemented yet
        self._current_player = self._players["Black"]
        self._is_game_paused = False
        self._is_game_stopped = False
        self._game_mode = StartingPositions.DEFAULT

    def start_game(self):
        """
        Starts the game and contains game logic.
        :return:
        """
        self.board = Board(self._game_mode)
        self.board.print_board()
        while not self.is_game_stopped:
            # Hacky for not, definitely will get changed when our Player class is implemented.
            # Our Player class will handle their own timers, moves, and previous moves.
            print("---Player 1---")
            self.player_moves()

            if self.is_game_stopped:
                break

            print("---Player 2---")
            self.player_moves()

        self.reset_game()

    def player_moves(self):
        """
        For UI demonstration purposes only - Player class not implemented yet.
        :return:
        """
        print("Time remaining: X")
        print("Moves remaining: X")
        Abalone.print_menu_options()

        moved = False
        while not moved:
            user_input = input("Input: ")
            match user_input:
                case "1":
                    input("Enter Move Information: ")
                    print("Pieces moved! (Pretend it moved)")
                    print("Time taken for this move: X")
                    moved = True
                    self.board.print_board()
                case "2":
                    print("Previous moves: ...")
                case "3":
                    self.pause_game()
                    input("Enter anything to resume: ")
                    self.resume_game()
                case "4":
                    self.stop_game()
                    break

    @staticmethod
    def print_menu_options():
        """
        Prints in-game menu options.
        :return:
        """
        print("1. Make Move\n"
              "2. View Previous Moves\n"
              "3. Pause Game\n"
              "4. Stop Game")

    def color_selection(self):
        pass

    def set_move_limit(self):
        pass

    def set_time_limit(self):
        pass

    def set_start_positions(self, enum_value):
        """
        Sets the starting positions.
        :param enum_value:
        :return:
        """
        if enum_value in (StartingPositions.DEFAULT, StartingPositions.GERMAN, StartingPositions.BELGIAN):
            self._game_mode = enum_value

    def undo_last_move(self):
        """
        Undo the last move made.
        :return:
        """
        pass

    def pause_game(self):
        """
        Pause the game.

        :return: None
        """
        print("Game paused")
        self.is_game_paused = True

    def resume_game(self):
        """
        Resume game after it's been paused.

        :return: None
        """
        print("Game resumed")
        self.is_game_paused = False

    def reset_game(self):
        """
        Assists in resetting the Abalone object after stopping game.

        :return: None
        """
        self.is_game_paused = False
        self.is_game_stopped = False

    def stop_game(self):
        """
        Stops the game.

        :return: None
        """
        print("Game stopped")
        self.is_game_stopped = True

    @property
    def is_game_paused(self):
        """
        Returns value for if the game is paused or not.

        :return: None
        """
        return self._is_game_paused

    @is_game_paused.setter
    def is_game_paused(self, paused):
        """
        Sets the value for if game is paused or not.
        :param paused: boolean (True/False)

        :return: None
        """
        self._is_game_paused = paused

    @property
    def is_game_stopped(self):
        """
        Returns value for if game is stopped or not.

        :return: None
        """
        return self._is_game_stopped

    @is_game_stopped.setter
    def is_game_stopped(self, stopped):
        """
        Sets value for if game is stopped or not
        :param stopped: boolean (True/False)

        :return: None
        """
        self._is_game_stopped = stopped

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board


if __name__ == "__main__":
    abalone = Abalone()
    abalone.start_game()

