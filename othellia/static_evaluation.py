from typing import Type

import numpy as np

from othellia.game import Game
from settings.values import BLACK_VALUE, WHITE_VALUE


class StaticEvaluation:
    """Class gathering several static evaluation method to analyse an Othello position.

    A positive score gives black the advantage.
    A negative score gives white the advantage.
    """

    # https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf

    # Default weights as placeholders
    evaluation_weights: tuple[float, float, float, float, float, float] = (
        0.3,
        0.15,
        0.15,
        0.1,
        0.1,
        0.2,
    )

    @staticmethod
    def coin_parity(game: Type[Game]) -> float:
        """Evaluate the proportion of a black and white pieces over the total pieces.

        Args:
            game (Game): a game.

        Returns:
            float: evaluation score.
        """
        black_piece_cnt = game.get_black_piece_count()
        white_piece_cnt = game.get_white_piece_count()

        return (
            100
            * (black_piece_cnt - white_piece_cnt)
            / (black_piece_cnt + white_piece_cnt)
        )

    @staticmethod
    def actual_mobility(game: Type[Game]) -> float:
        """Compare the number of black's legal moves over white's ones.

        Args:
            game (Game): a game.

        Returns:
            float: evaluation score.
        """
        black_actual_mobility = game.get_black_legal_moves_count()
        white_actual_mobility = game.get_white_legal_moves_count()

        if black_actual_mobility + white_actual_mobility == 0:
            return 0

        return (
            100
            * (black_actual_mobility - white_actual_mobility)
            / (black_actual_mobility + white_actual_mobility)
        )

    @staticmethod
    def potential_mobility(game: Type[Game]) -> float:
        """Compare the number of empty cells next to white pieces over black pieces.

        Args:
            game (Game): a game.

        Returns:
            float: evaluation score.
        """
        black_potential_mobility = game.get_white_empty_neighbors_count()
        white_potential_mobility = game.get_black_empty_neighbors_count()

        if black_potential_mobility + white_potential_mobility == 0:
            return 0

        return (
            100
            * (black_potential_mobility - white_potential_mobility)
            / (black_potential_mobility + white_potential_mobility)
        )

    @staticmethod
    def corners_captured(game: Type[Game]) -> float:
        """Compare the number of captured corners of black against white.

        Args:
            game (Game): a game.

        Returns:
            float: evaluation score.
        """
        corners = np.array(
            [
                game.board[0, 0],
                game.board[7, 0],
                game.board[0, 7],
                game.board[7, 7],
            ]
        )

        black_corner_cnt = (corners == BLACK_VALUE).sum()
        white_corner_cnt = (corners == WHITE_VALUE).sum()

        if black_corner_cnt + white_corner_cnt == 0:
            return 0

        return (
            100
            * (black_corner_cnt - white_corner_cnt)
            / (black_corner_cnt + white_corner_cnt)
        )

    @staticmethod
    def future_corners_captured(game: Type[Game]) -> float:
        """Compare the number of possible corners to be captured by black against white.

        Args:
            game (Game): a game.

        Returns:
            float: evaluation score.
        """
        corners = [(0, 0), (0, 7), (7, 0), (7, 7)]

        black_legal_moves = game.get_black_legal_moves()
        white_legal_moves = game.get_white_legal_moves()

        black_future_corner_cnt = (
            0
            if len(black_legal_moves) == 0
            else np.all(np.isin(black_legal_moves, corners), axis=1).sum()
        )
        white_future_corner_cnt = (
            0
            if len(white_legal_moves) == 0
            else np.all(
                np.isin(game.get_white_legal_moves(), corners), axis=1
            ).sum()
        )

        if black_future_corner_cnt + white_future_corner_cnt == 0:
            return 0

        return (
            100
            * (black_future_corner_cnt - white_future_corner_cnt)
            / (black_future_corner_cnt + white_future_corner_cnt)
        )

    @staticmethod
    def static_weights(game: Type[Game]) -> float:
        """Compare black pieces weights sum against white.

        Args:
            game (Game): a game.

        Returns:
            float: evaluation score.
        """
        weights = np.array(
            [
                [4, -3, 2, 2, 2, 2, -3, 4],
                [-3, -4, -1, -1, -1, -1, -4, -3],
                [2, -1, 1, 0, 0, 1, -1, 2],
                [2, -1, 0, 1, 1, 0, -1, 2],
                [2, -1, 0, 1, 1, 0, -1, 2],
                [2, -1, 1, 0, 0, 1, -1, 2],
                [-3, -4, -1, -1, -1, -1, -4, -3],
                [4, -3, 2, 2, 2, 2, -3, 4],
            ],
            dtype=int,
        )

        black_weights_sum = 0
        white_weights_sum = 0

        for column, row in game.get_all_black_cells():
            black_weights_sum += weights[row, column]

        for column, row in game.get_all_white_cells():
            white_weights_sum += weights[row, column]

        return black_weights_sum - white_weights_sum

    @staticmethod
    def evaluate(game: Type[Game]) -> float:
        """Return the weighted evaluation of respectively coin_parity,
        actual_mobility, potential_mobility, corners_captured,
        future_corners_captured and static_weights scores.

        Args:
            game (Type[Game]): a game.

        Returns:
            float: evaluation score.
        """
        a, b, c, d, e, f = StaticEvaluation.evaluation_weights

        return (
            a * StaticEvaluation.coin_parity(game)
            + b * StaticEvaluation.actual_mobility(game)
            + c * StaticEvaluation.potential_mobility(game)
            + d * StaticEvaluation.corners_captured(game)
            + e * StaticEvaluation.future_corners_captured(game)
            + f * StaticEvaluation.static_weights(game)
        )

    @staticmethod
    def set_evaluation_weights(
        weights: tuple[float, float, float, float, float, float]
    ):
        """Set the weights for the `evaluate()` function.

        Args:
            weights (tuple[float, float, float, float, float, float]): evaluation
            weights.
        """
        StaticEvaluation.evaluation_weights = weights
