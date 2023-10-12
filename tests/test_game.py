import numpy as np
import pytest

from game import Game
from settings.board import BOARD_CELL_LENGTH
from settings.cell_values import BLACK_VALUE, EMPTY_VALUE, WHITE_VALUE
from settings.directions import (
    DOWN,
    DOWN_LEFT,
    DOWN_RIGHT,
    LEFT,
    RIGHT,
    UP,
    UP_LEFT,
    UP_RIGHT,
)
from settings.graphics import HEIGHT, WIDTH
from utils.test import dict_to_str


@pytest.fixture
def game():
    return Game()


def test_piece_values():
    assert EMPTY_VALUE == 0
    assert BLACK_VALUE == 1
    assert WHITE_VALUE == -1


def test_initialization(game):
    assert np.array_equal(
        game.board,
        np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, -1, 1, 0, 0, 0],
                [0, 0, 0, 1, -1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            dtype=int,
        ),
    )

    assert np.array_equal(
        game.surrounding_cells,
        np.array(
            [
                (2, 2),
                (2, 3),
                (2, 4),
                (2, 5),
                (3, 2),
                (3, 5),
                (4, 2),
                (4, 5),
                (5, 2),
                (5, 3),
                (5, 4),
                (5, 5),
            ],
            dtype=(int, 2),
        ),
    )

    assert dict_to_str(game.sandwiches) == dict_to_str(
        {
            "2,3": np.array([[3, 3]]),
            "3,2": np.array([[3, 3]]),
            "4,5": np.array([[4, 4]]),
            "5,4": np.array([[4, 4]]),
        }
    )

    assert np.array_equal(
        game.indicators,
        np.array([(2, 3), (3, 2), (4, 5), (5, 4)], dtype=(int, 2)),
    )

    assert not game.is_over


def test_reset_game(game):
    game.board[0:2, 5:6] = 1
    game.indicators = np.append(game.indicators, (1, 1))
    game.reset_game()

    assert np.array_equal(
        game.board,
        np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, -1, 1, 0, 0, 0],
                [0, 0, 0, 1, -1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            dtype=int,
        ),
    )

    assert np.array_equal(
        game.surrounding_cells,
        np.array(
            [
                (2, 2),
                (2, 3),
                (2, 4),
                (2, 5),
                (3, 2),
                (3, 5),
                (4, 2),
                (4, 5),
                (5, 2),
                (5, 3),
                (5, 4),
                (5, 5),
            ],
            dtype=(int, 2),
        ),
    )

    assert dict_to_str(game.sandwiches) == dict_to_str(
        {
            "2,3": np.array([[3, 3]]),
            "3,2": np.array([[3, 3]]),
            "4,5": np.array([[4, 4]]),
            "5,4": np.array([[4, 4]]),
        }
    )

    assert np.array_equal(
        game.indicators,
        np.array([(2, 3), (3, 2), (4, 5), (5, 4)], dtype=(int, 2)),
    )

    assert not game.is_over


def test_mouse_pos_to_cell_index(game):
    assert game.mouse_pos_to_cell_index((0, 0)) == (0, 0)
    assert game.mouse_pos_to_cell_index((WIDTH, HEIGHT)) == (8, 8)
    assert game.mouse_pos_to_cell_index((150, 265)) == (1, 3)


def test_is_cell_empty(game):
    game.board[1, 1] = BLACK_VALUE
    game.board[2, 2] = WHITE_VALUE

    # Empty cell
    assert game.is_cell_empty((0, 0))
    # Black piece
    assert not game.is_cell_empty((1, 1))
    # White piece
    assert not game.is_cell_empty((2, 2))


def test_play_piece(game):
    game.player_value = BLACK_VALUE
    game.play_piece((4, 5))

    assert np.array_equal(
        game.board,
        np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, -1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ]
        ),
    )

    game.player_value = WHITE_VALUE
    game.play_piece((5, 3))

    assert np.array_equal(
        game.board,
        np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, -1, -1, -1, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ]
        ),
    )


