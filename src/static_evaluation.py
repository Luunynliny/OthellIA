import numpy as np


class StaticEvaluation:
    """Class gathering different methods to evaluate a board position."""

    def coin_parity(self, board: np.ndarray, max_player_value: int) -> float:
        """Evaluate the proportion of a player pieces over the total pieces.

        Args:
            board (np.ndarray): a board position.
            max_player_value (int): value of the player to max the score of.

        Returns:
            float: evaluation score.
        """
        max_piece_cnt = (board == max_player_value).sum()
        min_piece_cnt = (board == -max_player_value).sum()

        return (
            100
            * (max_piece_cnt - min_piece_cnt)
            / (max_piece_cnt + min_piece_cnt)
        )
