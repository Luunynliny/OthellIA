from typing import Type

from game import Game


class StaticEvaluation:
    """Class gathering different methods to evaluate a board position.
    A positive score gives black the advantage.
    A negative score gives white the advantage.
    """

    # https://courses.cs.washington.edu/courses/cse573/04au/Project/mini1/RUSSIA/Final_Paper.pdf

    def coin_parity(self, game: Type[Game]) -> float:
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

    def actual_mobility(self, game: Type[Game]) -> float:
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
