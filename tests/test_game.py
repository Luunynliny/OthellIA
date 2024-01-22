import numpy as np
import pytest

from othellia.game import Game, mouse_pos_to_cell_index
from settings.board import BOARD_CELL_LENGTH
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
from settings.values import BLACK_VALUE, EMPTY_VALUE, WHITE_VALUE
from utils.test import dict_to_str


@pytest.fixture
def game():
    return Game()


@pytest.fixture
def rng():
    return np.random.default_rng()


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
            ]
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
        np.array([(2, 3), (3, 2), (4, 5), (5, 4)]),
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
            ]
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
        np.array([(2, 3), (3, 2), (4, 5), (5, 4)]),
    )

    assert not game.is_over


def test_mouse_pos_to_cell_index():
    assert mouse_pos_to_cell_index((0, 0)) == (0, 0)
    assert mouse_pos_to_cell_index((WIDTH, HEIGHT)) == (8, 8)
    assert mouse_pos_to_cell_index((150, 265)) == (1, 3)


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


def test_is_move_legal(game, rng):
    legal_move = (3, 2)
    illegal_move = (0, 0)

    assert game.is_move_legal(legal_move)
    assert not game.is_move_legal(illegal_move)

    game.board.fill(BLACK_VALUE)
    game.update_ssi()
    move = (rng.integers(BOARD_CELL_LENGTH), rng.integers(BOARD_CELL_LENGTH))

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
        ]
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

    assert np.array_equal(game.cell_values_toward(cell_index, UP), [])
    assert np.array_equal(
        game.cell_values_toward(cell_index, DOWN),
        np.array([5, 10, 15, 20]),
    )
    assert np.array_equal(game.cell_values_toward(cell_index, LEFT), [])
    assert np.array_equal(
        game.cell_values_toward(cell_index, RIGHT),
        np.array([1, 2, 3, 4]),
    )
    assert np.array_equal(game.cell_values_toward(cell_index, UP_LEFT), [])
    assert np.array_equal(game.cell_values_toward(cell_index, UP_RIGHT), [])
    assert np.array_equal(game.cell_values_toward(cell_index, DOWN_LEFT), [])
    assert np.array_equal(
        game.cell_values_toward(cell_index, DOWN_RIGHT),
        np.array([6, 12, 18, 24]),
    )

    cell_index = (2, 2)

    assert np.array_equal(
        game.cell_values_toward(cell_index, UP),
        np.array([7, 2]),
    )
    assert np.array_equal(
        game.cell_values_toward(cell_index, DOWN),
        np.array([17, 22]),
    )
    assert np.array_equal(
        game.cell_values_toward(cell_index, LEFT),
        np.array([11, 10]),
    )
    assert np.array_equal(
        game.cell_values_toward(cell_index, RIGHT),
        np.array([13, 14]),
    )
    assert np.array_equal(
        game.cell_values_toward(cell_index, UP_LEFT),
        np.array([6, 0]),
    )
    assert np.array_equal(
        game.cell_values_toward(cell_index, UP_RIGHT),
        np.array([8, 4]),
    )
    assert np.array_equal(
        game.cell_values_toward(cell_index, DOWN_LEFT),
        np.array([16, 20]),
    )
    assert np.array_equal(
        game.cell_values_toward(cell_index, DOWN_RIGHT),
        np.array([18, 24]),
    )


def test_search_cell_sandwich_towards(game):
    cell_index = (2, 2)
    direction = (1, 1)

    assert np.array_equal(
        game.search_cell_sandwich_towards(cell_index, direction), []
    )

    game.player_value = WHITE_VALUE

    assert np.array_equal(
        game.search_cell_sandwich_towards(cell_index, direction), []
    )

    cell_index = (3, 5)
    direction = (0, -1)

    game.player_value = BLACK_VALUE

    assert np.array_equal(
        game.search_cell_sandwich_towards(cell_index, direction), []
    )

    game.player_value = WHITE_VALUE

    assert np.array_equal(
        game.search_cell_sandwich_towards(cell_index, direction),
        np.array([(3, 4)]),
    )

    cell_index = (7, 4)
    direction = (1, 0)

    game.player_value = BLACK_VALUE

    assert np.array_equal(
        game.search_cell_sandwich_towards(cell_index, direction), []
    )

    game.player_value = WHITE_VALUE

    assert np.array_equal(
        game.search_cell_sandwich_towards(cell_index, direction), []
    )


def test_search_cell_sandwiches(game):
    cell_index = (5, 3)

    assert np.array_equal(game.search_cell_sandwiches(cell_index), [])

    game.player_value = WHITE_VALUE

    assert np.array_equal(
        game.search_cell_sandwiches(cell_index),
        np.array([(4, 3)]),
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
        ]
    )
    cell_index = (3, 4)

    game.player_value = BLACK_VALUE

    assert np.array_equal(game.search_cell_sandwiches(cell_index), [])

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
        ),
    )


