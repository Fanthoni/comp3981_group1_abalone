from enum import Enum, auto


class BoardTile(Enum):
    RED = auto()
    BLUE = auto()
    EMPTY = auto()
    BORDER = auto()

class StartingPositions(Enum):
    DEFAULT = auto()
    GERMAN = auto()
    BELGIAN = auto()


class Board:
    def __init__(self):
        self._board = None
        self._blue_score = 0
        self._red_score = 0

    # Current use's int to choose initial board state; change later to agreed
    # upon emum type
    def make_board(self, board_choice):
        my_board = None

        # Default board state
        if board_choice == 0:
            my_board = {
                ('J', 5): BoardTile.BORDER, ('J', 6): BoardTile.BORDER, ('J', 7): BoardTile.BORDER, ('J', 8): BoardTile.BORDER, ('J', 9): BoardTile.BORDER, ('J', 10): BoardTile.BORDER,

                ('I', 4): BoardTile.BORDER, ('I', 5): BoardTile.RED, ('I', 6): BoardTile.RED, ('I', 7): BoardTile.RED, ('I', 8): BoardTile.RED, ('I', 9): BoardTile.RED, ('I', 10): BoardTile.BORDER,
                ('H', 3): BoardTile.BORDER, ('H', 4): BoardTile.RED, ('H', 5): BoardTile.RED, ('H', 6): BoardTile.RED, ('H', 7): BoardTile.RED, ('H', 8): BoardTile.RED, ('H', 9): BoardTile.RED, ('H', 10): BoardTile.BORDER,
                ('G', 2): BoardTile.BORDER, ('G', 3): BoardTile.EMPTY, ('G', 4): BoardTile.EMPTY, ('G', 5): BoardTile.RED, ('G', 6): BoardTile.RED, ('G', 7): BoardTile.RED, ('G', 8): BoardTile.EMPTY, ('G', 9): BoardTile.EMPTY, ('G', 10): BoardTile.BORDER,

                ('F', 1): BoardTile.BORDER, ('F', 2): BoardTile.EMPTY, ('F', 3): BoardTile.EMPTY, ('F', 4): BoardTile.EMPTY, ('F', 5): BoardTile.EMPTY, ('F', 6): BoardTile.EMPTY, ('F', 7): BoardTile.EMPTY, ('F', 8): BoardTile.EMPTY, ('F', 9): BoardTile.EMPTY, ('F', 10): BoardTile.BORDER,
                ('E', 0): BoardTile.BORDER, ('E', 1): BoardTile.EMPTY, ('E', 2): BoardTile.EMPTY, ('E', 3): BoardTile.EMPTY, ('E', 4): BoardTile.EMPTY, ('E', 5): BoardTile.EMPTY, ('E', 6): BoardTile.EMPTY, ('E', 7): BoardTile.EMPTY, ('E', 8): BoardTile.EMPTY, ('E', 9): BoardTile.EMPTY, ('E', 10): BoardTile.BORDER,
                ('D', 0): BoardTile.BORDER, ('D', 1): BoardTile.EMPTY, ('D', 2): BoardTile.EMPTY, ('D', 3): BoardTile.EMPTY, ('D', 4): BoardTile.EMPTY, ('D', 5): BoardTile.EMPTY, ('D', 6): BoardTile.EMPTY, ('D', 7): BoardTile.EMPTY, ('D', 8): BoardTile.EMPTY, ('D', 9): BoardTile.BORDER,

                ('C', 0): BoardTile.BORDER, ('C', 1): BoardTile.EMPTY, ('C', 2): BoardTile.EMPTY, ('C', 3): BoardTile.BLUE, ('C', 4): BoardTile.BLUE, ('C', 5): BoardTile.BLUE, ('C', 6): BoardTile.EMPTY, ('C', 7): BoardTile.EMPTY, ('C', 8): BoardTile.BORDER,
                ('B', 0): BoardTile.BORDER, ('B', 1): BoardTile.BLUE, ('B', 2): BoardTile.BLUE, ('B', 3): BoardTile.BLUE, ('B', 4): BoardTile.BLUE, ('B', 5): BoardTile.BLUE, ('B', 6): BoardTile.BLUE, ('B', 7): BoardTile.BORDER,
                ('A', 0): BoardTile.BORDER, ('A', 1): BoardTile.BLUE, ('A', 2): BoardTile.BLUE, ('A', 3): BoardTile.BLUE, ('A', 4): BoardTile.BLUE, ('A', 5): BoardTile.BLUE, ('A', 6): BoardTile.BORDER,

                ('@', 0): BoardTile.BORDER, ('@', 1): BoardTile.BORDER, ('@', 2): BoardTile.BORDER, ('@', 3): BoardTile.BORDER, ('@', 4): BoardTile.BORDER, ('@', 5): BoardTile.BORDER
            }
        # Belgian Daisy state
        elif board_choice == 1:
            my_board = {
                ('J', 5): BoardTile.BORDER, ('J', 6): BoardTile.BORDER, ('J', 7): BoardTile.BORDER, ('J', 8): BoardTile.BORDER, ('J', 9): BoardTile.BORDER, ('J', 10): BoardTile.BORDER,

                ('I', 4): BoardTile.BORDER, ('I', 5): BoardTile.RED, ('I', 6): BoardTile.RED, ('I', 7): BoardTile.EMPTY, ('I', 8): BoardTile.BLUE, ('I', 9): BoardTile.BLUE, ('I', 10): BoardTile.BORDER,
                ('H', 3): BoardTile.BORDER, ('H', 4): BoardTile.RED, ('H', 5): BoardTile.RED, ('H', 6): BoardTile.RED, ('H', 7): BoardTile.BLUE, ('H', 8): BoardTile.BLUE, ('H', 9): BoardTile.BLUE, ('H', 10): BoardTile.BORDER,
                ('G', 2): BoardTile.BORDER, ('G', 3): BoardTile.EMPTY, ('G', 4): BoardTile.RED, ('G', 5): BoardTile.RED, ('G', 6): BoardTile.EMPTY, ('G', 7): BoardTile.BLUE, ('G', 8): BoardTile.BLUE, ('G', 9): BoardTile.EMPTY, ('G', 10): BoardTile.BORDER,

                ('F', 1): BoardTile.BORDER, ('F', 2): BoardTile.EMPTY, ('F', 3): BoardTile.EMPTY, ('F', 4): BoardTile.EMPTY, ('F', 5): BoardTile.EMPTY, ('F', 6): BoardTile.EMPTY, ('F', 7): BoardTile.EMPTY, ('F', 8): BoardTile.EMPTY, ('F', 9): BoardTile.EMPTY, ('F', 10): BoardTile.BORDER,
                ('E', 0): BoardTile.BORDER, ('E', 1): BoardTile.EMPTY, ('E', 2): BoardTile.EMPTY, ('E', 3): BoardTile.EMPTY, ('E', 4): BoardTile.EMPTY, ('E', 5): BoardTile.EMPTY, ('E', 6): BoardTile.EMPTY, ('E', 7): BoardTile.EMPTY, ('E', 8): BoardTile.EMPTY, ('E', 9): BoardTile.EMPTY, ('E', 10): BoardTile.BORDER,
                ('D', 0): BoardTile.BORDER, ('D', 1): BoardTile.EMPTY, ('D', 2): BoardTile.EMPTY, ('D', 3): BoardTile.EMPTY, ('D', 4): BoardTile.EMPTY, ('D', 5): BoardTile.EMPTY, ('D', 6): BoardTile.EMPTY, ('D', 7): BoardTile.EMPTY, ('D', 8): BoardTile.EMPTY, ('D', 9): BoardTile.BORDER,

                ('C', 0): BoardTile.BORDER, ('C', 1): BoardTile.EMPTY, ('C', 2): BoardTile.RED, ('C', 3): BoardTile.RED, ('C', 4): BoardTile.EMPTY, ('C', 5): BoardTile.BLUE, ('C', 6): BoardTile.BLUE, ('C', 7): BoardTile.EMPTY, ('C', 8): BoardTile.BORDER,
                ('B', 0): BoardTile.BORDER, ('B', 1): BoardTile.RED, ('B', 2): BoardTile.RED, ('B', 3): BoardTile.RED, ('B', 4): BoardTile.BLUE, ('B', 5): BoardTile.BLUE, ('B', 6): BoardTile.BLUE, ('B', 7): BoardTile.BORDER,
                ('A', 0): BoardTile.BORDER, ('A', 1): BoardTile.RED, ('A', 2): BoardTile.RED, ('A', 3): BoardTile.EMPTY, ('A', 4): BoardTile.BLUE, ('A', 5): BoardTile.BLUE, ('A', 6): BoardTile.BORDER,

                ('@', 0): BoardTile.BORDER, ('@', 1): BoardTile.BORDER, ('@', 2): BoardTile.BORDER, ('@', 3): BoardTile.BORDER, ('@', 4): BoardTile.BORDER, ('@', 5): BoardTile.BORDER
            }
        # german daisy state
        elif board_choice == 2:
            my_board = {
                ('J', 5): BoardTile.BORDER, ('J', 6): BoardTile.BORDER, ('J', 7): BoardTile.BORDER, ('J', 8): BoardTile.BORDER, ('J', 9): BoardTile.BORDER, ('J', 10): BoardTile.BORDER,

                ('I', 4): BoardTile.BORDER, ('I', 5): BoardTile.EMPTY, ('I', 6): BoardTile.EMPTY, ('I', 7): BoardTile.EMPTY, ('I', 8): BoardTile.EMPTY, ('I', 9): BoardTile.EMPTY, ('I', 10): BoardTile.BORDER,

                ('H', 3): BoardTile.BORDER, ('H', 4): BoardTile.RED, ('H', 5): BoardTile.RED, ('H', 6): BoardTile.EMPTY, ('H', 7): BoardTile.EMPTY, ('H', 8): BoardTile.BLUE, ('H', 9): BoardTile.BLUE, ('H', 10): BoardTile.BORDER,
                ('G', 2): BoardTile.BORDER, ('G', 3): BoardTile.RED, ('G', 4): BoardTile.RED, ('G', 5): BoardTile.RED, ('G', 6): BoardTile.EMPTY, ('G', 7): BoardTile.BLUE, ('G', 8): BoardTile.BLUE, ('G', 9): BoardTile.BLUE, ('G', 10): BoardTile.BORDER,
                ('F', 1): BoardTile.BORDER, ('F', 2): BoardTile.EMPTY, ('F', 3): BoardTile.RED, ('F', 4): BoardTile.RED, ('F', 5): BoardTile.EMPTY, ('F', 6): BoardTile.EMPTY, ('F', 7): BoardTile.BLUE, ('F', 8): BoardTile.BLUE, ('F', 9): BoardTile.EMPTY, ('F', 10): BoardTile.BORDER,

                ('E', 0): BoardTile.BORDER, ('E', 1): BoardTile.EMPTY, ('E', 2): BoardTile.EMPTY, ('E', 3): BoardTile.EMPTY, ('E', 4): BoardTile.EMPTY, ('E', 5): BoardTile.EMPTY, ('E', 6): BoardTile.EMPTY, ('E', 7): BoardTile.EMPTY, ('E', 8): BoardTile.EMPTY, ('E', 9): BoardTile.EMPTY, ('E', 10): BoardTile.BORDER,

                ('D', 0): BoardTile.BORDER, ('D', 1): BoardTile.EMPTY, ('D', 2): BoardTile.RED, ('D', 3): BoardTile.RED, ('D', 4): BoardTile.EMPTY, ('D', 5): BoardTile.EMPTY, ('D', 6): BoardTile.BLUE, ('D', 7): BoardTile.BLUE, ('D', 8): BoardTile.EMPTY, ('D', 9): BoardTile.BORDER,
                ('C', 0): BoardTile.BORDER, ('C', 1): BoardTile.RED, ('C', 2): BoardTile.RED, ('C', 3): BoardTile.RED, ('C', 4): BoardTile.EMPTY, ('C', 5): BoardTile.BLUE, ('C', 6): BoardTile.BLUE, ('C', 7): BoardTile.BLUE, ('C', 8): BoardTile.BORDER,
                ('B', 0): BoardTile.BORDER, ('B', 1): BoardTile.RED, ('B', 2): BoardTile.RED, ('B', 3): BoardTile.EMPTY, ('B', 4): BoardTile.EMPTY, ('B', 5): BoardTile.BLUE, ('B', 6): BoardTile.BLUE, ('B', 7): BoardTile.BORDER,

                ('A', 0): BoardTile.BORDER, ('A', 1): BoardTile.EMPTY, ('A', 2): BoardTile.EMPTY, ('A', 3): BoardTile.EMPTY, ('A', 4): BoardTile.EMPTY, ('A', 5): BoardTile.EMPTY, ('A', 6): BoardTile.BORDER,

                ('@', 0): BoardTile.BORDER, ('@', 1): BoardTile.BORDER, ('@', 2): BoardTile.BORDER, ('@', 3): BoardTile.BORDER, ('@', 4): BoardTile.BORDER, ('@', 5): BoardTile.BORDER
            }

        return my_board


# print("|","\U0001F34C")
# print("","\U0001F34E")
# print("\U0001F34E")
# print("\U0001F735")
print(BoardTile.BORDER.value)
print(BoardTile.BLUE.value)
print(BoardTile.RED.value)
print(BoardTile.EMPTY.value)
# new_char = ord("J") + 1
# print(chr(new_char))
