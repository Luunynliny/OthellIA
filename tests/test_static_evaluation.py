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
    game.set_position(board, np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

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
    game.set_position(board, np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

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
    game.set_position(board, np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

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
    game.set_position(board, np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

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
    game.set_position(board, np.random.choice([BLACK_VALUE, WHITE_VALUE], 1))

    assert static_evaluation.actual_mobility(game) == 0
