"""
Contains the UI elements for the abalone game.
"""
from abalone import Abalone
from board import StartingPositions
from player import AIPlayer, HumanPlayer


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
        while not user_input == "7":
            AbaloneUI.print_menu_options()
            user_input = input("Input: ")

            match user_input:
                case "1":
                    self.abalone.start_game()
                case "2":
                    self.set_starting_position()
                case "3":
                    self.set_game_mode()
                case "4":
                    self.set_player_colour()
                case "5":
                    self.set_turn_time()
                case "6":
                    self.set_turn_lim()
                case "7":
                    pass
                case _:
                    print("Invalid")

    def set_starting_position(self):
        """
        Sets the starting position to one of three types.

        :return: None
        """
        AbaloneUI.print_game_options()
        user_input = input("Input: ")

        match user_input:
            case "1":
                self.abalone.set_start_positions(StartingPositions.DEFAULT)
                print("Starting position changed to DEFAULT.")
            case "2":
                self.abalone.set_start_positions(StartingPositions.GERMAN)
                print("Starting position changed to GERMAN.")

            case "3":
                self.abalone.set_start_positions(StartingPositions.BELGIAN)
                print("Starting position changed to BELGIAN")
            case _:
                print("Invalid")

    def set_game_mode(self):
        """
        Sets game to be played against human or AI for both players.

        :return: None
        """
        print("---Player 1---")
        user_input_p1 = input("1. Human\n"
                              "2. AI\n"
                              "Input: ")

        print("---Player 2---")
        user_input_p2 = input("1. Human\n"
                              "2. AI\n"
                              "Input: ")

        p1 = AIPlayer() if user_input_p1 == "2" else HumanPlayer()
        p2 = AIPlayer() if user_input_p2 == "2" else HumanPlayer()

        self.abalone.set_player1(p1)
        print(self.abalone._players["Black"])
        self.abalone.set_player2(p2)
        print(self.abalone._players["White"])


        print(f"Player 1 set to {p1} and Player 2 set to {p2}")

    def set_turn_lim(self):
        """
        Sub-menu to set the turn limit.

        :return: an int
        """
        print("---Player 1 Turn Limit---")
        user_input = input("Input: ")
        print(f"Player 1's turn limit set to {user_input} turns.")

        print("---Player 2 Turn Limit---")
        user_input = input("Input: ")
        print(f"Player 1's turn limit set to {user_input} turns.")

    def set_turn_time(self):
        """
        Sub-menu to set the turn time in seconds.

        :return: an int, time in seconds.
        """
        print("---Player 1 Time Limit---")
        user_input = input("Input: ")
        print(f"Player 1's time limit per turn set to {user_input} seconds.")

        print("---Player 2 Time Limit---")
        user_input = input("Input: ")
        print(f"Player 2's time limit per turn set to {user_input} seconds.")

    def set_player_colour(self):
        """
        Set the player colour.

        :return:f
        """
        print("---Player 1 Color---")
        user_input = input("1. White\n"
                           "2. Black\n"
                           "Input: ")
        p1 = "White"
        p2 = "Black"

        if user_input == "2":
            p1, p2 = p2, p1

        print(f"Player 1 set to {p1}, Player 2 automatically set to {p2}")

    @staticmethod
    def print_menu_options():
        print("---Main Menu---")
        print("1. Start Game\n"
              "2. Set Starting Positions\n"
              "3. Set Game Mode\n"
              "4. Set Player Colors\n"
              "5. Set Turn Time\n"
              "6. Set Turn Limit\n"
              "7. Exit")

    @staticmethod
    def print_game_options():
        print("---Starting Positions---")
        print("1. Default\n"
              "2. German\n"
              "3. Belgian")


if __name__ == "__main__":
    ui = AbaloneUI()
    ui.main_menu()
