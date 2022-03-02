"""
Contains the UI elements for the abalone game.
"""
from abalone import Abalone
from board import StartingPositions


class AbaloneUI:
    """
    WIP - ac
    """

    def __init__(self):
        self.abalone = Abalone()

    def main_menu(self):
        """
        Main menu for the game.

        :return: None
        """
        user_input = -1
        while not user_input == "6":
            AbaloneUI.print_menu_options()
            user_input = input("Input: ")

            match user_input:
                case "1":
                    self.abalone.start_game()
                case "2":
                    self.set_game_mode()
                case "3":
                    self.set_player_colour()
                case "4":
                    self.set_turn_time()
                case "5":
                    self.set_turn_lim()
                case "6":
                    pass
                case _:
                    print("Invalid")

    def set_game_mode(self):
        AbaloneUI.print_game_options()
        user_input = input("Input: ")

        match user_input:
            case "1":
                self.abalone.set_game_mode(StartingPositions.DEFAULT)
            case "2":
                self.abalone.set_game_mode(StartingPositions.GERMAN)
            case "3":
                self.abalone.set_game_mode(StartingPositions.BELGIAN)
            case _:
                print("Invalid")

    def set_turn_lim(self):
        """
        Sub-menu to set the turn limit.

        :return: an int
        """
        pass

    def set_turn_time(self):
        """
        Sub-menu to set the turn time in seconds.

        :return: an int, time in seconds.
        """
        pass

    def set_player_colour(self):
        """
        Set the player colour.

        :return:f
        """
        pass

    @staticmethod
    def print_menu_options():
        print("---Main Menu---")
        print("1. Start Game\n"
              "2. Set Starting Positions\n"
              "3. Set Player Colors\n"
              "4. Set Turn Time\n"
              "5. Set Turn Limit\n"
              "6. Exit")

    @staticmethod
    def print_game_options():
        print("---Starting Positions---")
        print("1. Default\n"
              "2. German\n"
              "3. Belgian")


if __name__ == "__main__":
    ui = AbaloneUI()
    ui.main_menu()
