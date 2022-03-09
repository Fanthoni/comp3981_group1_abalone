from board import StartingPositions, Board, BoardTile


class Abalone:
    """
    WIP - ac
    """

    def __init__(self):
        self._board = None
        self._players = {"Black": "Human", "White": "Human"}  # Player class not implemented yet
        self._current_player = "Black"
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

        if self._players["Black"] == "AI" and self._players["White"] == "AI":
            print("We do not support two AIs playing against each other yet. Please reconfigure players.")
            return

        while not self.is_game_stopped:
            # Our Player class will handle their own timers, moves, and previous moves.

            if self._current_player == "Black":
                if self._players.get("Black") == "AI":
                    print("---Black (AI)---")
                    self.ai_moves()
                else:
                    print("---Black (Player)---")
                    self.player_moves()
                self._current_player = "White"
            elif self._current_player == "White":
                if self._players.get("White") == "AI":
                    print("---White (AI)---")
                    self.ai_moves()
                else:
                    print("---White (Player)---")
                    self.player_moves()
                self._current_player = "Black"

        self.reset_game()

    def ai_moves(self):
        print("Time remaining: X")
        print("Moves remaining: X")
        print("Previous Moves: ...")
        print("Next Move = X")
        print("Time used to decide this move: X")

        print("Black : 0 - 0 : White")  # Scoreboard
        self.board.print_board()

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
                    print("Black : 0 - 0 : White")  # Scoreboard
                    self.board.print_board()
                case "2":
                    print("Previous moves: ...")
                case "3":
                    self.undo_last_move()
                case "4":
                    self.pause_game()
                    input("Enter anything to resume: ")
                    self.resume_game()
                case "5":
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
              "3. Undo Move\n"
              "4. Pause Game\n"
              "5. Stop Game")

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
        print("Move undone!")

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

    def set_player1(self, player):
        """
        Sets a player to black.
        """
        self._players["Black"] = player

    def set_player2(self, player):
        """
        Sets a player to white.
        """
        self._players["White"] = player

    @property
    def board(self):
        return self._board

    @board.setter
    def board(self, board):
        self._board = board

    def setup_from_input_file(self, file_name):
        """
        Takes an input file as input, translates it into a board layout and sets a player to the current player.
        :param file_name: input file

        :return: None
        """
        self.board = Board(StartingPositions.EMPTY)
        with open(file_name, 'r') as file:
            data = file.readlines()
            moves = data[1].strip('\n').split(',')

        key = "White" if data[0].strip('\n') == "w" else "Black"
        self._current_player = self._players[key]

        self.board.setup_board_from_moves(moves)
        print(f"{key}'s move (Black = Blue, White = Red)")
        self.board.print_board()

    def get_board_information(self):
        """
        Calls same method from board to get the board information.

        :return: String
        """
        return self.board.get_board_information()

    def get_marble_groups(self):
        return self.board.get_marble_groups()


if __name__ == "__main__":
    abalone = Abalone()
    abalone.setup_from_input_file("Test1")
    red_combinations = abalone.board.get_marble_groups(BoardTile.RED)
    # print(red_combinations)
    abalone.board.generate_moves(red_combinations)
