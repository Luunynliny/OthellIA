import numpy as np
import pytest

from genetic.fitness import play_match, play_tournament
from othellia.static_evaluation import StaticEvaluation
from settings.values import BLACK_VALUE


@pytest.fixture
def static_evaluation():
    return StaticEvaluation()


def test_play_match(static_evaluation):
    chromosome1 = np.array([1, 1, 1, 1, 1, 1])
    chromosome2 = np.array([0, 0, 0, 0, 0, 0])
    depth = 2

    result, transcript = play_match(chromosome1, chromosome2, depth)

    assert result == BLACK_VALUE
    assert (
        transcript
        == "c4c3e6b4b3a3b2b1a4a5a1b5c1d2c2a2a6b6c5c6d1e3c7a7d6d7c8b7d3d8e8e2f4e7"
        + "f8f7f5f3f6g3e1f2g5g4f1g1g2g6a8b8g7g8h5h3h6h4h2h1h8h7"
    )


def test_play_tournament(static_evaluation):
    chromosomes = np.array(
        [
            [1, 1, 1, 1, 1, 1],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0],
        ]
    )
    depth = 1

    assert np.array_equal(
        play_tournament(chromosomes, depth),
        np.array([6, -2, -2, -2]),
    )
