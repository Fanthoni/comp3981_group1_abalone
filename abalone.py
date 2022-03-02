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
        self._board = Board(self._game_mode)

        while not self.is_game_stopped:
            if self.is_game_paused:
                input("Enter anything to resume game: ")
                self.resume_game()

            self._board.print_board()
            Abalone.print_menu_options()

            user_input = input("Input: ")
            match user_input:
                case "1":
                    self.pause_game()
                case "2":
                    self.stop_game()

        self.reset_game()

    @staticmethod
    def print_menu_options():
        """
        Prints in-game menu options.
        :return:
        """
        print("---Game Menu---")
        print("1. Pause Game\n"
              "2. Stop Game")

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


if __name__ == "__main__":
    abalone = Abalone()
    abalone.start_game()


