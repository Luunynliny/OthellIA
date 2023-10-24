import numpy as np
import pytest

from othellia.game import Game
from othellia.static_evaluation import (
    actual_mobility,
    coin_parity,
    corners_captured,
    evaluate,
    future_corners_captured,
    potential_mobility,
    static_weights,
)
from settings.values import BLACK_VALUE, WHITE_VALUE


@pytest.fixture
def game():
    return Game()


def test_coin_parity(game):
    assert coin_parity(game) == 0

    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 1, 1, 1, 0, 0, 0],
            [0, 0, 0, 1, -1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ],
        dtype=int,
    )
    game.set_position(board, *np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

    assert coin_parity(game) == 60

    board = np.array(
        [
            [0, 0, 0, 1, 1, 0, 0, 0],
            [0, 0, -1, 1, 1, 1, 0, 0],
            [-1, -1, -1, 1, -1, -1, -1, -1],
            [-1, -1, -1, 1, -1, 1, -1, 1],
            [-1, 1, 1, -1, 1, -1, 1, 1],
            [1, 1, 1, 1, -1, -1, 0, 0],
            [0, 0, 1, -1, -1, -1, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ],
        dtype=int,
    )
    game.set_position(board, *np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

    assert coin_parity(game) == -5

    board = np.array(
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
    game.set_position(board, *np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

    assert coin_parity(game) == 100


def test_actual_mobility(game):
    assert actual_mobility(game) == 0

    board = np.array(
        [
            [1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, -1, 0, 0, 0, 0],
            [1, 1, 1, -1, -1, 0, 0, 0],
            [1, -1, 1, -1, -1, -1, 0, 1],
            [1, 1, -1, -1, -1, -1, -1, -1],
            [1, -1, 1, 1, 1, 1, 1, 1],
            [1, 1, -1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0],
        ],
        dtype=int,
    )
    game.set_position(board, *np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

    assert actual_mobility(game) == 40

    board = np.array(
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
    game.set_position(board, *np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

    assert actual_mobility(game) == 0


def test_potential_mobility(game):
    assert potential_mobility(game) == 0

    board = np.array(
        [
            [1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, -1, 0, 0, 0, 0],
            [1, 1, 1, -1, -1, 0, 0, 0],
            [1, -1, 1, -1, -1, -1, 0, 1],
            [1, 1, -1, -1, -1, -1, -1, -1],
            [1, -1, 1, 1, 1, 0, 0, 0],
            [1, 1, -1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0],
        ],
        dtype=int,
    )
    game.set_position(board, *np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

    assert potential_mobility(game) == pytest.approx(5.26, rel=1e-3)

    board = np.array(
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
    game.set_position(board, *np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

    assert potential_mobility(game) == -100

    board = np.full(
        (8, 8), *np.random.choice([BLACK_VALUE, WHITE_VALUE], 1), dtype=int
    )
    game.set_position(board, *np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

    assert potential_mobility(game) == 0


def test_corners_captured(game):
    assert corners_captured(game) == 0

    board = np.array(
        [
            [1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, -1, 0, 0, 0, 0],
            [1, 1, 1, -1, -1, 0, 0, 0],
            [1, -1, 1, -1, -1, -1, 0, 1],
            [1, 1, -1, -1, -1, -1, -1, -1],
            [1, -1, 1, 1, 1, 0, 0, 0],
            [1, 1, -1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0],
        ],
        dtype=int,
    )
    game.set_position(board, *np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

    assert corners_captured(game) == 100

    board = np.array(
        [
            [1, 1, 1, -1, -1, -1, -1, -1],
            [1, 1, 1, -1, -1, -1, -1, 1],
            [1, 1, 1, -1, -1, 1, 1, 1],
            [1, -1, 1, -1, -1, -1, 1, 1],
            [1, 1, -1, -1, -1, -1, -1, -1],
            [1, -1, 1, 1, 1, 0, 0, 0],
            [1, 1, -1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ],
        dtype=int,
    )
    game.set_position(board, *np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

    assert corners_captured(game) == 50


def test_future_corners_captured(game):
    assert corners_captured(game) == 0

    board = np.array(
        [
            [1, 1, 1, -1, -1, -1, -1, -1],
            [1, 1, 1, -1, -1, -1, -1, 1],
            [1, 1, 1, -1, -1, 1, 1, 1],
            [1, -1, 1, -1, -1, -1, 1, 1],
            [1, 1, -1, -1, -1, -1, -1, -1],
            [1, -1, 1, 1, 1, 0, 0, 0],
            [1, 1, -1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 1],
        ],
        dtype=int,
    )
    game.set_position(board, *np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

    assert future_corners_captured(game) == 0

    board = np.array(
        [
            [0, 1, 1, -1, -1, -1, -1, -1],
            [0, 1, 1, -1, -1, -1, -1, 1],
            [1, 1, 1, -1, -1, 1, 1, 1],
            [1, -1, 1, -1, -1, -1, 1, 1],
            [1, 1, -1, -1, -1, -1, -1, -1],
            [1, -1, 1, 1, 1, 0, 0, 0],
            [1, 0, -1, 1, 1, 1, 0, 0],
            [0, 1, 1, 1, 1, 1, 1, 1],
        ],
        dtype=int,
    )
    game.set_position(board, *np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

    assert future_corners_captured(game) == -100


def test_static_weights(game):
    assert static_weights(game) == 0

    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 1, 0, 0, 0],
            [0, 0, 0, 1, 1, 1, 0, 0],
            [0, 0, -1, 1, 1, 1, 1, 0],
            [0, 0, -1, -1, 1, 1, -1, 0],
            [0, -1, -1, -1, -1, 0, 1, 0],
            [-1, 0, 0, 0, 0, 0, 0, 1],
        ],
        dtype=int,
    )
    game.set_position(board, *np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

    assert static_weights(game) == 7

    board = np.array(
        [
            [1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, -1, 0, 0, 0, 0],
            [1, 1, 1, -1, -1, 0, 0, 0],
            [1, -1, 1, -1, -1, -1, 0, 1],
            [1, 1, -1, -1, -1, -1, -1, -1],
            [1, -1, 1, 1, 1, 1, 1, 1],
            [1, 1, -1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0],
        ],
        dtype=int,
    )
    game.set_position(board, *np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

    assert static_weights(game) == 2


def test_evaluate(game):
    assert evaluate(game) == 0

    board = np.array(
        [
            [1, 1, 1, 0, 0, 0, 0, 0],
            [1, 1, 1, -1, 0, 0, 0, 0],
            [1, 1, 1, -1, -1, 0, 0, 0],
            [1, -1, 1, -1, -1, -1, 0, 1],
            [1, 1, -1, -1, -1, -1, -1, -1],
            [1, -1, 1, 1, 1, 1, 1, 1],
            [1, 1, -1, 1, 1, 1, 0, 0],
            [1, 1, 1, 1, 1, 1, 1, 0],
        ],
        dtype=int,
    )
    game.set_position(board, *np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

    assert evaluate(game) == 27.65