def test_get_all_non_empty_cells(game):
    assert np.array_equal(
        game.get_all_non_empty_cells(),
        np.array([(3, 3), (3, 4), (4, 3), (4, 4)]),
    )

    game.board[4, 5] = BLACK_VALUE
    game.board[5, 3] = WHITE_VALUE

    assert np.array_equal(
        game.get_all_non_empty_cells(),
        np.array([(3, 3), (3, 4), (3, 5), (4, 3), (4, 4), (5, 4)]),
    )

    game.board.fill(EMPTY_VALUE)

    assert np.array_equal(game.get_all_non_empty_cells(), [])

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
        ]
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
        ),
    )


def test_get_all_white_cells(game):
    assert np.array_equal(
        game.get_all_white_cells(),
        np.array([(3, 3), (4, 4)]),
    )

    game.board[4, 5] = BLACK_VALUE
    game.board[5, 3] = WHITE_VALUE

    assert np.array_equal(
        game.get_all_white_cells(),
        np.array([(3, 3), (3, 5), (4, 4)]),
    )

    game.board.fill(EMPTY_VALUE)

    assert np.array_equal(game.get_all_white_cells(), [])

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
        ]
    )

    assert np.array_equal(
        game.get_all_white_cells(),
        np.array(
            [(2, 4), (3, 3), (3, 5), (4, 2), (4, 4)],
        ),
    )


def test_get_all_black_cells(game):
    assert np.array_equal(
        game.get_all_black_cells(),
        np.array([(3, 4), (4, 3)]),
    )

    game.board[4, 5] = BLACK_VALUE
    game.board[5, 3] = WHITE_VALUE

    assert np.array_equal(
        game.get_all_black_cells(),
        np.array([(3, 4), (4, 3), (5, 4)]),
    )

    game.board.fill(EMPTY_VALUE)

    assert np.array_equal(game.get_all_black_cells(), [])

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
        ]
    )

    assert np.array_equal(
        game.get_all_black_cells(),
        np.array(
            [(2, 3), (3, 2), (3, 4), (4, 3), (4, 5), (5, 2)],
        ),
    )


def test_get_empty_neighbors(game, rng):
    cell_index = (0, 0)

    assert np.array_equal(
        game.get_empty_neighbors(cell_index),
        np.array([(1, 0), (0, 1), (1, 1)]),
    )

    cell_index = (4, 3)

    assert np.array_equal(
        game.get_empty_neighbors(cell_index),
        np.array([(3, 2), (4, 2), (5, 2), (5, 3), (5, 4)]),
    )

    game.board.fill(BLACK_VALUE)
    cell_index = (rng.integers(BOARD_CELL_LENGTH), rng.integers(BOARD_CELL_LENGTH))

    assert np.array_equal(game.get_empty_neighbors(cell_index), [])

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
        ]
    )
    cell_index = (2, 4)

    assert np.array_equal(
        game.get_empty_neighbors(cell_index),
        np.array([(1, 3), (1, 4), (1, 5), (2, 5)]),
    )

    cell_index = (5, 2)

    assert np.array_equal(
        game.get_empty_neighbors(cell_index),
        np.array([(4, 1), (5, 1), (6, 1), (6, 2), (5, 3), (6, 3)]),
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
            ]
        ),
    )

    game.board.fill(BLACK_VALUE)
    game.update_surrounding_cells()

    assert np.array_equal(game.surrounding_cells, [])

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
        ]
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
        ]
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
        np.array([(2, 3), (3, 2), (4, 5), (5, 4)]),
    )

    game.player_value = WHITE_VALUE
    game.update_sandwiches()
    game.update_indicators()

    assert np.array_equal(
        game.indicators,
        np.array([(2, 4), (3, 5), (4, 2), (5, 3)]),
    )

    game.board.fill(BLACK_VALUE)
    game.player_value = BLACK_VALUE
    game.update_surrounding_cells()
    game.update_sandwiches()
    game.update_indicators()

    assert np.array_equal(game.indicators, [])

    game.player_value = WHITE_VALUE
    game.update_sandwiches()
    game.update_indicators()

    assert np.array_equal(game.indicators, [])

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
        ]
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
            ]
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
        ]
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
            ]
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
        ]
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
        ]
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
        ]
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
        ]
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
        ]
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
        ]
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
        ]
    )
    game.player_value = WHITE_VALUE
    game.next_player_turn()

    assert game.player_value == WHITE_VALUE and game.is_over

    game.player_value = BLACK_VALUE
    game.next_player_turn()

    assert game.player_value == BLACK_VALUE and game.is_over


