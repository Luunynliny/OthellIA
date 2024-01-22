from itertools import permutations
from math import factorial
from typing import cast

import numpy as np
from tqdm.notebook import tqdm

from othellia.game import Game
from othellia.minimax import think
from othellia.static_evaluation import StaticEvaluation
from settings import values
from utils.game import cell_index_to_notation


def play_match(
        chromosome_black: np.ndarray[np.float64, np.dtype[np.float64]],
        chromosome_white: np.ndarray[np.float64, np.dtype[np.float64]],
        depth: int,
) -> tuple[int, str]:
    """Plays an Othello game between two chromosomes and returns the result.

    Args:
        chromosome_black (np.ndarray[np.float64, np.dtype[np.float64]]): a chromosome
        playing as black.
        chromosome_white (np.ndarray[np.float64, np.dtype[np.float64]]): a chromosome
        playing as white.
        depth (int): depth of the minimax search.

    Returns:
        int: result of the match (1 black, -1 white, 0 draw).
        str: transcript of the game.
    """
    game = Game()
    static_evaluation = StaticEvaluation()

    transcript = ""

    while not game.is_over:
        match game.player_value:
            case values.BLACK_VALUE:
                static_evaluation.set_evaluation_weights(
                    cast(
                        tuple[float, float, float, float, float, float],
                        chromosome_black,
                    )
                )
            case values.WHITE_VALUE:
                static_evaluation.set_evaluation_weights(
                    cast(
                        tuple[float, float, float, float, float, float],
                        chromosome_white,
                    )
                )

        # Play the best legal move
        move = think(game, depth, static_evaluation.evaluate)
        game.play_piece(move)

        # Keep record of the move
        transcript += cell_index_to_notation(move)

    return game.get_winner(), transcript


def play_tournament(
        chromosomes: np.ndarray[np.float64, np.dtype[np.float64]], depth: int
) -> np.ndarray[np.float64, np.dtype[np.float64]]:
    """Runs a tournament by making each chromosomes play against each other as black
    and white, and returns each chromosomes score.

    A victory is represented by 1 points, a draw by 0 and a loss by -1.

    Args:
        chromosomes (np.ndarray[np.float64, np.dtype[np.float64]]): population of
        chromosome.
        depth (int): depth of the minimax search.

    Returns:
        np.ndarray[np.float64, np.dtype[np.float64]]: list of chromosomes score.
    """
    n_chromosomes = len(chromosomes)

    scores = np.zeros(n_chromosomes)

    # Iterate over each possible chromosome index pairs
    for b_index, w_index in tqdm(
            permutations(range(n_chromosomes), 2),
            desc="Tournament",
            total=factorial(n_chromosomes) // factorial(n_chromosomes - 2),
    ):
        winner, _ = play_match(
            chromosomes[b_index], chromosomes[w_index], depth
        )

        match winner:
            case values.BLACK_VALUE:
                scores[b_index] += 1
                scores[w_index] += -1
            case values.WHITE_VALUE:
                scores[b_index] += -1
                scores[w_index] += 1

    return np.array(scores, dtype=int)
