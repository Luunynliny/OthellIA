import numpy as np

from settings import EMPTY_VALUE, WIDTH


class Game:
    """Class gathering all the game's behaviours.

    Args:
        width (int): width of the board.
        height (int): height if the board.
    """

    def __init__(self):
        self.reset_game()

    def reset_game(self):
        """Reset the game board into initial configuration."""
        self.board = np.full((8, 8), EMPTY_VALUE, dtype=np.intc)

    def mouse_pos_to_cell_index(self, pos: tuple[int, int]) -> tuple[int, int]:
        """Convert a mouse position into a cell index.

        Args:
            pos (tuple[int, int]): x and y coordinates.

        Returns:
            tuple[int, int]: row and column indices.
        """
        x, y = pos
        cell_size = WIDTH / 8

        return (int(x // cell_size), int(y // cell_size))

    def is_cell_empty(self, cell_index: tuple[int, int]) -> bool:
        """Check if a cell doesn't contain  a piece.

        Args:
            cell_index (tuple[int, int]): row and column of the cell.

        Returns:
            bool: non-presence of a piece.
        """
        return self.board[cell_index] == EMPTY_VALUE

    def play_piece(self, cell_index: tuple[int, int], value: int):
        """Play a piece in a cell.

        Args:
            cell_index (tuple[int, int]): row and column of the cell.
            value (int): value of the piece.
        """
        self.board[cell_index] = value