def test_load_transcript(game):
    t = "c4e3f6e6"
    game.load_transcript(t)

    assert np.array_equal(
        game.board,
        np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, -1, 0, 0, 0],
                [0, 0, 1, 1, -1, 0, 0, 0],
                [0, 0, 0, 1, -1, 0, 0, 0],
                [0, 0, 0, 0, -1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ]
        ),
    )
    assert game.player_value == BLACK_VALUE


def test_set_position(game):
    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 1, 1, -1, 0, 0, 0],
            [0, 0, 0, 1, -1, 0, 0, 0],
            [0, 0, 0, 0, -1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    game.set_position(board, BLACK_VALUE)

    assert np.array_equal(
        game.board,
        np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, -1, 0, 0, 0],
                [0, 0, 1, 1, -1, 0, 0, 0],
                [0, 0, 0, 1, -1, 0, 0, 0],
                [0, 0, 0, 0, -1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ]
        ),
    )
    assert game.player_value == BLACK_VALUE
    assert np.array_equal(
        game.surrounding_cells,
        np.array(
            [
                (1, 2),
                (1, 3),
                (1, 4),
                (2, 2),
                (2, 4),
                (2, 5),
                (3, 1),
                (3, 2),
                (3, 5),
                (3, 6),
                (4, 1),
                (4, 6),
                (5, 1),
                (5, 2),
                (5, 3),
                (5, 4),
                (5, 6),
                (6, 4),
                (6, 5),
                (6, 6),
            ],
        ),
    )
    assert dict_to_str(game.sandwiches) == dict_to_str(
        {
            "3,5": np.array([[4, 5]]),
            "5,1": np.array([[4, 2]]),
            "5,2": np.array([[4, 3]]),
            "5,3": np.array([[4, 3]]),
            "5,4": np.array([[4, 4]]),
            "5,6": np.array([[4, 5]]),
        }
    )
    assert np.array_equal(
        game.indicators,
        np.array([(3, 5), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6)]),
    )

    game.set_position(board, WHITE_VALUE)

    assert np.array_equal(
        game.board,
        np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, -1, 0, 0, 0],
                [0, 0, 1, 1, -1, 0, 0, 0],
                [0, 0, 0, 1, -1, 0, 0, 0],
                [0, 0, 0, 0, -1, 1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ]
        ),
    )
    assert game.player_value == WHITE_VALUE
    assert np.array_equal(
        game.surrounding_cells,
        np.array(
            [
                (1, 2),
                (1, 3),
                (1, 4),
                (2, 2),
                (2, 4),
                (2, 5),
                (3, 1),
                (3, 2),
                (3, 5),
                (3, 6),
                (4, 1),
                (4, 6),
                (5, 1),
                (5, 2),
                (5, 3),
                (5, 4),
                (5, 6),
                (6, 4),
                (6, 5),
                (6, 6),
            ],
        ),
    )
    assert dict_to_str(game.sandwiches) == dict_to_str(
        {
            "1,2": np.array([[2, 3], [3, 4]]),
            "1,3": np.array([[2, 3], [3, 3]]),
            "2,2": np.array([[3, 3]]),
            "2,4": np.array([[3, 4], [3, 3]]),
            "2,5": np.array([[3, 4]]),
            "6,5": np.array([[5, 5]]),
            "6,6": np.array([[5, 5]]),
        }
    )
    assert np.array_equal(
        game.indicators,
        np.array(
            [(1, 2), (1, 3), (2, 2), (2, 4), (2, 5), (6, 5), (6, 6)],
        ),
    )


