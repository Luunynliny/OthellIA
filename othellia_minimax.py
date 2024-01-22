import pygame

from othellia.game import Game, mouse_pos_to_cell_index
from othellia.minimax import think
from othellia.sprites import (
    Board,
    EndgameMessage,
    IndicatorLayout,
    PieceLayout,
)
from othellia.static_evaluation import StaticEvaluation
from settings import values
from settings.colors import BOARD_COLOR
from settings.graphics import HEIGHT, WIDTH

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("othellia")

    board = Board()
    piece_layout = PieceLayout()
    indicator_layout = IndicatorLayout()

    endgame_message_black_won = EndgameMessage(values.BLACK_VALUE)
    endgame_message_white_won = EndgameMessage(values.WHITE_VALUE)
    endgame_message_draw = EndgameMessage(None)

    game = Game()
    static_evaluation = StaticEvaluation()

    # Set genetic evaluation weights
    static_evaluation.load_evaluation_weights()

    running = True
    is_game_over = False

    while running:
        if not game.is_over:
            match game.player_value:
                case values.BLACK_VALUE:
                    for event in pygame.event.get():
                        if event.type == pygame.QUIT:
                            running = False

                        if event.type == pygame.MOUSEBUTTONDOWN:
                            cell_index = mouse_pos_to_cell_index(
                                pygame.mouse.get_pos()
                            )

                            # Check if a piece can be played
                            if game.is_cell_empty(cell_index):
                                # Check if the move is legal
                                if game.is_move_legal(cell_index):
                                    game.play_piece(cell_index)
                case values.WHITE_VALUE:
                    # Find the best legal move
                    best_move = think(
                        game,
                        depth=2,
                        static_evaluation_func=static_evaluation.evaluate,
                    )
                    game.play_piece(best_move)

        # Update graphics
        piece_layout.update(game.board)
        indicator_layout.update(game.indicators)

        # Draw graphics
        screen.fill(BOARD_COLOR)

        board.draw(screen)
        piece_layout.draw(screen)

        # Hide indicators while white is thinking
        if game.player_value == values.BLACK_VALUE:
            indicator_layout.draw(screen)

        if game.is_over:
            match game.get_winner():
                case values.BLACK_VALUE:
                    endgame_message_black_won.draw(screen)
                case values.WHITE_VALUE:
                    endgame_message_white_won.draw(screen)
                case _:
                    endgame_message_draw.draw(screen)

        pygame.display.flip()

    pygame.quit()
