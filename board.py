from enum import Enum, auto


class BoardTile(Enum):
    """
    Red = White
    Blue = Black
    """
    RED = "\U0001F7E5"
    BLUE = "\U0001F7E6"
    EMPTY = "\U0001F7E9"
    BORDER = ""


class StartingPositions(Enum):
    DEFAULT = auto()
    GERMAN = auto()
    BELGIAN = auto()
    EMPTY = auto()


class Board:
    def __init__(self, board_choice):
        self._board = Board.make_board(board_choice)
        self._blue_score = 0
        self._red_score = 0

    @property
    def board(self):
        """
        Board state property
        :return: board dict
        """
        return self._board

    @classmethod
    def make_board(cls, board_choice):
        """
        Get board state
        :param board_choice: a StartingPosition
        :return: board state of the given board_choice
        """
        board = None
        # Default board state
        if board_choice == StartingPositions.EMPTY:
            board = {
                ('A', 0): BoardTile.BORDER, ('A', 1): BoardTile.EMPTY, ('A', 2): BoardTile.EMPTY,
                ('A', 3): BoardTile.EMPTY, ('A', 4): BoardTile.EMPTY, ('A', 5): BoardTile.EMPTY,
                ('A', 6): BoardTile.BORDER, ('B', 0): BoardTile.BORDER, ('B', 1): BoardTile.EMPTY,
                ('B', 2): BoardTile.EMPTY, ('B', 3): BoardTile.EMPTY, ('B', 4): BoardTile.EMPTY,
                ('B', 5): BoardTile.EMPTY, ('B', 6): BoardTile.EMPTY, ('B', 7): BoardTile.BORDER,
                ('C', 0): BoardTile.BORDER, ('C', 1): BoardTile.EMPTY, ('C', 2): BoardTile.EMPTY,
                ('C', 3): BoardTile.EMPTY, ('C', 4): BoardTile.EMPTY, ('C', 5): BoardTile.EMPTY,
                ('C', 6): BoardTile.EMPTY, ('C', 7): BoardTile.EMPTY, ('C', 8): BoardTile.BORDER,
                ('D', 0): BoardTile.BORDER, ('D', 1): BoardTile.EMPTY, ('D', 2): BoardTile.EMPTY,
                ('D', 3): BoardTile.EMPTY, ('D', 4): BoardTile.EMPTY, ('D', 5): BoardTile.EMPTY,
                ('D', 6): BoardTile.EMPTY, ('D', 7): BoardTile.EMPTY, ('D', 8): BoardTile.EMPTY,
                ('D', 9): BoardTile.BORDER, ('E', 0): BoardTile.BORDER, ('E', 1): BoardTile.EMPTY,
                ('E', 2): BoardTile.EMPTY, ('E', 3): BoardTile.EMPTY, ('E', 4): BoardTile.EMPTY,
                ('E', 5): BoardTile.EMPTY, ('E', 6): BoardTile.EMPTY, ('E', 7): BoardTile.EMPTY,
                ('E', 8): BoardTile.EMPTY, ('E', 9): BoardTile.EMPTY, ('E', 10): BoardTile.BORDER,
                ('F', 1): BoardTile.BORDER, ('F', 2): BoardTile.EMPTY, ('F', 3): BoardTile.EMPTY,
                ('F', 4): BoardTile.EMPTY, ('F', 5): BoardTile.EMPTY, ('F', 6): BoardTile.EMPTY,
                ('F', 7): BoardTile.EMPTY, ('F', 8): BoardTile.EMPTY, ('F', 9): BoardTile.EMPTY,
                ('F', 10): BoardTile.BORDER, ('G', 2): BoardTile.BORDER, ('G', 3): BoardTile.EMPTY,
                ('G', 4): BoardTile.EMPTY, ('G', 5): BoardTile.EMPTY, ('G', 6): BoardTile.EMPTY,
                ('G', 7): BoardTile.EMPTY, ('G', 8): BoardTile.EMPTY, ('G', 9): BoardTile.EMPTY,
                ('G', 10): BoardTile.BORDER, ('H', 3): BoardTile.BORDER, ('H', 4): BoardTile.EMPTY,
                ('H', 5): BoardTile.EMPTY, ('H', 6): BoardTile.EMPTY, ('H', 7): BoardTile.EMPTY,
                ('H', 8): BoardTile.EMPTY, ('H', 9): BoardTile.EMPTY, ('H', 10): BoardTile.BORDER,
                ('I', 4): BoardTile.BORDER, ('I', 5): BoardTile.EMPTY, ('I', 6): BoardTile.EMPTY,
                ('I', 7): BoardTile.EMPTY, ('I', 8): BoardTile.EMPTY, ('I', 9): BoardTile.EMPTY,
                ('I', 10): BoardTile.BORDER, ('J', 5): BoardTile.BORDER, ('J', 6): BoardTile.BORDER,
                ('J', 7): BoardTile.BORDER, ('J', 8): BoardTile.BORDER, ('J', 9): BoardTile.BORDER,
                ('J', 10): BoardTile.BORDER, ('@', 0): BoardTile.BORDER, ('@', 1): BoardTile.BORDER,
                ('@', 2): BoardTile.BORDER, ('@', 3): BoardTile.BORDER, ('@', 4): BoardTile.BORDER,
                ('@', 5): BoardTile.BORDER
            }
        # Belgian Daisy state
        elif board_choice == StartingPositions.BELGIAN:
            board = {
                ('A', 0): BoardTile.BORDER, ('A', 1): BoardTile.BLUE, ('A', 2): BoardTile.BLUE,
                ('A', 3): BoardTile.EMPTY, ('A', 4): BoardTile.RED, ('A', 5): BoardTile.RED,
                ('A', 6): BoardTile.BORDER,('B', 0): BoardTile.BORDER, ('B', 1): BoardTile.BLUE,
                ('B', 2): BoardTile.BLUE, ('B', 3): BoardTile.BLUE, ('B', 4): BoardTile.RED,
                ('B', 5): BoardTile.RED, ('B', 6): BoardTile.RED, ('B', 7): BoardTile.BORDER,
                ('C', 0): BoardTile.BORDER, ('C', 1): BoardTile.EMPTY, ('C', 2): BoardTile.BLUE,
                ('C', 3): BoardTile.BLUE, ('C', 4): BoardTile.EMPTY, ('C', 5): BoardTile.RED,
                ('C', 6): BoardTile.RED, ('C', 7): BoardTile.EMPTY, ('C', 8): BoardTile.BORDER,
                ('D', 0): BoardTile.BORDER, ('D', 1): BoardTile.EMPTY, ('D', 2): BoardTile.EMPTY,
                ('D', 3): BoardTile.EMPTY, ('D', 4): BoardTile.EMPTY, ('D', 5): BoardTile.EMPTY,
                ('D', 6): BoardTile.EMPTY, ('D', 7): BoardTile.EMPTY, ('D', 8): BoardTile.EMPTY,
                ('D', 9): BoardTile.BORDER, ('E', 0): BoardTile.BORDER, ('E', 1): BoardTile.EMPTY,
                ('E', 2): BoardTile.EMPTY, ('E', 3): BoardTile.EMPTY, ('E', 4): BoardTile.EMPTY,
                ('E', 5): BoardTile.EMPTY, ('E', 6): BoardTile.EMPTY, ('E', 7): BoardTile.EMPTY,
                ('E', 8): BoardTile.EMPTY, ('E', 9): BoardTile.EMPTY, ('E', 10): BoardTile.BORDER,
                ('F', 1): BoardTile.BORDER, ('F', 2): BoardTile.EMPTY, ('F', 3): BoardTile.EMPTY,
                ('F', 4): BoardTile.EMPTY, ('F', 5): BoardTile.EMPTY, ('F', 6): BoardTile.EMPTY,
                ('F', 7): BoardTile.EMPTY, ('F', 8): BoardTile.EMPTY, ('F', 9): BoardTile.EMPTY,
                ('F', 10): BoardTile.BORDER, ('G', 2): BoardTile.BORDER, ('G', 3): BoardTile.EMPTY,
                ('G', 4): BoardTile.RED, ('G', 5): BoardTile.RED, ('G', 6): BoardTile.EMPTY,
                ('G', 7): BoardTile.BLUE, ('G', 8): BoardTile.BLUE, ('G', 9): BoardTile.EMPTY,
                ('G', 10): BoardTile.BORDER, ('H', 3): BoardTile.BORDER, ('H', 4): BoardTile.RED,
                ('H', 5): BoardTile.RED, ('H', 6): BoardTile.RED, ('H', 7): BoardTile.BLUE,
                ('H', 8): BoardTile.BLUE, ('H', 9): BoardTile.BLUE, ('H', 10): BoardTile.BORDER,
                ('I', 4): BoardTile.BORDER, ('I', 5): BoardTile.RED, ('I', 6): BoardTile.RED,
                ('I', 7): BoardTile.EMPTY, ('I', 8): BoardTile.BLUE, ('I', 9): BoardTile.BLUE,
                ('I', 10): BoardTile.BORDER,  ('J', 5): BoardTile.BORDER, ('J', 6): BoardTile.BORDER,
                ('J', 7): BoardTile.BORDER, ('J', 8): BoardTile.BORDER, ('J', 9): BoardTile.BORDER,
                ('J', 10): BoardTile.BORDER, ('@', 0): BoardTile.BORDER, ('@', 1): BoardTile.BORDER,
                ('@', 2): BoardTile.BORDER, ('@', 3): BoardTile.BORDER, ('@', 4): BoardTile.BORDER,
                ('@', 5): BoardTile.BORDER
            }
        # german daisy state
        elif board_choice == StartingPositions.GERMAN:
            board = {
                ('A', 0): BoardTile.BORDER, ('A', 1): BoardTile.EMPTY, ('A', 2): BoardTile.EMPTY,
                ('A', 3): BoardTile.EMPTY, ('A', 4): BoardTile.EMPTY, ('A', 5): BoardTile.EMPTY,
                ('A', 6): BoardTile.BORDER, ('B', 0): BoardTile.BORDER, ('B', 1): BoardTile.BLUE,
                ('B', 2): BoardTile.BLUE, ('B', 3): BoardTile.EMPTY, ('B', 4): BoardTile.EMPTY,
                ('B', 5): BoardTile.RED, ('B', 6): BoardTile.RED, ('B', 7): BoardTile.BORDER,
                ('C', 0): BoardTile.BORDER, ('C', 1): BoardTile.BLUE, ('C', 2): BoardTile.BLUE,
                ('C', 3): BoardTile.BLUE, ('C', 4): BoardTile.EMPTY, ('C', 5): BoardTile.RED,
                ('C', 6): BoardTile.RED, ('C', 7): BoardTile.RED, ('C', 8): BoardTile.BORDER,
                ('D', 0): BoardTile.BORDER, ('D', 1): BoardTile.EMPTY, ('D', 2): BoardTile.BLUE,
                ('D', 3): BoardTile.BLUE, ('D', 4): BoardTile.EMPTY, ('D', 5): BoardTile.EMPTY,
                ('D', 6): BoardTile.RED, ('D', 7): BoardTile.RED, ('D', 8): BoardTile.EMPTY,
                ('D', 9): BoardTile.BORDER, ('E', 0): BoardTile.BORDER, ('E', 1): BoardTile.EMPTY,
                ('E', 2): BoardTile.EMPTY, ('E', 3): BoardTile.EMPTY, ('E', 4): BoardTile.EMPTY,
                ('E', 5): BoardTile.EMPTY, ('E', 6): BoardTile.EMPTY, ('E', 7): BoardTile.EMPTY,
                ('E', 8): BoardTile.EMPTY, ('E', 9): BoardTile.EMPTY, ('E', 10): BoardTile.BORDER,
                ('F', 1): BoardTile.BORDER, ('F', 2): BoardTile.EMPTY, ('F', 3): BoardTile.RED,
                ('F', 4): BoardTile.RED, ('F', 5): BoardTile.EMPTY, ('F', 6): BoardTile.EMPTY,
                ('F', 7): BoardTile.BLUE, ('F', 8): BoardTile.BLUE, ('F', 9): BoardTile.EMPTY,
                ('F', 10): BoardTile.BORDER, ('G', 2): BoardTile.BORDER, ('G', 3): BoardTile.RED,
                ('G', 4): BoardTile.RED, ('G', 5): BoardTile.RED, ('G', 6): BoardTile.EMPTY,
                ('G', 7): BoardTile.BLUE, ('G', 8): BoardTile.BLUE, ('G', 9): BoardTile.BLUE,
                ('G', 10): BoardTile.BORDER, ('H', 3): BoardTile.BORDER, ('H', 4): BoardTile.RED,
                ('H', 5): BoardTile.RED, ('H', 6): BoardTile.EMPTY, ('H', 7): BoardTile.EMPTY,
                ('H', 8): BoardTile.BLUE, ('H', 9): BoardTile.BLUE, ('H', 10): BoardTile.BORDER,
                ('I', 4): BoardTile.BORDER, ('I', 5): BoardTile.EMPTY, ('I', 6): BoardTile.EMPTY,
                ('I', 7): BoardTile.EMPTY, ('I', 8): BoardTile.EMPTY, ('I', 9): BoardTile.EMPTY,
                ('I', 10): BoardTile.BORDER, ('J', 5): BoardTile.BORDER, ('J', 6): BoardTile.BORDER,
                ('J', 7): BoardTile.BORDER,('J', 8): BoardTile.BORDER, ('J', 9): BoardTile.BORDER,
                ('J', 10): BoardTile.BORDER, ('@', 0): BoardTile.BORDER, ('@', 1): BoardTile.BORDER,
                ('@', 2): BoardTile.BORDER, ('@', 3): BoardTile.BORDER, ('@', 4): BoardTile.BORDER,
                ('@', 5): BoardTile.BORDER
            }
        else:  # Default Board
            board = {
                ('A', 0): BoardTile.BORDER, ('A', 1): BoardTile.BLUE, ('A', 2): BoardTile.BLUE,
                ('A', 3): BoardTile.BLUE, ('A', 4): BoardTile.BLUE, ('A', 5): BoardTile.BLUE,
                ('A', 6): BoardTile.BORDER, ('B', 0): BoardTile.BORDER, ('B', 1): BoardTile.BLUE,
                ('B', 2): BoardTile.BLUE, ('B', 3): BoardTile.BLUE, ('B', 4): BoardTile.BLUE,
                ('B', 5): BoardTile.BLUE, ('B', 6): BoardTile.BLUE, ('B', 7): BoardTile.BORDER,
                ('C', 0): BoardTile.BORDER, ('C', 1): BoardTile.EMPTY, ('C', 2): BoardTile.EMPTY,
                ('C', 3): BoardTile.BLUE, ('C', 4): BoardTile.BLUE, ('C', 5): BoardTile.BLUE,
                ('C', 6): BoardTile.EMPTY, ('C', 7): BoardTile.EMPTY, ('C', 8): BoardTile.BORDER,
                ('D', 0): BoardTile.BORDER, ('D', 1): BoardTile.EMPTY, ('D', 2): BoardTile.EMPTY,
                ('D', 3): BoardTile.EMPTY, ('D', 4): BoardTile.EMPTY, ('D', 5): BoardTile.EMPTY,
                ('D', 6): BoardTile.EMPTY, ('D', 7): BoardTile.EMPTY, ('D', 8): BoardTile.EMPTY,
                ('D', 9): BoardTile.BORDER, ('E', 0): BoardTile.BORDER, ('E', 1): BoardTile.EMPTY,
                ('E', 2): BoardTile.EMPTY, ('E', 3): BoardTile.EMPTY, ('E', 4): BoardTile.EMPTY,
                ('E', 5): BoardTile.EMPTY, ('E', 6): BoardTile.EMPTY, ('E', 7): BoardTile.EMPTY,
                ('E', 8): BoardTile.EMPTY, ('E', 9): BoardTile.EMPTY, ('E', 10): BoardTile.BORDER,
                ('F', 1): BoardTile.BORDER, ('F', 2): BoardTile.EMPTY, ('F', 3): BoardTile.EMPTY,
                ('F', 4): BoardTile.EMPTY, ('F', 5): BoardTile.EMPTY, ('F', 6): BoardTile.EMPTY,
                ('F', 7): BoardTile.EMPTY, ('F', 8): BoardTile.EMPTY, ('F', 9): BoardTile.EMPTY,
                ('F', 10): BoardTile.BORDER, ('G', 2): BoardTile.BORDER, ('G', 3): BoardTile.EMPTY,
                ('G', 4): BoardTile.EMPTY, ('G', 5): BoardTile.RED, ('G', 6): BoardTile.RED,
                ('G', 7): BoardTile.RED, ('G', 8): BoardTile.EMPTY, ('G', 9): BoardTile.EMPTY,
                ('G', 10): BoardTile.BORDER, ('H', 3): BoardTile.BORDER, ('H', 4): BoardTile.RED,
                ('H', 5): BoardTile.RED, ('H', 6): BoardTile.RED, ('H', 7): BoardTile.RED,
                ('H', 8): BoardTile.RED, ('H', 9): BoardTile.RED, ('H', 10): BoardTile.BORDER,
                ('I', 4): BoardTile.BORDER, ('I', 5): BoardTile.RED, ('I', 6): BoardTile.RED,
                ('I', 7): BoardTile.RED, ('I', 8): BoardTile.RED, ('I', 9): BoardTile.RED,
                ('I', 10): BoardTile.BORDER, ('J', 5): BoardTile.BORDER, ('J', 6): BoardTile.BORDER,
                ('J', 7): BoardTile.BORDER, ('J', 8): BoardTile.BORDER, ('J', 9): BoardTile.BORDER,
                ('J', 10): BoardTile.BORDER, ('@', 0): BoardTile.BORDER, ('@', 1): BoardTile.BORDER,
                ('@', 2): BoardTile.BORDER, ('@', 3): BoardTile.BORDER, ('@', 4): BoardTile.BORDER,
                ('@', 5): BoardTile.BORDER
            }
        return board

    def update_board(self, move):
        """
        Updates the current board state according to the move
        :param move: a Move object
        """
        pass

    @classmethod
    def __get_indentation_space(cls, row):
        """
        Helper function to print_board formation
        :param row: a char
        :return: the number of spaces needed to be print before the BoardTile values
        """
        match row:
            case 'I':
                return 10
            case 'H':
                return 8
            case 'G':
                return 6
            case 'F':
                return 5
            case 'E':
                return 3
            case 'D':
                return 5
            case 'C':
                return 6
            case 'B':
                return 8
            case 'A':
                return 10

    @classmethod
    def __get_column_label_value(cls, row):
        """
        Helper function to print_board labelling
        :param row: a String row value
        :return: a string with the current column label if exists. Empty string otherwise
        """
        match row:
            case 'D':
                return "9"
            case 'C':
                return "8"
            case 'B':
                return "7"
            case 'A':
                return "6"
            case _:
                return ""

    def print_board(self):
        """
        Prints the current board state
        """
        for row in range(ord('I'), ord('@'), -1):
            current_row = chr(row)
            current_row_keys = sorted([key for key in self._board.keys() if current_row in key])
            indent_space_amount = Board.__get_indentation_space(current_row)
            current_row_string_value = " " * indent_space_amount + current_row

            for key in current_row_keys:
                if self._board[key].value is not BoardTile.BORDER:
                    current_row_string_value += self._board[key].value + " "
            current_row_string_value += "\b" + Board.__get_column_label_value(current_row)
            print(current_row_string_value)

        # Prints the last row label
        print(" " * 14 + "1  2  3  4  5")

    @property
    def red_score(self):
        """
        Returns red score
        :return: int
        """
        return self._red_score

    @property
    def blue_score(self):
        """
        Returns blue score
        :return: int
        """
        return self._blue_score

    def setup_board_from_moves(self, moves):
        """
        Translate a board setup from an array of moves into a board layout.
        :param moves: list of moves
        :return: None
        """
        for move in moves:
            row = move[0]
            col = int(move[1])
            color = move[2]

            self._board[(row, col)] = BoardTile.RED if color == "w" else BoardTile.BLUE

    def get_board_information(self):
        """
        Sorted position list of all the black tiles, then all the white tiles
        :return: String
        """
        white_tiles = self._get_board_tile(BoardTile.RED)
        black_tiles = self._get_board_tile(BoardTile.BLUE)

        return (black_tiles + white_tiles)[0:-1]  # Remove last comma

    def _get_board_tile(self, board_tile):
        """
        Returns all the selected board tile's position on the board in the format: "{row}{column}{color}.
        :param board_tile: BoardTile enum
        :return: Comma separated string
        """
        string = ""
        if board_tile == BoardTile.RED:
            color = "w"
        elif board_tile == BoardTile.BLUE:
            color = "b"
        else:
            return

        for key, value in self._board.items():
            row, col = key
            if value == board_tile:
                string += f"{row}{col}{color},"

        return string

    def get_marble_groups(self):
        directions = [(1, 1), (1, 0), (0, 1), (1, 0), (0, -1), (-1, -1)]
        groups = set()
        for key, value in self.board.items():
            if value == BoardTile.RED:
                for direction in directions:
                    groups.add(self.find_groups(key, direction))
        return groups

    def find_groups(self, key, direction):
        row, col = ord(key[0]), key[1]
        row_move, col_move = direction

        temp = [key]

        for i in range(3):
            row = row + row_move
            col = col + col_move
            new_key = (chr(row), col)

            if self.board.get(new_key) == BoardTile.RED:
                temp.append(new_key)
            else:
                break

        if len(temp) == 1:
            return key
        return tuple(sorted(temp))

