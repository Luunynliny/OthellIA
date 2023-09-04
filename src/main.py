import pygame

from sprites import Board

WIDTH, HEIGHT = (605, 605)
BOARD_COLOR = (77, 77, 77)

if __name__ == "__main__":
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Othellia")

    board = Board()

    running = True
    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        screen.fill(BOARD_COLOR)
        board.draw(screen)

        pygame.display.flip()

    pygame.quit()
