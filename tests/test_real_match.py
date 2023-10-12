import numpy as np
import pytest

from game import Game
from settings.cell_values import BLACK_VALUE, WHITE_VALUE


@pytest.fixture
def game():
    return Game()


def test_bertrandias_vs_kashiwabara(game):
    # https://www.ffothello.org/championnat-de-france-2022-kashiwabara-conserve-son-titre-bertrandias-2e/
    t = (
        "d3c5e6f5f6e3d6f7g6c4c6e7d7c3d8e8f3f4g4c8g3g5f8g8b5h5f2d2b4h4e2h3d1f1g1e1h2c2h6"
        "h1g2h7c1c7g7a5b7h8b6b3a3a7a4a2a6b1a1b2b8a8"
    )

    game.load_transcript(t)

    assert np.array_equal(
        game.board,
        np.array(
            [
                [1, -1, -1, -1, -1, -1, -1, -1],
                [1, -1, -1, -1, -1, -1, 1, -1],
                [1, -1, -1, -1, -1, 1, -1, -1],
                [1, 1, -1, -1, -1, -1, -1, -1],
                [1, 1, -1, -1, -1, -1, 1, -1],
                [1, 1, -1, -1, -1, -1, 1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, -1, -1, -1, -1, -1],
            ],
            dtype=int,
        ),
    )
    assert game.get_winner() == WHITE_VALUE


def test_lazard_vs_juigner(game):
    # https://www.ffothello.org/championnat-de-france-2016-3e-titre-pour-manu-lazard/
    t = (
        "d3c3c4c5d6e3b5e6f6a6f5b6b4b3f2e2a4c6a5a3f3f4d7e7d8f8c2d2g4c8b8g5e1d1h6c7g6g3f7"
        "f1b1c1g1h4h5g2e8b7g8g7a7a8h8h7a2a1h1b2h3h2"
    )

    game.load_transcript(t)

    assert np.array_equal(
        game.board,
        np.array(
            [
                [-1, 1, 1, 1, 1, 1, 1, 1],
                [-1, -1, -1, -1, -1, -1, -1, -1],
                [-1, -1, -1, 1, 1, 1, -1, 1],
                [-1, -1, 1, 1, 1, -1, 1, 1],
                [-1, 1, 1, 1, 1, 1, -1, 1],
                [-1, 1, -1, -1, 1, 1, -1, 1],
                [-1, -1, -1, -1, -1, -1, -1, 1],
                [-1, 1, 1, 1, 1, 1, 1, 1],
            ],
            dtype=int,
        ),
    )

    assert game.get_winner() == BLACK_VALUE


def test_fronmark_vs_berg(game):
    # https://www.worldothello.org/ratings/player?playerID=1454
    t = (
        "f5d6c3d3c4f4c5b3e2e3c2b4c6d1f2d2a3e6d7f7c1b1e1f1g4g1f3g5e7g3h4h3f6e8d8c8c7a5a2"
        "a4a6f8b5h5b2g6g7b8h7b7b6h6h8a7a8g8g2a1h2"
    )

    game.load_transcript(t)

    assert np.array_equal(
        game.board,
        np.array(
            [
                [-1, -1, -1, -1, -1, -1, -1, 0],
                [1, -1, 1, 1, 1, 1, 1, 1],
                [1, 1, -1, 1, -1, 1, 1, 1],
                [1, 1, 1, -1, 1, 1, -1, 1],
                [1, 1, -1, 1, 1, 1, -1, 1],
                [1, -1, 1, 1, -1, 1, -1, 1],
                [1, 1, -1, 1, 1, -1, -1, 1],
                [1, -1, -1, -1, -1, -1, -1, 1],
            ],
            dtype=int,
        ),
    )

    assert game.get_winner() == BLACK_VALUE


def test_kanae_vs_hoshikawa(game):
    # https://www.youtube.com/watch?v=wle0NNd_NPs
    t = (
        "d3e3f3c5c6c3b6b5a4c7b2a6f6f5a7a8b7a5c8b8g6a3c4d8e6d7e2e1d6b4f2c2b3a2a1b1c1d1f7"
        "f8d2f1g1e7e8f4g8g7g5"
    )

    game.load_transcript(t)

    assert np.array_equal(
        game.board,
        np.array(
            [
                [-1, -1, -1, -1, -1, -1, -1, 0],
                [-1, -1, -1, -1, -1, -1, 0, 0],
                [-1, -1, -1, -1, -1, -1, 0, 0],
                [-1, -1, -1, -1, -1, -1, 0, 0],
                [-1, -1, -1, -1, -1, -1, -1, 0],
                [-1, -1, -1, -1, -1, -1, -1, 0],
                [-1, -1, -1, -1, -1, -1, -1, 0],
                [-1, -1, -1, -1, -1, -1, -1, 0],
            ],
            dtype=int,
        ),
    )

    assert game.get_winner() == WHITE_VALUE
