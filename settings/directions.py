UP: tuple[int, int] = (0, -1)
DOWN: tuple[int, int] = (0, 1)
LEFT: tuple[int, int] = (-1, 0)
RIGHT: tuple[int, int] = (1, 0)

UP_LEFT: tuple[int, int] = (-1, -1)
UP_RIGHT: tuple[int, int] = (1, -1)
DOWN_LEFT: tuple[int, int] = (-1, 1)
DOWN_RIGHT: tuple[int, int] = (1, 1)

DIRECTIONS: tuple[
    tuple[int, int],
    tuple[int, int],
    tuple[int, int],
    tuple[int, int],
    tuple[int, int],
    tuple[int, int],
    tuple[int, int],
    tuple[int, int],
] = (UP, DOWN, LEFT, RIGHT, UP_LEFT, UP_RIGHT, DOWN_LEFT, DOWN_RIGHT)
