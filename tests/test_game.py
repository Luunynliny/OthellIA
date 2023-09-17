import numpy as np
import pytest

from game import Game
from settings import BLACK_VALUE, BOARD_SIZE, EMPTY_VALUE, WHITE_VALUE


@pytest.fixture
def game():
    return Game()


def test_initialization(game):
    assert np.array_equal(
        game.board, np.full((8, 8), EMPTY_VALUE, dtype=np.intc)
    )


def test_reset_game(game):
    game.board[0:2, 5:6] = 1
    game.reset_game()

    assert np.array_equal(
        game.board, np.full((8, 8), EMPTY_VALUE, dtype=np.intc)
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
                [0, BLACK_VALUE, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
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
                [0, WHITE_VALUE, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ]
        ),
    )
