import numpy as np
import pytest

from othellia.game import Game
from othellia.minimax import minimax, think
from othellia.static_evaluation import coin_parity
from settings.values import BLACK_VALUE


@pytest.fixture
def game():
    return Game()


def test_minimax_depth_zero(game):
    assert minimax(game, 0, -np.inf, np.inf, coin_parity, True) == 0
    assert minimax(game, 0, -np.inf, np.inf, coin_parity, False) == 0


def test_minimax(game):
    depth = 3

    assert minimax(
        game, depth, -np.inf, np.inf, coin_parity, True
    ) == pytest.approx(42.85, rel=1e-3)
    assert minimax(
        game, depth, -np.inf, np.inf, coin_parity, False
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
        game, depth, -np.inf, np.inf, coin_parity, True
    ) == pytest.approx(38.46, rel=1e-3)
    assert minimax(
        game, depth, -np.inf, np.inf, coin_parity, False
    ) == pytest.approx(7.69, rel=1e-3)


def test_think(game):
    depth = 3

    assert think(game, depth, coin_parity) == 0
    game.next_player_turn()
    assert think(game, depth, coin_parity) == 0

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

    assert think(game, depth, coin_parity) == 5
    game.next_player_turn()
    assert think(game, depth, coin_parity) == 1
