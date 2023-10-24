from copy import deepcopy
from typing import Callable, Type

import numpy as np

from othellia.game import Game
from settings.values import BLACK_VALUE


def minimax(
    game: Type[Game],
    depth: int,
    alpha: float,
    beta: float,
    static_evaluation_func: Callable,
    maximazing_player: bool,
) -> float:
    """Analyse the current board position according to a static evaluation function and
    a depth.

    Args:
        game (Type[Game]): a game.
        depth (int): depth of the search.
        alpha (float): alpha parameter of pruning.
        beta (float): beta parameter of pruning.
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
                game_copy,
                depth - 1,
                alpha,
                beta,
                static_evaluation_func,
                False,
            )
            max_eval = max(max_eval, child_eval)

            alpha = max(alpha, max_eval)
            if beta <= alpha:
                break

        return max_eval
    else:
        min_eval = np.inf

        for move in game.indicators:
            game_copy = deepcopy(game)  # Copy the game without reference
            game_copy.play_piece(move)

            child_eval = minimax(
                game_copy, depth - 1, alpha, beta, static_evaluation_func, True
            )
            min_eval = min(min_eval, child_eval)

            beta = min(beta, min_eval)
            if beta <= alpha:
                break

        return min_eval


def think(game, depth: int, static_evaluation_func: Callable) -> int:
    """Return the best move to play according to the game position,
    the player turn, a searching depth and a static evaluation method.

    Args:
        game (Type[Game]): a game.
        depth (int): depth of the search.
        static_evaluation_func (Callable): position evaluation function.


    Returns:
        int: indicator index of the best move.
    """
    maximazing_player = game.player_value == BLACK_VALUE
    scores = []

    for legal_move in game.indicators:
        game_copy = deepcopy(game)  # Copy without reference
        game_copy.play_piece(legal_move)

        scores.append(
            minimax(
                game_copy,
                depth,
                -np.inf,
                np.inf,
                static_evaluation_func,
                maximazing_player,
            )
        )

    return np.array(scores).argmax()
