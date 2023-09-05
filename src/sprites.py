import pygame

BOARD_SIZE = 605
CELL_SIZE = 70
CELL_GAP = 5
PIECE_SIZE = 60
INDICATOR_SIZE = 25

CELL_COLOR = (141, 187, 100)
BLACK_PIECE_COLOR = (47, 54, 64)
WHITE_PIECE_COLOR = (245, 246, 250)
INDICATOR_COLOR = (159, 100, 187)


class Cell(pygame.sprite.Sprite):
    """Sprite of board cell.

    Args:
        x (int): x-axis top-left pixel position.
        y (int): y-axis top-left pixel position.
    """

    def __init__(self, x, y):
        super().__init__()

        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE))
        self.image.fill(CELL_COLOR)

        self.rect = self.image.get_rect()
        self.rect.topleft = (x, y)

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class Board(pygame.sprite.Group):
    """Sprite group of the board."""

    def __init__(self):
        super().__init__()

        self.init_board()

    def init_board(self):
        """Initiliaze board cells position."""
        for y in range(8):
            for x in range(8):
                self.add(
                    Cell(
                        x * CELL_SIZE + (x + 1) * CELL_GAP,
                        y * CELL_SIZE + (y + 1) * CELL_GAP,
                    )
                )


class Piece(pygame.sprite.Sprite):
    """Sprite of a piece.

    A piece can be black or white, depending on which player it belongs to.

    Args:
        row (int): row position on the board.
        col (int): column position on the board.
        is_black (bool): color of the piece.
    """

    def __init__(self, row, col, is_black):
        super().__init__()

        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(
            self.image,
            color=BLACK_PIECE_COLOR if is_black else WHITE_PIECE_COLOR,
            center=(
                CELL_SIZE / 2,
                CELL_SIZE / 2,
            ),
            radius=PIECE_SIZE / 2,
            width=0,  # Fill the circle
        )

        self.rect = self.image.get_rect()
        self.rect.topleft = (
            row * CELL_SIZE + (row + 1) * CELL_GAP,
            col * CELL_SIZE + (col + 1) * CELL_GAP,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class PieceLayout(pygame.sprite.Group):
    """Sprite group of all the pieces on the board."""

    def __init__(self):
        super().__init__()

        self.init_layout()

    def init_layout(self):
        """Initiliaze starting piece layout."""
        self.add(
            Piece(3, 3, is_black=False),
            Piece(3, 4, is_black=True),
            Piece(4, 3, is_black=True),
            Piece(4, 4, is_black=False),
        )


class Indicator(pygame.sprite.Sprite):
    """Sprite of a move indicator.

    Only certain moves are legal on each player's turn, notified by indicators
    for more convenience.

    Args:
        row (int): row position on the board.
        col (int): column position on the board.
    """

    def __init__(self, row, col):
        super().__init__()

        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        # self.image.fill((255, 0, 0))
        pygame.draw.circle(
            self.image,
            color=INDICATOR_COLOR,
            center=(
                CELL_SIZE / 2,
                CELL_SIZE / 2,
            ),
            radius=INDICATOR_SIZE / 2,
            width=0,  # Fill the circle
        )

        self.rect = self.image.get_rect()
        self.rect.topleft = (
            row * CELL_SIZE + (row + 1) * CELL_GAP,
            col * CELL_SIZE + (col + 1) * CELL_GAP,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)


class IndicatorLayout(pygame.sprite.Group):
    """Sprite group of all move indicators."""

    def __init__(self):
        super().__init__()

        self.init_layout()

    def init_layout(self):
        """Initiliaze starting indicator layout."""
        self.add(
            Indicator(2, 3),
            Indicator(3, 2),
            Indicator(4, 5),
            Indicator(5, 4),
        )


class PhantomPiece(pygame.sprite.Sprite):
    """Sprite of a phantom piece.

    A phantom piece is used to help the player visualize his next move by
    replacing an indicator with a semi-transparent version of his piece.

    Args:
        row (_type_): row position on the board.
        col (_type_): color position on the board.
        is_black (bool): color of the piece.
    """

    def __init__(self, row, col, is_black):
        super().__init__()

        self.image = pygame.Surface((CELL_SIZE, CELL_SIZE), pygame.SRCALPHA)
        pygame.draw.circle(
            self.image,
            color=(*BLACK_PIECE_COLOR, 255 / 2)
            if is_black
            else (*WHITE_PIECE_COLOR, 255 / 2),
            center=(
                CELL_SIZE / 2,
                CELL_SIZE / 2,
            ),
            radius=PIECE_SIZE / 2,
            width=0,  # Fill the circle
        )

        self.rect = self.image.get_rect()
        self.rect.topleft = (
            row * CELL_SIZE + (row + 1) * CELL_GAP,
            col * CELL_SIZE + (col + 1) * CELL_GAP,
        )

    def draw(self, surface):
        surface.blit(self.image, self.rect)
