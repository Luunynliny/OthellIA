import pygame

from game import Game
from settings import BLACK_VALUE, BOARD_COLOR, HEIGHT, WHITE_VALUE, WIDTH
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
    is_black_turn = True
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
                            value=BLACK_VALUE
                            if is_black_turn
                            else WHITE_VALUE,
                        )

                        game.remove_indicator(cell_index)

                        # Next player turn
                        is_black_turn = not is_black_turn

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