def test_get_black_legal_moves(game):
    assert np.array_equal(
        game.get_black_legal_moves(),
        np.array([(2, 3), (3, 2), (4, 5), (5, 4)]),
    )

    board = np.array(
        [
            [-1, 0, -1, 0, -1, 0, 1, 0],
            [-1, 1, 1, -1, -1, 1, 1, 1],
            [-1, 0, 1, 0, -1, 0, 1, 0],
            [-1, 1, 1, 1, 1, 1, 1, 1],
            [-1, 0, 1, 0, 1, 0, 1, 0],
            [-1, 1, -1, -1, -1, 1, -1, 1],
            [-1, 0, -1, 0, 1, 0, 1, 0],
            [-1, -1, -1, -1, -1, -1, -1, 1],
        ]
    )
    game.set_position(board, BLACK_VALUE)

    assert np.array_equal(game.get_black_legal_moves(), np.array([]))

    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 1, 1, -1, 0, 0, 0],
            [0, 0, 0, 1, -1, 0, 0, 0],
            [0, 0, 0, 0, -1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    game.set_position(board, WHITE_VALUE)

    assert np.array_equal(
        game.get_black_legal_moves(),
        np.array([(3, 5), (5, 1), (5, 2), (5, 3), (5, 4), (5, 6)]),
    )


def test_get_white_legal_moves(game):
    assert np.array_equal(
        game.get_white_legal_moves(),
        np.array([(2, 4), (3, 5), (4, 2), (5, 3)]),
    )

    board = np.array(
        [
            [-1, 0, -1, 0, -1, 0, 1, 0],
            [-1, 1, 1, -1, -1, 1, 1, 1],
            [-1, 0, 1, 0, -1, 0, 1, 0],
            [-1, 1, 1, 1, 1, 1, 1, 1],
            [-1, 0, 1, 0, 1, 0, 1, 0],
            [-1, 1, -1, -1, -1, 1, -1, 1],
            [-1, 0, -1, 0, 1, 0, 1, 0],
            [-1, -1, -1, -1, -1, -1, -1, 1],
        ]
    )
    game.set_position(board, WHITE_VALUE)

    assert np.array_equal(game.get_white_legal_moves(), np.array([]))

    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 1, 1, -1, 0, 0, 0],
            [0, 0, 0, 1, -1, 0, 0, 0],
            [0, 0, 0, 0, -1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    game.set_position(board, BLACK_VALUE)

    assert np.array_equal(
        game.get_white_legal_moves(),
        np.array([(1, 2), (1, 3), (2, 2), (2, 4), (2, 5), (6, 5), (6, 6)]),
    )


def test_get_black_legal_moves_count(game):
    assert game.get_black_legal_moves_count() == 4

    board = np.array(
        [
            [-1, 0, -1, 0, -1, 0, 1, 0],
            [-1, 1, 1, -1, -1, 1, 1, 1],
            [-1, 0, 1, 0, -1, 0, 1, 0],
            [-1, 1, 1, 1, 1, 1, 1, 1],
            [-1, 0, 1, 0, 1, 0, 1, 0],
            [-1, 1, -1, -1, -1, 1, -1, 1],
            [-1, 0, -1, 0, 1, 0, 1, 0],
            [-1, -1, -1, -1, -1, -1, -1, 1],
        ]
    )
    game.set_position(board, BLACK_VALUE)

    assert game.get_black_legal_moves_count() == 0

    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 1, 1, -1, 0, 0, 0],
            [0, 0, 0, 1, -1, 0, 0, 0],
            [0, 0, 0, 0, -1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    game.set_position(board, WHITE_VALUE)

    assert game.get_black_legal_moves_count() == 6


def test_get_white_legal_moves_count(game):
    assert game.get_white_legal_moves_count() == 4

    board = np.array(
        [
            [-1, 0, -1, 0, -1, 0, 1, 0],
            [-1, 1, 1, -1, -1, 1, 1, 1],
            [-1, 0, 1, 0, -1, 0, 1, 0],
            [-1, 1, 1, 1, 1, 1, 1, 1],
            [-1, 0, 1, 0, 1, 0, 1, 0],
            [-1, 1, -1, -1, -1, 1, -1, 1],
            [-1, 0, -1, 0, 1, 0, 1, 0],
            [-1, -1, -1, -1, -1, -1, -1, 1],
        ]
    )
    game.set_position(board, WHITE_VALUE)

    assert game.get_white_legal_moves_count() == 0

    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 1, 1, -1, 0, 0, 0],
            [0, 0, 0, 1, -1, 0, 0, 0],
            [0, 0, 0, 0, -1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )
    game.set_position(board, BLACK_VALUE)

    assert game.get_white_legal_moves_count() == 7


def test_get_black_empty_neighbors_count(game, rng):
    assert game.get_black_empty_neighbors_count() == 10

    game.board.fill(*rng.choice([BLACK_VALUE, WHITE_VALUE], 1))

    assert game.get_black_empty_neighbors_count() == 0

    game.board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 1, 1, -1, 0, 0, 0],
            [0, 0, 0, 1, -1, 0, 0, 0],
            [0, 0, 0, 0, -1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )

    assert game.get_black_empty_neighbors_count() == 14

    game.board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 0, -1, -1, -1, 0, 0],
            [0, 0, -1, -1, -1, -1, -1, 0],
            [0, 0, 0, -1, -1, -1, 0, 0],
            [0, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )

    assert game.get_black_empty_neighbors_count() == 0


def test_get_white_empty_neighbors_count(game, rng):
    assert game.get_white_empty_neighbors_count() == 10

    game.board.fill(*rng.choice([BLACK_VALUE, WHITE_VALUE], 1))

    assert game.get_white_empty_neighbors_count() == 0

    game.board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, -1, 0, 0, 0],
            [0, 0, 1, 1, -1, 0, 0, 0],
            [0, 0, 0, 1, -1, 0, 0, 0],
            [0, 0, 0, 0, -1, 1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ]
    )

    assert game.get_white_empty_neighbors_count() == 11

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
        ]
    )

    assert game.get_white_empty_neighbors_count() == 0