def test_is_move_legal(game):
    legal_move = (3, 2)
    illegal_move = (0, 0)

    assert game.is_move_legal(legal_move)
    assert not game.is_move_legal(illegal_move)

    game.board.fill(BLACK_VALUE)
    game.update_ssi()
    move = np.random.randint(BOARD_CELL_LENGTH, size=2)

    assert not game.is_move_legal(move)

    game.board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, -1, 1, 0, 0],
            [0, 0, 1, -1, 1, 0, 0, 0],
            [0, 0, -1, 1, -1, 0, 0, 0],
            [0, 0, 0, -1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ],
        dtype=int,
    )
    game.player_value = WHITE_VALUE
    game.update_ssi()
    legal_move = (4, 6)
    illegal_move = (1, 5)

    assert game.is_move_legal(legal_move)
    assert not game.is_move_legal(illegal_move)


def test_cell_values_toward(game):
    game.board = np.arange(25).reshape(5, 5)

    cell_index = (0, 0)

    assert game.cell_values_toward(cell_index, UP) is None
    assert np.array_equal(
        game.cell_values_toward(cell_index, DOWN),
        np.array([5, 10, 15, 20], dtype=int),
    )
    assert game.cell_values_toward(cell_index, LEFT) is None
    assert np.array_equal(
        game.cell_values_toward(cell_index, RIGHT),
        np.array([1, 2, 3, 4], dtype=int),
    )
    assert game.cell_values_toward(cell_index, UP_LEFT) is None
    assert game.cell_values_toward(cell_index, UP_RIGHT) is None
    assert game.cell_values_toward(cell_index, DOWN_LEFT) is None
    assert np.array_equal(
        game.cell_values_toward(cell_index, DOWN_RIGHT),
        np.array([6, 12, 18, 24], dtype=int),
    )

    cell_index = (2, 2)

    assert np.array_equal(
        game.cell_values_toward(cell_index, UP),
        np.array([7, 2], dtype=int),
    )
    assert np.array_equal(
        game.cell_values_toward(cell_index, DOWN),
        np.array([17, 22], dtype=int),
    )
    assert np.array_equal(
        game.cell_values_toward(cell_index, LEFT),
        np.array([11, 10], dtype=int),
    )
    assert np.array_equal(
        game.cell_values_toward(cell_index, RIGHT),
        np.array([13, 14], dtype=int),
    )
    assert np.array_equal(
        game.cell_values_toward(cell_index, UP_LEFT),
        np.array([6, 0], dtype=int),
    )
    assert np.array_equal(
        game.cell_values_toward(cell_index, UP_RIGHT),
        np.array([8, 4], dtype=int),
    )
    assert np.array_equal(
        game.cell_values_toward(cell_index, DOWN_LEFT),
        np.array([16, 20], dtype=int),
    )
    assert np.array_equal(
        game.cell_values_toward(cell_index, DOWN_RIGHT),
        np.array([18, 24], dtype=int),
    )


def test_search_cell_sandwich_towards(game):
    cell_index = (2, 2)
    direction = (1, 1)

    assert game.search_cell_sandwich_towards(cell_index, direction) is None

    game.player_value = WHITE_VALUE

    assert game.search_cell_sandwich_towards(cell_index, direction) is None

    cell_index = (3, 5)
    direction = (0, -1)

    game.player_value = BLACK_VALUE

    assert game.search_cell_sandwich_towards(cell_index, direction) is None

    game.player_value = WHITE_VALUE

    assert np.array_equal(
        game.search_cell_sandwich_towards(cell_index, direction),
        np.array([(3, 4)], dtype=(int, 2)),
    )

    cell_index = (7, 4)
    direction = (1, 0)

    game.player_value = BLACK_VALUE

    assert game.search_cell_sandwich_towards(cell_index, direction) is None

    game.player_value = WHITE_VALUE

    assert game.search_cell_sandwich_towards(cell_index, direction) is None


