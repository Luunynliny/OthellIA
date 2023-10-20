import numpy as np
import pytest

from game import Game
from settings.cell_values import BLACK_VALUE, WHITE_VALUE
from static_evaluation import StaticEvaluation


@pytest.fixture
def game():
    return Game()


@pytest.fixture
def static_evaluation():
    return StaticEvaluation()


def test_coin_parity(game, static_evaluation):
    assert static_evaluation.coin_parity(game) == 0

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

    assert static_evaluation.coin_parity(game) == 60

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

    assert static_evaluation.coin_parity(game) == -5

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

    assert static_evaluation.coin_parity(game) == 100


def test_actual_mobility(game, static_evaluation):
    assert static_evaluation.actual_mobility(game) == 0

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

    assert static_evaluation.actual_mobility(game) == 40

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

    assert static_evaluation.actual_mobility(game) == 0


def test_potential_mobility(game, static_evaluation):
    assert static_evaluation.potential_mobility(game) == 0

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

    assert static_evaluation.potential_mobility(game) == pytest.approx(
        5.26, rel=1e-3
    )

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

    assert static_evaluation.potential_mobility(game) == -100

    board = np.full(
        (8, 8), *np.random.choice([BLACK_VALUE, WHITE_VALUE], 1), dtype=int
    )
    game.set_position(board, *np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

    assert static_evaluation.potential_mobility(game) == 0


def test_corners_captured(game, static_evaluation):
    assert static_evaluation.corners_captured(game) == 0

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

    assert static_evaluation.corners_captured(game) == 100

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

    assert static_evaluation.corners_captured(game) == 50


def test_future_corners_captured(game, static_evaluation):
    assert static_evaluation.corners_captured(game) == 0

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

    assert static_evaluation.future_corners_captured(game) == 0

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

    assert static_evaluation.future_corners_captured(game) == -100


def test_static_weights(game, static_evaluation):
    assert static_evaluation.static_weights(game) == 0

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

    assert static_evaluation.static_weights(game) == 7

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

    assert static_evaluation.static_weights(game) == 2


def test_evaluate(game, static_evaluation):
    weights = [0.3, 0.15, 0.15, 0.1, 0.1, 0.2]

    assert static_evaluation.evaluate(game, weights) == 0

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

    assert static_evaluation.evaluate(game, weights) == 27.65
