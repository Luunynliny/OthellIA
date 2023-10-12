import pygame

from settings import cell_values
from settings.cell_values import BLACK_VALUE, WHITE_VALUE
from settings.colors import BOARD_COLOR
from settings.graphics import HEIGHT, WIDTH
from src.game import Game
from src.sprites import Board, EndgameMessage, IndicatorLayout, PieceLayout

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("othellia")

    board = Board()
    piece_layout = PieceLayout()
    indicator_layout = IndicatorLayout()

    endgame_message_black_won = EndgameMessage(BLACK_VALUE)
    endgame_message_white_won = EndgameMessage(WHITE_VALUE)
    endgame_message_draw = EndgameMessage(None)

    game = Game()

    running = True
    is_game_over = False
    player_turn_value = BLACK_VALUE

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                cell_index = game.mouse_pos_to_cell_index(
                    pygame.mouse.get_pos()
                )

                # Check if a piece can be played
                if game.is_cell_empty(cell_index):
                    # Check if the move is legal
                    if game.is_move_legal(cell_index):
                        game.play_piece(cell_index)

        # Update graphics
        piece_layout.update(game.board)
        indicator_layout.update(game.indicators)

        # Draw graphics
        screen.fill(BOARD_COLOR)

        board.draw(screen)
        piece_layout.draw(screen)
        indicator_layout.draw(screen)

        if game.is_over:
            match game.get_winner():
                case cell_values.BLACK_VALUE:
                    endgame_message_black_won.draw(screen)
                case cell_values.WHITE_VALUE:
                    endgame_message_white_won.draw(screen)
                case _:
                    endgame_message_draw.draw(screen)

        pygame.display.flip()

    pygame.quit()
