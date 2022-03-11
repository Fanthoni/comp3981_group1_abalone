import tkinter as tk
from board import StartingPositions
from enum import Enum


class PlayerColor(Enum):
    RED = "Red",
    BLUE = "Blue"


class PlayerMode(Enum):
    HUMAN = "Human"
    AI = "AI"


class SettingsMenu:

    window_size = "550x600"

    def __init__(self):
        self._root = tk.Tk()
        self._starting_pos = tk.StringVar(value=StartingPositions.DEFAULT.value)
        self._player_color = tk.StringVar(value="Blue.v.Red")
        self._player1_mode = tk.StringVar(value=PlayerMode.HUMAN.value)
        self._player2_mode = tk.StringVar(value=PlayerMode.AI.value)
        self._player_move_limit = tk.IntVar(value=15)

        # time limit in integer second
        self._player1_time_limit = tk.IntVar(value=30)
        self._player2_time_limit = tk.IntVar(value=30)

    def display(self):
        settings_window = self._root
        settings_window.geometry(SettingsMenu.window_size)
        settings_window.title("Abalone Game Settings")

        self.pack_starting_positions_options()
        self.pack_player_color_options()

        self.pack_player1_mode_options()
        self.pack_player2_mode_options()

        self.pack_turn_and_move_limit_config()

        self.pack_submit_button()

        settings_window.mainloop()

    def pack_starting_positions_options(self):
        frame = tk.Frame(master=self._root)
        frame.grid(row=0, column=0)

        start_pos_title = tk.Label(master=frame, text="\nStarting Position")
        start_pos_title.config(font=("Roboto", 18))
        start_pos_title.pack()

        for pos in StartingPositions:
            opt = tk.Radiobutton(
                frame, text=pos.value, value=pos.value, variable=self._starting_pos
            )
            opt.pack()

    def pack_player_color_options(self):
        frame = tk.Frame(master=self._root)
        frame.grid(row=0, column=1)

        player_color_title = tk.Label(master=frame, text="\nPlayer Color")
        player_color_title.config(font=("Roboto", 18))
        player_color_title.pack()

        opt1 = tk.Radiobutton(
            frame, text="Player1 Blue(Black) - Red(White) Player2", value="Blue.v.Red", variable=self._player_color
        )
        opt2 = tk.Radiobutton(
            frame, text="Player1 Red(White) - Blue(Black) Player2", value="Red.v.Blue", variable=self._player_color
        )
        opt1.pack()
        opt2.pack()

    def pack_player1_mode_options(self):
        frame = tk.Frame(master=self._root)
        frame.grid(row=1, column=0)

        player1_mode_title = tk.Label(master=frame, text="\nPlayer1 Mode")
        player1_mode_title.config(font=("Roboto", 18))
        player1_mode_title.pack()

        human_opt = tk.Radiobutton(
            frame, text=PlayerMode.HUMAN.value, value=PlayerMode.HUMAN.value, variable=self._player1_mode
        )
        ai_opt = tk.Radiobutton(
            frame, text=PlayerMode.AI.value, value=PlayerMode.AI.value, variable=self._player1_mode
        )
        human_opt.pack()
        ai_opt.pack()

    def pack_player2_mode_options(self):
        frame = tk.Frame(master=self._root)
        frame.grid(row=1, column=1)

        player2_mode_title = tk.Label(master=frame, text="\nPlayer2 Mode")
        player2_mode_title.config(font=("Roboto", 18))
        player2_mode_title.pack()

        human_opt = tk.Radiobutton(
            frame, text=PlayerMode.HUMAN.value, value=PlayerMode.HUMAN.value, variable=self._player2_mode
        )
        ai_opt = tk.Radiobutton(
            frame, text=PlayerMode.AI.value, value=PlayerMode.AI.value, variable=self._player2_mode
        )
        human_opt.pack()
        ai_opt.pack()

    def pack_turn_and_move_limit_config(self):
        frame = tk.Frame(master=self._root)
        frame.grid(row=2, column=0)

        time_and_move_limit_config_title = tk.Label(master=frame, text="\nTime & Move Limit Config")
        time_and_move_limit_config_title.config(font=("Roboto", 18))
        time_and_move_limit_config_title.pack()

        move_limit_label = tk.Label(master=frame, text="Move Limit per Player")
        move_limit_label.pack()
        move_limit_entry = tk.Entry(master=frame, width=20)
        move_limit_entry.pack()

        player1_turn_limit_label = tk.Label(master=frame, text="Player1 Turn Limit")
        player1_turn_limit_label.pack()
        player1_turn_limit_entry = tk.Entry(master=frame, width=20)
        player1_turn_limit_entry.pack()

        player2_turn_limit_label = tk.Label(master=frame, text="Player2 Turn Limit")
        player2_turn_limit_label.pack()
        player2_turn_limit_entry = tk.Entry(master=frame, width=20)
        player2_turn_limit_entry.pack()

    def pack_submit_button(self):
        button = tk.Button(text="Apply Game Configuration!", fg="White", bg="Green")
        button.grid(row=2, column=1)
        button.bind("<Button-1>", self.handle_submit)

    def handle_submit(self, event):
        print(self._starting_pos.get())
