import numpy as np
import pytest

from othellia.game import Game
from othellia.minimax import minimax, think
from othellia.static_evaluation import StaticEvaluation
from settings.values import BLACK_VALUE


@pytest.fixture
def game():
    return Game()


@pytest.fixture
def static_evaluation():
    return StaticEvaluation()


def test_minimax_depth_zero(game, static_evaluation):
    assert (
        minimax(game, 0, -np.inf, np.inf, static_evaluation.coin_parity, True)
        == 0
    )
    assert (
        minimax(game, 0, -np.inf, np.inf, static_evaluation.coin_parity, False)
        == 0
    )


def test_minimax(game, static_evaluation):
    depth = 3

    assert minimax(
        game, depth, -np.inf, np.inf, static_evaluation.coin_parity, True
    ) == pytest.approx(42.85, rel=1e-3)
    assert minimax(
        game, depth, -np.inf, np.inf, static_evaluation.coin_parity, False
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
        game, depth, -np.inf, np.inf, static_evaluation.coin_parity, True
    ) == pytest.approx(38.46, rel=1e-3)
    assert minimax(
        game, depth, -np.inf, np.inf, static_evaluation.coin_parity, False
    ) == pytest.approx(7.69, rel=1e-3)


def test_think(game, static_evaluation):
    depth = 3

    assert np.array_equal(
        think(game, depth, static_evaluation.coin_parity), (2, 3)
    )
    game.next_player_turn()
    assert np.array_equal(
        think(game, depth, static_evaluation.coin_parity), (2, 4)
    )

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

    assert np.array_equal(
        think(game, depth, static_evaluation.coin_parity), (6, 4)
    )
    game.next_player_turn()
    assert np.array_equal(
        think(game, depth, static_evaluation.coin_parity), (1, 4)
    )
