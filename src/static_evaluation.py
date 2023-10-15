from typing import Type

from game import Game
from settings.cell_values import WHITE_VALUE


class StaticEvaluation:
    """Class gathering different methods to evaluate a board position."""

    def coin_parity(self, game: Type[Game], max_player_value: int) -> float:
        """Evaluate the proportion of a player pieces over the total pieces.

        Args:
            game (Game): a game.
            max_player_value (int): score of the player position.

        Returns:
            float: evaluation score.
        """
        max_player_piece_cnt = game.get_black_piece_count()
        min_player_piece_cnt = game.get_white_piece_count()

        if max_player_value == WHITE_VALUE:
            max_player_piece_cnt, min_player_piece_cnt = (
                min_player_piece_cnt,
                max_player_piece_cnt,
            )

        return (
            100
            * (max_player_piece_cnt - min_player_piece_cnt)
            / (max_player_piece_cnt + min_player_piece_cnt)
        )
