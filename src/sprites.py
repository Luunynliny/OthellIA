import pygame

BOARD_SIZE = 605
CELL_SIZE = 70
CELL_GAP = 5

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
