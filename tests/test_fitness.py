import numpy as np
import pytest

from genetic.fitness import play_match
from othellia.static_evaluation import StaticEvaluation
from settings.values import WHITE_VALUE


@pytest.fixture
def static_evaluation():
    return StaticEvaluation()


def test_play_match(static_evaluation):
    chromosome1 = np.array([1, 1, 1, 1, 1, 1])
    chromosome2 = np.array([0, 0, 0, 0, 0, 0])
    depth = 2

    result, transcript = play_match(chromosome1, chromosome2, depth)

    assert result == WHITE_VALUE
    assert (
        transcript
        == "c4e3f4c5e6f5d6f6d3c3g4g6h6g7g5h5f8g3h4h8h3h7f7g8e8d8d7h2d2c8f2f3g2c6e7h1e2g"
        + "1c2f1b6b5c7a6a5c1b2b3a7a4a3b4b7a2a1a8d1b1e1b8"
    )