def test_search_cell_sandwiches(game):
    cell_index = (5, 3)

    assert game.search_cell_sandwiches(cell_index) is None

    game.player_value = WHITE_VALUE

    assert np.array_equal(
        game.search_cell_sandwiches(cell_index),
        np.array([(4, 3)], dtype=(int, 2)),
    )

    game.board = np.array(
        [
            [1, 1, 1, 1, 1, 1, 1, -1],
            [-1, 1, 1, -1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 0, 1, 1, -1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [1, 1, 1, 1, 1, 1, 1, 1],
            [-1, 1, 1, 1, 1, -1, 1, 1],
        ],
        dtype=int,
    )
    cell_index = (3, 4)

    game.player_value = BLACK_VALUE

    assert game.search_cell_sandwiches(cell_index) is None

    game.player_value = WHITE_VALUE

    assert np.array_equal(
        game.search_cell_sandwiches(cell_index),
        np.array(
            [
                (3, 3),
                (3, 2),
                (4, 4),
                (5, 4),
                (2, 3),
                (1, 2),
                (4, 3),
                (5, 2),
                (6, 1),
                (2, 5),
                (1, 6),
            ],
            dtype=(int, 2),
        ),
    )


def test_get_all_non_empty_cells(game):
    assert np.array_equal(
        game.get_all_non_empty_cells(),
        np.array([(3, 3), (3, 4), (4, 3), (4, 4)], dtype=(int, 2)),
    )

    game.board[4, 5] = BLACK_VALUE
    game.board[5, 3] = WHITE_VALUE

    assert np.array_equal(
        game.get_all_non_empty_cells(),
        np.array(
            [(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (5, 4)], dtype=(int, 2)
        ),
    )

    game.board.fill(EMPTY_VALUE)

    assert game.get_all_non_empty_cells() is None

    game.board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, -1, 1, 0, 0],
            [0, 0, 1, -1, 1, 0, 0, 0],
            [0, 0, -1, 1, -1, 0, 0, 0],
            [0, 0, 0, -1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ],
        dtype=int,
    )

    assert np.array_equal(
        game.get_all_non_empty_cells(),
        np.array(
            [
                (2, 3),
                (2, 4),
                (3, 2),
                (3, 3),
                (3, 4),
                (3, 5),
                (4, 2),
                (4, 3),
                (4, 4),
                (4, 5),
                (5, 2),
            ],
            dtype=(int, 2),
        ),
    )


def test_get_empty_neighbors(game):
    cell_index = (0, 0)

    assert np.array_equal(
        game.get_empty_neighbors(cell_index),
        np.array([(1, 0), (0, 1), (1, 1)], dtype=(int, 2)),
    )

    cell_index = (4, 3)

    assert np.array_equal(
        game.get_empty_neighbors(cell_index),
        np.array([(3, 2), (4, 2), (5, 2), (5, 3), (5, 4)], dtype=(int, 2)),
    )

    game.board.fill(BLACK_VALUE)
    cell_index = np.random.randint(BOARD_CELL_LENGTH, size=2)

    assert game.get_empty_neighbors(cell_index) is None

    game.board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, -1, 1, 0, 0],
            [0, 0, 1, -1, 1, 0, 0, 0],
            [0, 0, -1, 1, -1, 0, 0, 0],
            [0, 0, 0, -1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ],
        dtype=int,
    )
    cell_index = (2, 4)

    assert np.array_equal(
        game.get_empty_neighbors(cell_index),
        np.array([(1, 3), (1, 4), (1, 5), (2, 5)], dtype=(int, 2)),
    )

    cell_index = (5, 2)

    assert np.array_equal(
        game.get_empty_neighbors(cell_index),
        np.array(
            [(4, 1), (5, 1), (6, 1), (6, 2), (5, 3), (6, 3)], dtype=(int, 2)
        ),
    )


