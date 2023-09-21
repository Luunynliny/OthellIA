import numpy as np

from settings import BLACK_VALUE, EMPTY_VALUE, WHITE_VALUE, WIDTH


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

        self.play_piece((3, 3), value=BLACK_VALUE)
        self.play_piece((4, 4), value=BLACK_VALUE)
        self.play_piece((3, 4), value=WHITE_VALUE)
        self.play_piece((4, 3), value=WHITE_VALUE)

        self.indicators = np.array(
            [(2, 4), (3, 5), (4, 2), (5, 3)], dtype=(int, 2)
        )

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

    def is_move_legal(self, cell_index: tuple[int, int]) -> bool:
        """Ensure if a move is legal according to the current state of
        the board.

        Args:
            cell_index (tuple[int, int]): row and column of the cell.

        Returns:
            bool: Legality of the move.
        """
        return np.any(np.all(self.indicators == cell_index, axis=1))

    def remove_indicator(self, cell_index: tuple[int, int]):
        """Remove indicator at a cell position.

        Args:
            cell_index (tuple[int, int]): row and column of the cell.
        """
        to_keep = np.any(self.indicators != cell_index, axis=1)
        self.indicators = self.indicators[to_keep]
