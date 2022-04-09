from move import Move


class FileOperator:

    def __init__(self, file_name: str):
        self._file_name = file_name

    def write_move(self, move: Move):
        """
        Append move notation to the file object
        :param move: a Move object
        :return: none
        """
        move_string = ""
        for marble_cell in move.marble_group:
            move_string += f"{marble_cell[0]}{marble_cell[1]}"
        move_string += f"{move.direction.value[0]}{move.direction.value[1]}\n"
        with open(self._file_name, mode='a', encoding='utf-8') as move_file:
            move_file.write(move_string)

    def write_board(self, board):
        """
        Append board notation to the file object
        :param board: a Board object
        :return: none
        """
        board_string = board.get_board_information() + "\n"
        with open(self._file_name, mode='a', encoding='utf-8') as move_file:
            move_file.write(board_string)

    @staticmethod
    def get_move_file_name(input_file_name: str):
        dot_index = input_file_name.index('.')
        return f"testOutput/{input_file_name[:dot_index]}.move"

    @staticmethod
    def get_board_file_name(input_file_name: str):
        dot_index = input_file_name.index('.')
        return f"testOutput/{input_file_name[:dot_index]}.board"
