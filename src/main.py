import pygame

from game import Game
from sprites import Board, PieceLayout

WIDTH, HEIGHT = (605, 605)
BOARD_COLOR = (77, 77, 77)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("othellia")

    board = Board()
    piece_layout = PieceLayout()

    game = Game(WIDTH, HEIGHT)

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
                    game.play_piece(cell_index, is_black=is_black_turn)

                    # Next player turn
                    is_black_turn = not is_black_turn

        # Update graphics
        piece_layout.update(game.board)

        # Draw graphics
        screen.fill(BOARD_COLOR)

        board.draw(screen)
        piece_layout.draw(screen)

        pygame.display.flip()

    pygame.quit()
