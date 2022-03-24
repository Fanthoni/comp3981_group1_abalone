from enum import Enum, auto
from move import Move
import copy
from file_writer import FileOperator


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
    DEFAULT = "Default"
    GERMAN = "German Daisies"
    BELGIAN = "Belgian Daisies"
    EMPTY = auto()


class MoveDirections(Enum):
    """
    Contains all possible movement directions in a hex grid.
    """
    NW = (1, 0)
    NE = (1, 1)
    W = (0, -1)
    E = (0, 1)
    SW = (-1, -1)
    SE = (-1, 0)


class Board:
    def __init__(self, board_choice):
        self._board = Board.make_board(board_choice)
        self._blue_score = 0
        self._red_score = 0

    @property
    def board(self):
        """
        Board state property.

        :return: board dict
        """
        return self._board

    @classmethod
    def make_board(cls, board_choice):
        """
        Get board state.

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
                ('A', 6): BoardTile.BORDER, ('B', 0): BoardTile.BORDER, ('B', 1): BoardTile.BLUE,
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
                ('I', 10): BoardTile.BORDER, ('J', 5): BoardTile.BORDER, ('J', 6): BoardTile.BORDER,
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
                ('J', 7): BoardTile.BORDER, ('J', 8): BoardTile.BORDER, ('J', 9): BoardTile.BORDER,
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

    def update_board(self, move: Move):
        """
        Updates the current board state according to the move.

        :param move: a Move object
        """
        pass

    @classmethod
    def __get_indentation_space(cls, row):
        """
        Helper function to print_board formation.

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
        Helper function to print_board labelling.

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
        Prints the current board state.
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
        Returns red score.

        :return: int
        """
        return self._red_score

    @property
    def blue_score(self):
        """
        Returns blue score.

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
        Sorted position list of all the black tiles, then all the white tiles.

        :return: String
        """
        white_tiles = self._get_board_tile(BoardTile.RED)
        black_tiles = self._get_board_tile(BoardTile.BLUE)

        return (black_tiles + white_tiles)[0:-1]  # Remove last comma

    def _get_board_tile(self, board_tile):
        """
        Returns all the selected board tile's position on the board in the format: {row}{column}{color}.

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

    def get_marble_groups(self, colour: BoardTile) -> set:
        """
        Returns a set containing all possible groupings of marbles.

        :param colour: a BoardTile Enum, the colour of the side to generate groups for.
        :return: a set containing all possible groupings of marbles.
        """
        groups = set()
        for key, value in self.board.items():
            if value == colour:
                for direction in MoveDirections:
                    groups.add(self._find_groups(key, direction.value, colour))
        return groups

    def _find_groups(self, key: tuple, direction: tuple, colour: BoardTile) -> tuple:
        """
        Search for other marbles nearby that can form a group.

        :param key: a tuple, the 'starting' marble for the grouping.
        :param direction: a tuple, the direction the grouping moves in from the starting marble.
        :param colour: a BoardTile Enum, the colour of the marble group.
        :return: a tuple, contains the co-ordinates (keys) of the grouping.
        """
        row, col = ord(key[0]), key[1]
        row_move, col_move = direction

        temp = [key]

        for i in range(2):
            # Up to two more marbles can be added to the group.
            row = row + row_move
            col = col + col_move
            new_key = (chr(row), col)

            if self.board.get(new_key) == colour:
                temp.append(new_key)
            else:
                break

        if len(temp) == 1:
            return key
        return tuple(sorted(temp))

    def get_board_value(self, tile: tuple) -> BoardTile:
        """
        Return the BoardTile value of a given space on the board.

        :param tile: a tuple, the tile that you want the value for.
        :return: BoardTile
        """
        return self._board[tile]

    @classmethod
    def get_next_tile(cls, tile: tuple, direction: tuple) -> tuple:
        """
        Get the co-ordinate of the next tile in the given direction.

        :param tile: a tuple,
        :param direction: a tuple, the direction of the tile you want the value of.
        :return: a tuple
        """
        current = list(tile)  # Convert to list for modification
        next_tile = tuple([chr(ord(current[0]) + direction[0]), current[1] + direction[1]])
        return next_tile

    def get_next_tile_value(self, tile: tuple, direction: tuple) -> BoardTile:
        """
        Get the value of the next tile in a given direction.

        :param tile: a tuple,
        :param direction: a tuple, the direction of the tile you want the value of.
        :return: BoardTile
        """
        return self.get_board_value(self.get_next_tile(tile, direction))

    @classmethod
    def _get_single_group(cls, group: set) -> set:
        """
        Returns all single marbles from a set of all possible groupings of marbles.

        :param group: a set
        :return: a set, containing only single marbles.
        """
        return set(filter(lambda combination: type(combination[0]) == str, group))

    @classmethod
    def _get_duo_group(cls, group: set) -> set:
        """
        Returns all groups containing two marbles from a set of all possible groupings of marbles.

        :param group: a set
        :return: a set, containing only groups of two marbles.
        """
        return set(filter(lambda combination: len(combination) == 2 and type(combination[0]) == tuple, group))

    @classmethod
    def _get_trio_group(cls, group: set) -> set:
        """
        Returns all groups containing three marbles from a set of all possible groupings of marbles.

        :param group: a set
        :return: a set, containing only groups of two marbles.
        """
        return set(filter(lambda combination: len(combination) == 3, group))

    @classmethod
    def _is_marble_group_in_correct_direction(cls, marble_group, direction):
        return (ord(marble_group[1][0]) - ord(marble_group[0][0]), marble_group[1][1] - marble_group[0][1]) == direction

    def get_board_after_move(self, move):
        board_copy = copy.deepcopy(self)

        if len(move.marble_group) == 1 or move.direction.value in self._get_marble_group_inline_directions(move.marble_group):
            if len(move.marble_group) > 1 and not self._is_marble_group_in_correct_direction(move.marble_group, move.direction.value):
                return self.get_board_after_move(Move(tuple(reversed(move.marble_group)), move.direction))

            colour_queue = []
            current_tile = move.marble_group[0]
            current_tile_value = self.board[current_tile]

            while current_tile_value not in [BoardTile.EMPTY, BoardTile.BORDER]:
                colour_queue.append(current_tile_value)
                current_tile = self.get_next_tile(current_tile, move.direction.value)
                current_tile_value = self.board[current_tile]

            starting_tile = move.marble_group[0]
            current_tile = self.get_next_tile(starting_tile, move.direction.value)
            while len(colour_queue) > 0:
                colour_to_fill_in = colour_queue.pop(0)
                board_copy.board[current_tile] = colour_to_fill_in if board_copy.board[current_tile] != BoardTile.BORDER else BoardTile.BORDER
                current_tile = self.get_next_tile(current_tile, move.direction.value)
            board_copy.board[starting_tile] = BoardTile.EMPTY
        else:
            for marble in move.marble_group:
                colour_to_fill_in = self.board[marble]
                next_tile = self.get_next_tile(marble, move.direction.value)
                board_copy.board[next_tile] = colour_to_fill_in
                board_copy.board[marble] = BoardTile.EMPTY
        return board_copy

    def generate_moves(self, group: set):
        """
        Generate all possible moves for a marble or set of marbles.

        :param input_file_name: a String
        :param group: a set
        :return: a list, contains all valid move directions for the group.
        """
        single_group = self._get_single_group(group)
        duo_group = self._get_duo_group(group)
        trio_group = self._get_trio_group(group)

        valid_moves = []
        for marble in single_group:
            move_directions = self._generate_single_moves(marble)
            for direction in move_directions:
                move = Move([marble], direction)
                valid_moves.append(move)

        for marble in duo_group:
            move_directions = self._generate_duo_moves(marble)
            for direction in move_directions:
                move = Move(marble, direction)
                valid_moves.append(move)

        for marble in trio_group:
            move_directions = self._generate_trio_moves(marble)
            for direction in move_directions:
                move = Move(marble, direction)
                valid_moves.append(move)
        return valid_moves

    def _generate_single_moves(self, marble: tuple) -> list:
        """
        Generate all possible moves for a single marble.

        :param marble: a tuple
        :return: a list
        """
        possible_moves = []
        for direction in MoveDirections:
            if self.get_next_tile_value(marble, direction.value) == BoardTile.EMPTY:
                possible_moves.append(direction)
        return possible_moves

    @classmethod
    def _get_marble_group_inline_directions(cls, marble_group: tuple) -> tuple:
        """
        Returns two MoveDirections for an inline marble group
        :param marble_group: a tuple
        :return: two opposite MoveDirection
        """
        first_marble = marble_group[0]
        second_marble = marble_group[1]

        direction = [ord(second_marble[0]) - ord(first_marble[0]), second_marble[1] - first_marble[1]]
        opposite_direction = list(map(lambda x: x * -1, direction))
        return tuple(direction), tuple(opposite_direction)

    def _generate_duo_moves(self, marble_group: tuple) -> list:
        """
        Generate all possible moves for a column of two marbles.

        :param marble_group: a tuple
        :return: a list
        """
        # Get marbles. Cast to list to enable modification.
        group_tail = marble_group[0]
        group_head = marble_group[1]
        # Get colour of the grouping.
        group_colour = self.get_board_value(marble_group[0])
        opposite_colour = BoardTile.BLUE if group_colour == BoardTile.RED else BoardTile.RED

        possible_moves = []
        for direction in MoveDirections:
            if direction.value in self._get_marble_group_inline_directions(marble_group):
                # Checks in-line movement for 2 marbles
                if self.get_next_tile_value(group_tail, direction.value) == BoardTile.EMPTY or \
                        self.get_next_tile_value(group_head, direction.value) == BoardTile.EMPTY:
                    possible_moves.append(direction)
                # Checks for 2-1 Sumito
                next_tail = self.get_next_tile(group_tail, direction.value)
                next_head = self.get_next_tile(group_head, direction.value)

                if self.get_next_tile_value(group_tail, direction.value) == opposite_colour \
                        and self.get_next_tile_value(next_tail, direction.value) in [BoardTile.EMPTY, BoardTile.BORDER] \
                        or self.get_next_tile_value(group_head, direction.value) == opposite_colour \
                        and self.get_next_tile_value(next_head, direction.value) in [BoardTile.EMPTY, BoardTile.BORDER]:
                    possible_moves.append(direction)
            else:
                # Check for possible sidesteps.
                if self.get_next_tile_value(group_tail, direction.value) == BoardTile.EMPTY and \
                        self.get_next_tile_value(group_head, direction.value) == BoardTile.EMPTY:
                    possible_moves.append(direction)
        return possible_moves

    def _generate_trio_moves(self, marble_group: tuple) -> list:
        """
        Generate all possible moves for a column of three marbles.

        :param marble_group: a tuple
        :return: a list
        """
        # Get head and tail of the column.
        group_tail = marble_group[0]
        group_head = marble_group[2]

        # Get colour of the grouping.
        group_colour = self.get_board_value(marble_group[0])
        opposite_colour = BoardTile.BLUE if group_colour == BoardTile.RED else BoardTile.RED

        possible_moves = []
        for direction in MoveDirections:
            if direction.value in self._get_marble_group_inline_directions(marble_group):
                # Checks in-line movement for 2 marbles
                if self.get_next_tile_value(group_tail, direction.value) == BoardTile.EMPTY or \
                        self.get_next_tile_value(group_head, direction.value) == BoardTile.EMPTY:
                    possible_moves.append(direction)
                # Checks for 3-1 Sumito
                next_tail = self.get_next_tile(group_tail, direction.value)
                next_head = self.get_next_tile(group_head, direction.value)

                if self.get_next_tile_value(group_tail, direction.value) == opposite_colour \
                        and self.get_next_tile_value(next_tail, direction.value) in [BoardTile.EMPTY, BoardTile.BORDER] \
                        or self.get_next_tile_value(group_head, direction.value) == opposite_colour \
                        and self.get_next_tile_value(next_head, direction.value) in [BoardTile.EMPTY, BoardTile.BORDER]:
                    possible_moves.append(direction)

                # Checks for 3-2 Sumito
                next_next_tail = self.get_next_tile(next_tail, direction.value)
                next_next_head = self.get_next_tile(next_head, direction.value)
                if self.get_next_tile_value(group_tail, direction.value) == opposite_colour \
                        and self.get_next_tile_value(next_tail, direction.value) == opposite_colour \
                        and self.get_next_tile_value(next_next_tail, direction.value) in [BoardTile.EMPTY, BoardTile.BORDER] \
                        or self.get_next_tile_value(group_head, direction.value) == opposite_colour \
                        and self.get_next_tile_value(next_head, direction.value) == opposite_colour \
                        and self.get_next_tile_value(next_next_head, direction.value) in [BoardTile.EMPTY, BoardTile.BORDER]:
                    possible_moves.append(direction)
            else:
                # Check for possible sidesteps.
                if self.get_next_tile_value(group_tail, direction.value) == BoardTile.EMPTY \
                        and self.get_next_tile_value(marble_group[1], direction.value) == BoardTile.EMPTY \
                        and self.get_next_tile_value(group_head, direction.value) == BoardTile.EMPTY:
                    possible_moves.append(direction)
        return possible_moves

    def generate_all_possible_moves_and_resulting_boards(self, current_player, input_file_name):
        """
        Generate .move and .board file for all the possible moves in the current board state when it's
        the current_player's turn.

        .move and .board file naming will follow the input_file_name naming.

        :param current_player: a String
        :param input_file_name: a String
        :return:
        """
        marble_groups = self.get_marble_groups(
            BoardTile.BLUE if current_player == "Black" else BoardTile.RED)
        moves = self.generate_moves(marble_groups)

        move_file_writer = FileOperator(FileOperator.get_move_file_name(input_file_name))
        board_file_writer = FileOperator(FileOperator.get_board_file_name(input_file_name))

        board_results = []
        for move in moves:
            move_file_writer.write_move(move)
            board_results.append(self.get_board_after_move(move))

        for board in board_results:
            board_file_writer.write_board(board)

        print(f"move and board files are generated under testOutput directory")