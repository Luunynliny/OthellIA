import numpy as np
import pytest

from game import Game
from settings import BLACK_VALUE, BOARD_SIZE, EMPTY_VALUE, WHITE_VALUE


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
                [0, 0, 0, 1, -1, 0, 0, 0],
                [0, 0, 0, -1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            dtype=np.intc,
        ),
    )

    assert np.array_equal(
        game.indicators,
        np.array([(2, 4), (3, 5), (4, 2), (5, 3)], dtype=(int, 2)),
    )


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
                [0, 0, 0, 1, -1, 0, 0, 0],
                [0, 0, 0, -1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            dtype=np.intc,
        ),
    )

    assert np.array_equal(
        game.indicators,
        np.array([(2, 4), (3, 5), (4, 2), (5, 3)], dtype=(int, 2)),
    )


def test_mouse_pos_to_cell_index(game):
    assert game.mouse_pos_to_cell_index((0, 0)) == (0, 0)
    assert game.mouse_pos_to_cell_index((BOARD_SIZE, BOARD_SIZE)) == (8, 8)
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


def test_play_piece_black(game):
    game.play_piece((1, 1), value=BLACK_VALUE)

    assert np.array_equal(
        game.board,
        np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, -1, 0, 0, 0],
                [0, 0, 0, -1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ]
        ),
    )


def test_play_piece_white(game):
    game.play_piece((1, 1), value=WHITE_VALUE)

    assert np.array_equal(
        game.board,
        np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, -1, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 1, -1, 0, 0, 0],
                [0, 0, 0, -1, 1, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ]
        ),
    )


def test_is_move_legal(game):
    legal_move = (3, 5)
    illegal_move = (0, 0)

    assert game.is_move_legal(legal_move)
    assert not game.is_move_legal(illegal_move)


def test_remove_indicator(game):
    game.remove_indicator((2, 4))

    assert np.array_equal(
        game.indicators,
        np.array([(3, 5), (4, 2), (5, 3)], dtype=(int, 2)),
    )

    game.remove_indicator((4, 2))

    assert np.array_equal(
        game.indicators,
        np.array([(3, 5), (5, 3)], dtype=(int, 2)),
    )
