import numpy as np
import pytest

from settings.cell_values import BLACK_VALUE, WHITE_VALUE
from static_evaluation import StaticEvaluation


@pytest.fixture
def static_evaluation():
    return StaticEvaluation()


def test_coin_parity(static_evaluation):
    board = np.array(
        [
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, -1, 1, 0, 0, 0],
            [0, 0, 0, 1, -1, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
            [0, 0, 0, 0, 0, 0, 0, 0],
        ],
        dtype=int,
    )

    assert static_evaluation.coin_parity(board, BLACK_VALUE) == 0
    assert static_evaluation.coin_parity(board, WHITE_VALUE) == 0

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

    assert static_evaluation.coin_parity(board, BLACK_VALUE) == -5
    assert static_evaluation.coin_parity(board, WHITE_VALUE) == 5

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

    assert static_evaluation.coin_parity(board, BLACK_VALUE) == 100
    assert static_evaluation.coin_parity(board, WHITE_VALUE) == -100
