import tkinter as tk

import player
from board import StartingPositions
from enum import Enum
from player import *


class PlayerMode(Enum):
    HUMAN = "Human"
    AI = "AI"


class SettingsMenu:
    window_size = "300x600"

    def __init__(self, game_gui, abalone):
        self._game = abalone
        # self._root = tk.Tk()
        self._root = tk.Toplevel(game_gui)
        self._starting_pos = tk.Variable(value=StartingPositions.DEFAULT)
        self._player1_mode = tk.Variable(value=PlayerMode.HUMAN)
        self._player2_mode = tk.Variable(value=PlayerMode.AI)
        self._player_move_limit = None

        # time limit in integer second
        self._player1_time_limit = None
        self._player2_time_limit = None

    def display(self):
        """
        The entry point to run the window
        """
        settings_window = self._root
        settings_window.geometry(SettingsMenu.window_size)
        settings_window.title("Abalone Game Settings")

        self.pack_starting_positions_options()
        # self.pack_player_color_options()

        self.pack_player1_mode_options()
        self.pack_player2_mode_options()

        self.pack_turn_and_move_limit_config()

        self.pack_submit_button()

        # settings_window.mainloop()

    def pack_starting_positions_options(self):
        frame = tk.Frame(master=self._root)
        frame.grid(row=0, column=0)

        start_pos_title = tk.Label(master=frame, text="\nStarting Position")
        start_pos_title.config(font=("Roboto", 18))
        start_pos_title.pack()

        for pos in [positions for positions in StartingPositions if positions is not StartingPositions.EMPTY]:
            opt = tk.Radiobutton(
                master=frame, text=pos.value, value=pos, variable=self._starting_pos
            )
            opt.pack()

    def pack_player1_mode_options(self):
        frame = tk.Frame(master=self._root)
        frame.grid(row=1, column=0)

        player1_mode_title = tk.Label(master=frame, text="\nPlayer1 Mode (Black/Blue)")
        player1_mode_title.config(font=("Roboto", 18))
        player1_mode_title.pack()

        for player_mode in [mode for mode in PlayerMode]:
            opt = tk.Radiobutton(
                master=frame, text=player_mode.value, value=player_mode, variable=self._player1_mode
            )
            opt.pack()

    def pack_player2_mode_options(self):
        frame = tk.Frame(master=self._root)
        frame.grid(row=2, column=0)

        player2_mode_title = tk.Label(master=frame, text="\nPlayer2 Mode (White/Red)")
        player2_mode_title.config(font=("Roboto", 18))
        player2_mode_title.pack()

        for player_mode in [mode for mode in PlayerMode]:
            opt = tk.Radiobutton(
                master=frame, text=player_mode.value, value=player_mode, variable=self._player2_mode
            )
            opt.pack()

    def pack_turn_and_move_limit_config(self):
        frame = tk.Frame(master=self._root)
        frame.grid(row=3, column=0)

        time_and_move_limit_config_title = tk.Label(master=frame, text="\nTime & Move Limit")
        time_and_move_limit_config_title.config(font=("Roboto", 18))
        time_and_move_limit_config_title.pack()

        move_limit_label = tk.Label(master=frame, text="Move Limit per Player")
        move_limit_label.pack()
        self._player_move_limit = tk.Entry(master=frame, width=20)
        self._player_move_limit.insert(0, "40")
        self._player_move_limit.pack()

        player1_turn_limit_label = tk.Label(master=frame, text="Player1 Turn Limit (seconds)")
        player1_turn_limit_label.pack()
        self._player1_time_limit = tk.Entry(master=frame, width=20)
        self._player1_time_limit.insert(0, "10")
        self._player1_time_limit.pack()

        player2_turn_limit_label = tk.Label(master=frame, text="Player2 Turn Limit (seconds)")
        player2_turn_limit_label.pack()
        self._player2_time_limit = tk.Entry(master=frame, width=20)
        self._player2_time_limit.insert(0, "10")
        self._player2_time_limit.pack()

    def pack_submit_button(self):
        button = tk.Button(master=self._root, text="Apply Game Configuration!", fg="White", bg="Green")
        button.grid(row=4, column=0)
        button.bind("<Button-1>", self.handle_submit)

    def handle_submit(self, event):
        starting_position = self._starting_pos.get()
        player1_mode = self._player1_mode.get()
        player2_mode = self._player2_mode.get()
        move_limit_per_player = int(self._player_move_limit.get())
        player1_time_limit = int(self._player1_time_limit.get())
        player2_time_limit = int(self._player2_time_limit.get())

        self._game.set_start_positions(SettingsMenu.get_starting_positions(starting_position))
        self._game.set_player1(SettingsMenu.construct_player(
            move_limit_per_player, player1_time_limit, player1_mode))
        self._game.set_player2(SettingsMenu.construct_player(
            move_limit_per_player, player2_time_limit, player2_mode))

        self._root.destroy()  # close the settings window

    @staticmethod
    def get_starting_positions(pos):
        """
        Return a Starting Position enum
        :param pos: a string
        :return:
        """
        if pos == "StartingPositions.DEFAULT":
            return StartingPositions.DEFAULT
        elif pos == "StartingPositions.GERMAN":
            return StartingPositions.GERMAN
        else:
            return StartingPositions.BELGIAN

    @staticmethod
    def construct_player(move_limit, time_limit, player_mode) -> player.Player:
        """
        make a player object based on the configuration
        :return: a Player object
        """
        if player_mode == "PlayerMode.AI":
            return AIPlayer(move_limit, time_limit)
        else:
            return HumanPlayer(move_limit, time_limit)
