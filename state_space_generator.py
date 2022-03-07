from abalone import Abalone
from board import BoardTile, Board


class StateSpaceGenerator:

    @staticmethod
    def generate_next_ply_board_state(board: Board):
        """
        Generate list of board states that can be performed based on the current board state
        :param board: a Board object
        :return: A list boards
        """
        moves = {}
        resulting_boards = {}

        shore_cells = StateSpaceGenerator._find_shore_cells(board)
        two_shore_cells = StateSpaceGenerator._find_2_shore_cells(shore_cells)
        three_shore_cells = StateSpaceGenerator._find_3_shore_cells(two_shore_cells)

    @staticmethod
    def _find_shore_cells(board: Board):
        """
        Find all shore cells on this board
        :param board: a Board class
        :return: set of keys of all the shore cells
        """
        empty_cells = {cell for cell, value in board.board.items() if value == BoardTile.EMPTY}
        shore_cells = {cell for cell in empty_cells if StateSpaceGenerator._is_cell_shore_cell(board, cell)}
        return set(sorted(shore_cells))

    @staticmethod
    def _is_cell_shore_cell(board: Board, cell: tuple):
        """
        Determines whether this cell is considered as a shore cell
        :param board: a Board class
        :param cell: a cell key in tuple
        :return: true if this cell is a shore cell
        """
        board = board.board
        neighbour_cells = StateSpaceGenerator._get_all_neighbouring_cells(cell)
        for neighbour in neighbour_cells:
            if board[neighbour] not in [BoardTile.EMPTY, BoardTile.BORDER]:
                return True
        return False

    @staticmethod
    def _find_2_shore_cells(shore_cells: set):
        """
        Find all combination of 2 shore-cells, side by side based on this shore cells
        :param shore_cells: set of tuples of cell key
        :return: a set of tuples containing 2-cell-combination shore cell keys
        """
        combinations = set()
        for shore_cell in shore_cells:
            shore_cell_neighbours = StateSpaceGenerator._get_all_neighbouring_cells(shore_cell)
            for neighbour in shore_cell_neighbours:
                if neighbour in shore_cells:
                    combinations.add(tuple(sorted([shore_cell, neighbour])))
        return sorted(combinations)

    @staticmethod
    def _find_3_shore_cells(two_shore_cells):
        copy_of_two_shore_cells = two_shore_cells
        three_shore_cells = []

        for i in range(len(copy_of_two_shore_cells)):
            current_combination = copy_of_two_shore_cells.pop()
            for combination in copy_of_two_shore_cells:
                if current_combination[0] in combination or current_combination[1] in combination:
                    candidate = combination + current_combination
                    candidate = list(dict.fromkeys(candidate))
                    if (ord(candidate[2][0]) - ord(candidate[1][0]) == ord(candidate[1][0]) - ord(candidate[0][0])
                        and candidate[2][1] - candidate[1][1] == candidate[1][1] - candidate[0][1]):
                        three_shore_cells.append(candidate)
        for cell in three_shore_cells:
            print(cell)

    @staticmethod
    def _get_all_neighbouring_cells(cell: tuple):
        """
        Get all the neighbour cell keys
        :param cell: a cell (tuple) to search neighbour of
        :return: a set of tuples of all neighbour cell of this cell
        """
        return {
            (chr(ord(cell[0]) + 1), cell[1]),
            (chr(ord(cell[0]) + 1), cell[1] + 1),
            (cell[0], cell[1] - 1),
            (cell[0], cell[1] + 1),
            (chr(ord(cell[0]) - 1), cell[1] - 1),
            (chr(ord(cell[0]) - 1), cell[1])
        }


if __name__ == "__main__":
    abalone = Abalone()
    abalone.setup_from_input_file("testInput/Test1.input")
    StateSpaceGenerator().generate_next_ply_board_state(abalone.board)