def test_update_surrounding_cells(game):
    assert np.array_equal(
        game.surrounding_cells,
        np.array(
            [
                (2, 2),
                (2, 3),
                (2, 4),
                (2, 5),
                (3, 2),
                (3, 5),
                (4, 2),
                (4, 5),
                (5, 2),
                (5, 3),
                (5, 4),
                (5, 5),
            ],
            dtype=(int, 2),
        ),
    )

    game.board[4, 5] = BLACK_VALUE
    game.board[5, 3] = WHITE_VALUE
    game.update_surrounding_cells()

    assert np.array_equal(
        game.surrounding_cells,
        np.array(
            [
                (2, 2),
                (2, 3),
                (2, 4),
                (2, 5),
                (2, 6),
                (3, 2),
                (3, 6),
                (4, 2),
                (4, 5),
                (4, 6),
                (5, 2),
                (5, 3),
                (5, 5),
                (6, 3),
                (6, 4),
                (6, 5),
            ],
            dtype=(int, 2),
        ),
    )

    game.board.fill(BLACK_VALUE)
    game.update_surrounding_cells()

    assert game.surrounding_cells is None

    game.board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 1, -1, 1, 0, 0],
            [0, 0, 1, -1, 1, 0, 0, 0],
            [0, 0, -1, 1, -1, 0, 0, 0],
            [0, 0, 0, -1, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ],
        dtype=int,
    )
    game.update_surrounding_cells()

    assert np.array_equal(
        game.surrounding_cells,
        np.array(
            [
                (1, 2),
                (1, 3),
                (1, 4),
                (1, 5),
                (2, 1),
                (2, 2),
                (2, 5),
                (2, 6),
                (3, 1),
                (3, 6),
                (4, 1),
                (4, 6),
                (5, 1),
                (5, 3),
                (5, 4),
                (5, 5),
                (5, 6),
                (6, 1),
                (6, 2),
                (6, 3),
            ],
            dtype=(int, 2),
        ),
    )


def test_update_sandwiches(game):
    assert dict_to_str(game.sandwiches) == dict_to_str(
        {
            "2,3": np.array([[3, 3]]),
            "3,2": np.array([[3, 3]]),
            "4,5": np.array([[4, 4]]),
            "5,4": np.array([[4, 4]]),
        }
    )

    game.player_value = WHITE_VALUE
    game.update_sandwiches()

    assert dict_to_str(game.sandwiches) == dict_to_str(
        {
            "2,4": np.array([[3, 4]]),
            "3,5": np.array([[3, 4]]),
            "4,2": np.array([[4, 3]]),
            "5,3": np.array([[4, 3]]),
        }
    )

    game.board.fill(BLACK_VALUE)
    game.player_value = BLACK_VALUE
    game.update_surrounding_cells()
    game.update_sandwiches()

    assert game.sandwiches == {}

    game.player_value = WHITE_VALUE
    game.update_sandwiches()

    assert game.sandwiches == {}

    game.board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, -1, 0, -1, 0, 0],
            [0, 0, 1, 1, -1, -1, 0, 0],
            [0, 0, 0, 1, -1, 1, 0, 0],
            [0, 0, 0, -1, -1, 1, 0, 0],
            [0, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ],
        dtype=int,
    )
    game.player_value = BLACK_VALUE
    game.update_surrounding_cells()
    game.update_sandwiches()

    assert dict_to_str(game.sandwiches) == dict_to_str(
        {
            "2,1": np.array([[3, 2], [4, 3]]),
            "2,5": np.array([[3, 5], [4, 5]]),
            "3,1": np.array([[3, 2]]),
            "3,6": np.array([[3, 5], [4, 5]]),
            "3,7": np.array([[4, 6]]),
            "4,1": np.array([[3, 2]]),
            "4,2": np.array([[3, 2]]),
            "5,1": np.array([[5, 2], [5, 3]]),
            "5,6": np.array([[4, 5]]),
            "6,1": np.array([[5, 2], [4, 3]]),
            "6,3": np.array([[5, 3], [4, 3]]),
        }
    )

    game.player_value = WHITE_VALUE
    game.update_sandwiches()

    assert dict_to_str(game.sandwiches) == dict_to_str(
        {
            "1,1": np.array([[2, 2], [3, 3]]),
            "1,2": np.array([[2, 2], [2, 3], [3, 4]]),
            "1,3": np.array([[2, 3], [3, 3]]),
            "1,4": np.array([[2, 3]]),
            "2,4": np.array([[3, 4]]),
            "2,5": np.array([[3, 4]]),
            "5,6": np.array([[5, 5], [5, 4]]),
            "6,3": np.array([[5, 4]]),
            "6,4": np.array([[5, 4], [5, 5]]),
            "6,5": np.array([[5, 5], [5, 4]]),
            "6,6": np.array([[5, 5]]),
        }
    )


