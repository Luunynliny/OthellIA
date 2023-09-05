import pygame

from sprites import Board, IndicatorLayout, PhantomPiece, PieceLayout

WIDTH, HEIGHT = (605, 605)
BOARD_COLOR = (77, 77, 77)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Othellia")

    board = Board()
    piece_layout = PieceLayout()
    indicator_layout = IndicatorLayout()
    black_phantom_piece = PhantomPiece(0, 0, is_black=True)
    white_phantom_piece = PhantomPiece(7, 7, is_black=False)

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BOARD_COLOR)
        board.draw(screen)
        piece_layout.draw(screen)
        indicator_layout.draw(screen)
        black_phantom_piece.draw(screen)
        white_phantom_piece.draw(screen)

        pygame.display.flip()

    pygame.quit()
