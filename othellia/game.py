from copy import deepcopy
from textwrap import wrap
from typing import Any

import numpy as np
from numpy import ndarray, dtype, signedinteger
# noinspection PyProtectedMember
from numpy._typing import _64Bit

from settings.board import BOARD_CELL_LENGTH
from settings.directions import DIRECTIONS
from settings.graphics import WIDTH
from settings.values import BLACK_VALUE, EMPTY_VALUE, WHITE_VALUE
from utils.game import notation_to_cell_index


def mouse_pos_to_cell_index(pos: tuple[int, int]) -> tuple[int, int]:
    """Convert a mouse position into a cell index.

    Args:
        pos (tuple[int, int]): x and y coordinates.

    Returns:
        tuple[int, int]: column and row indices.
    """
    x, y = pos
    cell_size = WIDTH / BOARD_CELL_LENGTH

    return int(x // cell_size), int(y // cell_size)


class Game:
    """Class gathering all the game's behaviours."""
    player_value: int
    is_over: bool
    indicators: ndarray[Any, dtype[Any]]
    surrounding_cells: ndarray[Any, dtype[Any]]
    sandwiches: dict[str, ndarray[tuple[int, int], dtype[signedinteger[_64Bit]]]]
    board: ndarray[Any, dtype[Any]]

    def __init__(self) -> None:
        self.reset_game()

    def reset_game(self) -> None:
        """Reset the game board into initial configuration."""
        self.board = np.full(
            (BOARD_CELL_LENGTH, BOARD_CELL_LENGTH), EMPTY_VALUE, dtype=int
        )

        self.board[3, 3] = WHITE_VALUE
        self.board[4, 4] = WHITE_VALUE
        self.board[3, 4] = BLACK_VALUE
        self.board[4, 3] = BLACK_VALUE

        self.player_value = BLACK_VALUE
        self.update_ssi()

        self.is_over = False

    def is_cell_empty(self, cell_index: tuple[int, int]) -> bool:
        """Check if a cell doesn't contain  a piece.

        Args:
            cell_index (tuple[int, int]): cell's column and row.

        Returns:
            bool: non-presence of a piece.
        """
        col, row = cell_index
        return bool(self.board[row, col] == EMPTY_VALUE)

    def play_piece(self, cell_index: tuple[int, int]) -> None:
        """Play a piece in a cell and update the board according.

        Args:
            cell_index (tuple[int, int]): cell's column and row.
        """
        col, row = cell_index
        self.board[row, col] = self.player_value

        self.flip_sandwiches(cell_index)

        self.next_player_turn()

        self.update_ssi()

    def is_move_legal(self, cell_index: tuple[int, int]) -> bool:
        """Ensure if a move is legal according to the current state of
        the board.

        Args:
            cell_index (tuple[int, int]): cell's column and row.

        Returns:
            bool: Legality of the move.
        """
        if np.array_equal(self.indicators, np.array([])):
            return False

        return bool(np.any(np.all(self.indicators == cell_index, axis=1)))

    def update_sandwiches(self) -> None:
        """Find all the sandwiches from available legal moves.

        Returns:
            dict: sandwiches for each possible move.
        """
        self.sandwiches = {}

        if len(self.surrounding_cells) != 0:
            for cell_index in self.surrounding_cells:
                cell_sandwiches = self.search_cell_sandwiches(cell_index)

                if len(cell_sandwiches) == 0:
                    continue

                x, y = cell_index
                self.sandwiches[f"{x},{y}"] = cell_sandwiches

    def search_cell_sandwiches(
            self, cell_index: tuple[int, int]
    ) -> np.ndarray[tuple[int, int], np.dtype[np.int64]]:
        """Find all possible sandwiches from a single cell.

        Args:
            cell_index (tuple[int, int]): cell's column and row.

        Returns:
            np.ndarray[tuple[int, int], np.dtype[np.int64]]: cell indices within the
            sandwiches.
        """
        sandwiches: list[tuple[int, int] | dtype[signedinteger[_64Bit]]] = []

        # Loop for sandwiches in all directions
        for direction in DIRECTIONS:
            cell_indices = self.search_cell_sandwich_towards(
                cell_index, direction
            )

            if len(cell_indices) == 0:
                continue

            sandwiches.extend(cell_indices)

        return np.array(sandwiches)

    def search_cell_sandwich_towards(
            self,
            cell_index: tuple[int, int],
            direction: tuple[int, int],
    ) -> np.ndarray[tuple[int, int], np.dtype[np.int64]]:
        """Find if a sandwich, if possible, in a given directory from a cell.

        Args:
            cell_index (tuple[int, int]): column and row of the cell.
            direction (tuple[int, int]): direction of the search.

        Returns:
            npt.ArrayLike[tuple[int, int]]: cell indices within the sandwich.
        """
        consecutive = 0
        is_sandwich_end = False

        cvt = self.cell_values_toward(cell_index, direction)

        for cell_value in cvt:
            # Check for the end of the sandwich
            if cell_value == self.player_value:
                is_sandwich_end = True
                break

            # Check if the cell has the opponent colour
            if cell_value != -self.player_value:
                break

            consecutive += 1

        x, y = cell_index
        dx, dy = direction

        return (
            np.array(
                [
                    (x + (dx * c), y + (dy * c))
                    for c in range(1, consecutive + 1)
                ],
                dtype=(int, 2),
            )
            if consecutive > 0 and is_sandwich_end
            else np.array([])
        )

    def cell_values_toward(
            self, cell_index: tuple[int, int], direction: tuple[int, int]
    ) -> np.ndarray[np.int64, np.dtype[np.int64]]:
        """Return all the cells value toward a cell in a given direction.

        Args:
            cell_index (tuple[int, int]): column and row of the cell.
            direction (tuple[int, int]): direction of the search.

        Returns:
            np.ndarray[np.int64, np.dtype[np.int64]]: cells value in the given
            direction.
        """
        x, y = cell_index

        match direction:
            case (0, 1):
                return self.board[y + 1:, x]
            case (1, 0):
                return self.board[y, x + 1:]
            case (0, -1):
                return self.board[:y, x][::-1]
            case (-1, 0):
                return self.board[y, :x][::-1]
            case (1, 1):
                return self.board[y + 1:, x + 1:].diagonal()
            case (1, -1):
                return np.flipud(self.board[:y, x + 1:]).diagonal()
            case (-1, 1):
                return np.fliplr(self.board[y + 1:, :x]).diagonal()
            case _:
                return np.flipud(np.fliplr(self.board[:y, :x])).diagonal()

    def update_surrounding_cells(self) -> None:
        """Find the empty cells surrounding the pieces cluster."""
        surrounding_cells: list[tuple[int, int]] = []

        for cell_index in self.get_all_non_empty_cells():
            empty_neighbors = self.get_empty_neighbors(cell_index)

            if len(empty_neighbors) == 0:
                continue

            surrounding_cells.extend(empty_neighbors)

        self.surrounding_cells = np.array(np.unique(surrounding_cells, axis=0))

    def get_all_non_empty_cells(
            self,
    ) -> np.ndarray[tuple[int, int], np.dtype[np.int64]]:
        """Return all non-empty cells on the board.

        Returns:
            np.ndarray[tuple[int, int], np.dtype[np.int64]]: cells column and row.
        """
        cells = []

        for col in range(BOARD_CELL_LENGTH):
            for row in range(BOARD_CELL_LENGTH):
                value = self.board[row, col]

                if value == EMPTY_VALUE:
                    continue

                cells.append((col, row))

        return np.array(cells)

    def get_all_black_cells(
            self,
    ) -> np.ndarray[tuple[int, int], np.dtype[np.int64]]:
        """Return all blck cells on the board.

        Returns:
            np.ndarray[tuple[int, int]: cells column and row.
        """
        cells = []

        for col in range(BOARD_CELL_LENGTH):
            for row in range(BOARD_CELL_LENGTH):
                value = self.board[row, col]

                if value != BLACK_VALUE:
                    continue

                cells.append((col, row))

        return np.array(cells)

    def get_all_white_cells(
            self,
    ) -> np.ndarray[tuple[int, int], np.dtype[np.int64]]:
        """Return all white cells on the board.

        Returns:
            np.ndarray[tuple[int, int], np.dtype[np.int64]]: cells column and row.
        """
        cells = []

        for col in range(BOARD_CELL_LENGTH):
            for row in range(BOARD_CELL_LENGTH):
                value = self.board[row, col]

                if value != WHITE_VALUE:
                    continue

                cells.append((col, row))

        return np.array(cells)

    def get_empty_neighbors(
            self, cell_index: tuple[int, int]
    ) -> np.ndarray[tuple[int, int], np.dtype[np.int64]]:
        """Retrieve all the empty neighbors of a given cell.

        Args:
            cell_index (tuple[int, int]): cell's column and row.

        Returns:
            np.ndarray[tuple[int, int]]: cells column and row.
        """
        row, col = cell_index
        neighbors = []

        # https://stackoverflow.com/a/67758639
        for y in range(-1, 2):
            for x in range(-1, 2):
                # No shifting case
                if x == 0 and y == 0:
                    continue

                nx = row + x
                ny = col + y

                # Check boundaries
                if (
                        nx < 0
                        or nx >= BOARD_CELL_LENGTH
                        or ny < 0
                        or ny >= BOARD_CELL_LENGTH
                ):
                    continue

                if self.board[ny, nx] != EMPTY_VALUE:
                    continue

                neighbors.append((nx, ny))

        return np.array(neighbors)

    def update_indicators(self) -> None:
        """Update the move indicators positions according the possible sandwiches."""
        cells = []

        if len(self.sandwiches) > 0:
            for k in self.sandwiches.keys():
                col, row = list(map(int, k.split(",")))
                cells.append((col, row))

        self.indicators = np.array(cells)

    def flip_sandwiches(self, indicator_index: tuple[int, int]) -> None:
        """Flip all the pieces within the available sandwiches from an indicator's
        location.

        Args:
            indicator_index (tuple[int, int]): column and row of an indicator.
        """
        key = f"{indicator_index[0]},{indicator_index[1]}"
        _get = self.sandwiches.get(key)

        cells_to_flip = iter(_get) if _get is not None else []

        for col, row in cells_to_flip:
            self.board[row, col] *= -1

    def is_player_able_to_play(self) -> bool:
        """Check if a player has legal moves to play.

        Returns:
            bool : whether the player is able to play.
        """
        return not np.array_equal(self.indicators, np.array([]))

    def get_black_piece_count(self) -> int:
        """Return the number of black pieces on the board.

        Returns:
            int: number of black pieces.
        """
        return int(np.sum(self.board == BLACK_VALUE))

    def get_white_piece_count(self) -> int:
        """Return the number of white pieces on the board.

        Returns:
            int: number of black pieces.
        """
        return int(np.sum(self.board == WHITE_VALUE))

    def get_winner(self) -> int:
        """Return the value of the player who won the game.

        Returns:
            int: value of the player who won the game, 0 if drawn.
        """
        black_piece_count = self.get_black_piece_count()
        white_piece_count = self.get_white_piece_count()

        # Draw
        if black_piece_count == white_piece_count:
            return 0

        return (
            BLACK_VALUE
            if black_piece_count > white_piece_count
            else WHITE_VALUE
        )

    def update_ssi(self) -> None:
        """Updates the game surrounding cells, sandwiches and indicators."""
        self.update_surrounding_cells()
        self.update_sandwiches()
        self.update_indicators()

    def next_player_turn(self) -> None:
        """Update the next player value or declare the game over."""
        self.player_value *= -1
        self.update_ssi()

        # Check for skipping turn
        if not self.is_player_able_to_play():
            self.player_value *= -1
            self.update_ssi()

            if not self.is_player_able_to_play():
                # Neither player has legal moves left
                self.is_over = True

    def load_transcript(self, transcript: str) -> None:
        """Play each player move from a match transcription.

        Args:
            transcript (str): sequence of moves.
        """
        for move in wrap(transcript, 2):
            self.play_piece(notation_to_cell_index(move))

    def set_position(
            self, board: np.ndarray[np.int64, np.dtype[np.int64]], to_play: int
    ) -> None:
        """Set a board position and update surrounding cells, sandwiches and indicators
        for a player to play.

        Args:
            board (np.ndarray[np.int64, np.dtype[np.int64]]): a board position.
            to_play (int): value of the player to play.
        """
        self.board = board
        self.player_value = to_play

        self.update_ssi()

    def get_black_legal_moves(
            self,
    ) -> np.ndarray[tuple[int, int], np.dtype[np.int64]]:
        """Return all black possible moves to play.

        Returns:
            np.ndarray[tuple[int, int], np.dtype[np.int64]]: list of cells row and
            column.
        """
        game_copy = deepcopy(self)  # Copy the game without reference

        game_copy.player_value = BLACK_VALUE
        game_copy.update_ssi()

        return game_copy.indicators

    def get_white_legal_moves(
            self,
    ) -> np.ndarray[tuple[int, int], np.dtype[np.int64]]:
        """Return all white possible moves to play.

        Returns:
            np.ndarray[tuple[int, int], np.dtype[np.int64]]: list of cells row and
            column.
        """
        game_copy = deepcopy(self)  # Copy the game without reference

        game_copy.player_value = WHITE_VALUE
        game_copy.update_ssi()

        return game_copy.indicators

    def get_black_legal_moves_count(self) -> int:
        """Returns the number of black's legal moves.

        Returns:
            int: number of legal moves.
        """
        return len(self.get_black_legal_moves())

    def get_white_legal_moves_count(self) -> int:
        """Returns the number of white's legal moves.

        Returns:
            int: number of legal moves.
        """
        return len(self.get_white_legal_moves())

    def get_black_empty_neighbors_count(self) -> int:
        """Returns the number of empty cells next to black's pieces.

        Returns:
            int: number of empty cells.
        """
        black_cells = self.get_all_black_cells()

        if len(black_cells) == 0:
            return 0

        empty_cells: list[tuple[int, int]] = []
        for cell_index in black_cells:
            empty_neighbors = self.get_empty_neighbors(cell_index)

            if len(empty_neighbors) == 0:
                continue

            empty_cells.extend(empty_neighbors)

        return len(np.unique(empty_cells, axis=0))

    def get_white_empty_neighbors_count(self) -> int:
        """Returns the number of empty cells next to white's pieces.

        Returns:
            int: number of empty cells.
        """
        white_cells = self.get_all_white_cells()

        if len(white_cells) == 0:
            return 0

        empty_cells: list[tuple[int, int]] = []
        for cell_index in white_cells:
            empty_neighbors = self.get_empty_neighbors(cell_index)

            if len(empty_neighbors) == 0:
                continue

            empty_cells.extend(empty_neighbors)

        return len(np.unique(empty_cells, axis=0))