def test_update_indicators(game):
    assert np.array_equal(
        game.indicators,
        np.array([(2, 3), (3, 2), (4, 5), (5, 4)], dtype=(int, 2)),
    )

    game.player_value = WHITE_VALUE
    game.update_sandwiches()
    game.update_indicators()

    assert np.array_equal(
        game.indicators,
        np.array([(2, 4), (3, 5), (4, 2), (5, 3)], dtype=(int, 2)),
    )

    game.board.fill(BLACK_VALUE)
    game.player_value = BLACK_VALUE
    game.update_surrounding_cells()
    game.update_sandwiches()
    game.update_indicators()

    assert game.indicators == []

    game.player_value = WHITE_VALUE
    game.update_sandwiches()
    game.update_indicators()

    assert game.indicators == []

    game.board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, -1, 0, -1, 0, 0],
            [0, 0, 1, 1, -1, -1, 0, 0],
            [0, 0, 0, 1, -1, 1, 0, 0],
            [0, 0, 0, -1, -1, 1, 0, 0],
            [0, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ],
        dtype=int,
    )
    game.player_value = BLACK_VALUE
    game.update_surrounding_cells()
    game.update_sandwiches()
    game.update_indicators()

    assert np.array_equal(
        game.indicators,
        np.array(
            [
                (2, 1),
                (2, 5),
                (3, 1),
                (3, 6),
                (3, 7),
                (4, 1),
                (4, 2),
                (5, 1),
                (5, 6),
                (6, 1),
                (6, 3),
            ],
            dtype=(int, 2),
        ),
    )

    game.player_value = WHITE_VALUE
    game.update_sandwiches()
    game.update_indicators()

    assert np.array_equal(
        game.indicators,
        np.array(
            [
                (1, 1),
                (1, 2),
                (1, 3),
                (1, 4),
                (2, 4),
                (2, 5),
                (5, 6),
                (6, 3),
                (6, 4),
                (6, 5),
                (6, 6),
            ],
            dtype=(int, 2),
        ),
    )


def test_flip_sandwiches(game):
    indicator_index = (4, 5)
    game.flip_sandwiches(indicator_index)

    assert np.array_equal(
        game.board,
        np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, -1, 1, 0, 0, 0],
                [0, 0, 0, 1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            dtype=int,
        ),
    )

    game.board = np.array(
        [
            [-1, -1, -1, -1, -1, -1, -1, -1],
            [-1, 1, 1, 1, 1, 1, 1, -1],
            [-1, 1, 1, 1, 1, 1, 1, -1],
            [-1, 1, 1, 1, 1, 1, 1, -1],
            [-1, 1, 1, 1, 1, 1, 1, -1],
            [-1, 1, 0, 1, 1, 1, 1, -1],
            [-1, 1, 1, 1, 1, 1, 1, -1],
            [-1, -1, -1, -1, -1, -1, -1, -1],
        ],
        dtype=int,
    )
    game.player_value = WHITE_VALUE
    game.update_ssi()
    indicator_index = (2, 5)
    game.flip_sandwiches(indicator_index)

    assert np.array_equal(
        game.board,
        np.array(
            [
                [-1, -1, -1, -1, -1, -1, -1, -1],
                [-1, 1, -1, 1, 1, 1, -1, -1],
                [-1, 1, -1, 1, 1, -1, 1, -1],
                [-1, 1, -1, 1, -1, 1, 1, -1],
                [-1, -1, -1, -1, 1, 1, 1, -1],
                [-1, -1, 0, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, 1, 1, 1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1],
            ],
            dtype=int,
        ),
    )


def test_is_player_able_to_play(game):
    assert game.is_player_able_to_play()

    game.player_value = WHITE_VALUE
    game.update_ssi()

    assert game.is_player_able_to_play()

    game.board = np.array(
        [
            [-1, 0, -1, 0, -1, 0, 1, 0],
            [-1, 1, 1, -1, -1, 1, 1, 1],
            [-1, 0, 1, 0, -1, 0, 1, 0],
            [-1, 1, 1, 1, 1, 1, 1, 1],
            [-1, 0, 1, 0, 1, 0, 1, 0],
            [-1, 1, -1, -1, -1, 1, -1, 1],
            [-1, 0, -1, 0, 1, 0, 1, 0],
            [-1, -1, -1, -1, -1, -1, -1, 1],
        ],
        dtype=int,
    )
    game.player_value = BLACK_VALUE
    game.update_ssi()

    assert not game.is_player_able_to_play()

    game.player_value = WHITE_VALUE
    game.update_ssi()

    assert not game.is_player_able_to_play()


