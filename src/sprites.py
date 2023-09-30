import numpy as np
import pygame

from settings.colors import (
    BLACK_PIECE_COLOR,
    CELL_COLOR,
    INDICATOR_COLOR,
    WHITE_PIECE_COLOR,
)
from settings.graphics import CELL_GAP, CELL_SIZE, INDICATOR_SIZE, PIECE_SIZE


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

    def update(self, cells: np.ndarray):
        """Update the piece layout according the content of all board's cells.

        Args:
            cells (np.ndarray): board's cells.
        """
        self.empty()

        for row in range(8):
            for col in range(8):
                val = cells[row, col]

                # Check empty cell
                if val == 0:
                    continue

                self.add(Piece(col, row, is_black=(val == 1)))


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

    def update(self, indicators: np.ndarray):
        """Update the indicator layout.

        Args:
            indicators (np.ndarray): legal moves.
        """
        self.empty()

        for row, col in indicators:
            self.add(Indicator(row, col))


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
