import numpy as np
import pytest

from game import Game
from minimax import minimax
from settings.cell_values import BLACK_VALUE
from static_evaluation import StaticEvaluation


@pytest.fixture
def game():
    return Game()


@pytest.fixture
def static_evaluation():
    return StaticEvaluation()


def test_minimax_depth_zero(game, static_evaluation):
    assert minimax(game, 0, static_evaluation.coin_parity, True) == 0
    assert minimax(game, 0, static_evaluation.coin_parity, False) == 0


def test_minimax_maximize(game, static_evaluation):
    depth = 3

    assert minimax(
        game, depth, static_evaluation.coin_parity, True
    ) == pytest.approx(42.85, rel=1e-3)
    assert minimax(
        game, depth, static_evaluation.coin_parity, False
    ) == pytest.approx(42.85, rel=1e-3)

    game.set_position(
        np.array(
            [
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 1, 0, 0, 0],
                [0, 0, 0, 1, -1, -1, 0, 0],
                [0, 0, 1, 1, -1, -1, 0, 0],
                [0, 0, 0, -1, 0, -1, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
                [0, 0, 0, 0, 0, 0, 0, 0],
            ],
            dtype=int,
        ),
        BLACK_VALUE,
    )

    assert minimax(
        game, depth, static_evaluation.coin_parity, True
    ) == pytest.approx(38.46, rel=1e-3)
    assert minimax(
        game, depth, static_evaluation.coin_parity, False
    ) == pytest.approx(7.69, rel=1e-3)