def test_get_black_piece_count(game):
    assert game.get_black_piece_count() == 2

    game.board.fill(EMPTY_VALUE)

    assert game.get_black_piece_count() == 0

    game.board = np.array(
        [
            [-1, 0, -1, 0, -1, 0, 1, 0],
            [-1, 1, 1, -1, -1, 1, 1, 1],
            [-1, 0, 1, 0, -1, 0, 1, 0],
            [-1, 1, 1, 1, 1, 1, 1, 1],
            [-1, 0, 1, 0, 1, 0, 1, 0],
            [-1, 1, -1, -1, -1, 1, -1, 1],
            [-1, 0, -1, 0, 1, 0, 1, 0],
            [-1, -1, -1, -1, -1, -1, -1, 1],
        ],
        dtype=int,
    )

    assert game.get_black_piece_count() == 24


def test_get_white_piece_count(game):
    assert game.get_white_piece_count() == 2

    game.board.fill(EMPTY_VALUE)

    assert game.get_white_piece_count() == 0

    game.board = np.array(
        [
            [-1, 0, -1, 0, -1, 0, 1, 0],
            [-1, 1, 1, -1, -1, 1, 1, 1],
            [-1, 0, 1, 0, -1, 0, 1, 0],
            [-1, 1, 1, 1, 1, 1, 1, 1],
            [-1, 0, 1, 0, 1, 0, 1, 0],
            [-1, 1, -1, -1, -1, 1, -1, 1],
            [-1, 0, -1, 0, 1, 0, 1, 0],
            [-1, -1, -1, -1, -1, -1, -1, 1],
        ],
        dtype=int,
    )

    assert game.get_white_piece_count() == 24


def test_get_winner(game):
    game.board = np.array(
        [
            [-1, 0, -1, 0, -1, 0, 1, 0],
            [-1, 1, 1, -1, -1, 1, 1, 1],
            [-1, 0, 1, 0, -1, 0, 1, 0],
            [-1, 1, 1, 1, 1, 1, 1, 1],
            [-1, 0, 1, 0, 1, 0, 1, 0],
            [-1, 1, -1, -1, -1, 1, -1, 1],
            [-1, 0, -1, 0, 1, 0, 1, 0],
            [-1, -1, -1, -1, -1, -1, -1, 1],
        ],
        dtype=int,
    )
    game.update_ssi()

    assert game.get_winner() == 0

    game.board = np.array(
        [
            [-1, -1, -1, -1, -1, -1, 1, -1],
            [-1, 1, 1, -1, -1, 1, 1, 1],
            [-1, -1, 1, -1, -1, -1, 1, -1],
            [-1, 1, 1, 1, 1, 1, 1, 1],
            [-1, -1, 1, -1, 1, -1, 1, -1],
            [-1, 1, -1, -1, -1, 1, -1, 1],
            [-1, -1, -1, -1, 1, -1, 1, -1],
            [-1, -1, -1, -1, -1, -1, -1, 1],
        ],
        dtype=int,
    )
    game.update_ssi()

    assert game.get_winner() == WHITE_VALUE

    game.board = np.array(
        [
            [-1, 1, -1, 1, -1, 1, 1, 1],
            [-1, 1, 1, -1, -1, 1, 1, 1],
            [-1, 1, 1, 1, -1, 1, 1, 1],
            [-1, 1, 1, 1, 1, 1, 1, 1],
            [-1, 1, 1, 1, 1, 1, 1, 1],
            [-1, 1, -1, -1, -1, 1, -1, 1],
            [-1, 1, -1, 1, 1, 1, 1, 1],
            [-1, -1, -1, -1, -1, -1, -1, 1],
        ],
        dtype=int,
    )
    game.update_ssi()

    assert game.get_winner() == BLACK_VALUE


def test_next_player_turn(game):
    game.next_player_turn()

    assert game.player_value == WHITE_VALUE and not game.is_over

    game.board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 1, 1, 1, 1, 1, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ],
        dtype=int,
    )
    game.player_value = WHITE_VALUE
    game.next_player_turn()

    assert game.player_value == WHITE_VALUE and game.is_over

    game.player_value = BLACK_VALUE
    game.next_player_turn()

    assert game.player_value == BLACK_VALUE and game.is_over
