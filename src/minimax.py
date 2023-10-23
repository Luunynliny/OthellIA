from copy import deepcopy
from typing import Callable, Type

import numpy as np

from game import Game


def minimax(
    game: Type[Game],
    depth: int,
    static_evaluation_func: Callable,
    maximazing_player: bool,
) -> float:
    """Analyse the current board position according to a static evaluation function and
    a depth.

    Args:
        game (Type[Game]): a game.
        depth (int): depth of the search.
        static_evaluation_func (Callable): position evaluation function.
        maximazing_player (bool): if we want to maximizing the score of the player.

    Returns:
        float: evaluation score.
    """
    # https://www.youtube.com/watch?v=l-hh51ncgDI
    if depth == 0 or game.is_over:
        return static_evaluation_func(game)

    if maximazing_player:
        max_eval = -np.inf

        for move in game.indicators:
            game_copy = deepcopy(game)  # Copy the game without reference
            game_copy.play_piece(move)

            child_eval = minimax(
                game_copy, depth - 1, static_evaluation_func, False
            )
            max_eval = max(max_eval, child_eval)

        return max_eval
    else:
        min_eval = np.inf

        for move in game.indicators:
            game_copy = deepcopy(game)  # Copy the game without reference
            game_copy.play_piece(move)

            child_eval = minimax(
                game_copy, depth - 1, static_evaluation_func, True
            )
            min_eval = min(min_eval, child_eval)

        return min_eval
