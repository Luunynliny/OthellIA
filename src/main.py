import pygame

from game import Game
from settings.cell_values import BLACK_VALUE
from settings.colors import BOARD_COLOR
from settings.graphics import HEIGHT, WIDTH
from sprites import Board, IndicatorLayout, PieceLayout

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("othellia")

    board = Board()
    piece_layout = PieceLayout()
    indicator_layout = IndicatorLayout()

    game = Game()

    running = True
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
                        game.play_piece(
                            cell_index,
                            player_turn_value,
                        )

                        # Next player turn
                        player_turn_value *= -1

                        game.update_surrounding_cells()
                        game.update_sandwiches(player_turn_value)
                        game.update_indicators()

        # Update graphics
        piece_layout.update(game.board)
        indicator_layout.update(game.indicators)

        # Draw graphics
        screen.fill(BOARD_COLOR)

        board.draw(screen)
        piece_layout.draw(screen)
        indicator_layout.draw(screen)

        pygame.display.flip()

    pygame.quit()