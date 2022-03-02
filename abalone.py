from board import StartingPositions, Board


class Abalone:
    """
    WIP - ac
    """

    def __init__(self):
        self._board = None
        self._players = ["Black", "White"]  # Player class not implemented yet
        self._current_player = self._players[0]
        self._is_game_paused = False
        self._is_game_stopped = False
        self._game_mode = StartingPositions.DEFAULT

    def start_game(self):

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
        print("---Game Menu---")
        print("1. Pause Game\n"
              "2. Stop Game")

    def color_selection(self):
        pass

    def set_move_limit(self):
        pass

    def set_time_limit(self):
        pass

    def set_game_mode(self, enum_value):
        if enum_value in (StartingPositions.DEFAULT, StartingPositions.GERMAN, StartingPositions.BELGIAN):
            self._game_mode = enum_value

    def undo_last_move(self):
        pass

    def pause_game(self):
        print("Game paused")
        self.is_game_paused = True

    def resume_game(self):
        print("Game resumed")
        self.is_game_paused = False

    def reset_game(self):
        self.is_game_paused = False
        self.is_game_stopped = False

    def stop_game(self):
        self.is_game_stopped = True

    @property
    def is_game_paused(self):
        return self._is_game_paused

    @is_game_paused.setter
    def is_game_paused(self, paused):
        self._is_game_paused = paused

    @property
    def is_game_stopped(self):
        return self._is_game_stopped

    @is_game_stopped.setter
    def is_game_stopped(self, stopped):
        self._is_game_stopped = stopped


if __name__ == "__main__":
    abalone = Abalone()
    abalone.start_game()
