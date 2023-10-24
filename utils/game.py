def notation_to_cell_index(cell_notation: str) -> tuple[int, int]:
    """Convert a cell game notation into the corresponding row and column index.

    Args:
        cell_notation (str): game notation of the cell.

    Returns:
        tuple[int, int]: row and column of the cell.
    """
    row, col = list(cell_notation)

    return (ord(row) - 97, int(col) - 1)


def cell_index_to_notation(cell_index: tuple[int, int]) -> str:
    """Convert a cell row and column index into game notation.

    Args:
        cell_index (tuple[int, int]): row and column of the cell

    Returns:
        str: game notation of the cell.
    """
    row, col = cell_index

    return f"{chr(97 + row)}{col  + 1}"
