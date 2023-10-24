import numpy as np

from othellia.game import Game
from othellia.minimax import think
from othellia.static_evaluation import StaticEvaluation
from settings import values
from utils.game import cell_index_to_notation


def play_match(
    chromosome_black: np.ndarray, chromosome_white: np.ndarray, depth: int
) -> tuple[int, str]:
    """Plays an Othello game between two chromosomes and returns the result.

    Args:
        chromosome_black (np.ndarray): a chromosome playing as black.
        chromosome_white (np.ndarray): a chromosome playing as white.
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
                static_evaluation.set_evaluation_weights(chromosome_black)
            case values.WHITE_VALUE:
                static_evaluation.set_evaluation_weights(chromosome_black)

        # Play best legal move
        move = think(game, depth, static_evaluation.evaluate)
        game.play_piece(move)

        # Keep record of the move
        transcript += cell_index_to_notation(move)

    return game.get_winner(), transcript
