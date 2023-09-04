import pygame

WIDTH, HEIGHT = (605, 605)

BOARD_SIZE = 605
CELL_SIZE = 70
CELL_GAP = 5

BOARD_COLOR = (77, 77, 77)
CELL_COLOR = (141, 187, 100)


class Cell(pygame.sprite.Sprite):
    def __init__(self, x, y, corner=None):
        super().__init__()

        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE)).convert_alpha()
        self.image.fill(CELL_COLOR)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Board(pygame.sprite.Group):
    def __init__(self):
        super().__init__()

        self.init_board()

    def init_board(self):
        for y in range(8):
            for x in range(8):
                self.add(
                    Cell(
                        x * CELL_SIZE + (x + 1) * CELL_GAP,
                        y * CELL_SIZE + (y + 1) * CELL_GAP,
                    )
                )


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
