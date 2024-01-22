from copy import deepcopy
from typing import Callable, cast

import numpy as np

from othellia.game import Game
from settings.values import BLACK_VALUE


def minimax(
    game: Game,
    depth: int,
    alpha: float,
    beta: float,
    static_evaluation_func: Callable[[Game], float],
    maximizing_player: bool,
) -> float:
    """Analyse the current board position according to a static evaluation function and
    a depth.

    Args:
        game (Game): a game.
        depth (int): depth of the search.
        alpha (float): alpha parameter of pruning.
        beta (float): beta parameter of pruning.
        static_evaluation_func (Callable[[Game], float]): position evaluation function.
        maximizing_player (bool): if we want to maximize (for black)
        or minimize (for white)the score of the player.

    Returns:
        float: evaluation score.
    """
    # https://www.youtube.com/watch?v=l-hh51ncgDI
    if depth == 0 or game.is_over:
        return static_evaluation_func(game)

    if maximizing_player:
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

            alpha = max(alpha, child_eval)
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

            beta = min(beta, child_eval)
            if beta <= alpha:
                break

        return min_eval


def think(
    game: Game, depth: int, static_evaluation_func: Callable[[Game], float]
) -> tuple[int, int]:
    """Return the best move to play according to the game position,
    the player turn, a searching depth and a static evaluation method.

    Args:
        game (Game): a game.
        depth (int): depth of the search.
        static_evaluation_func (Callable[[Game], float]): position evaluation function.


    Returns:
        tuple[int, int]: row and column of the best move.
    """
    maximizing_player = game.player_value == BLACK_VALUE
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
                maximizing_player,
            )
        )

    min_index = np.array(scores).argmin()
    max_index = np.array(scores).argmax()

    return (
        cast(tuple[int, int], game.indicators[max_index])
        if maximizing_player
        else cast(tuple[int, int], game.indicators[min_index])
    )
