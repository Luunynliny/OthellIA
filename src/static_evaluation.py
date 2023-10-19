from typing import Type

from game import Game


class StaticEvaluation:
    """Class gathering different methods to evaluate a board position.
    A positive score gives black the advantage.
    A negative score gives white the advantage.
    """

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
