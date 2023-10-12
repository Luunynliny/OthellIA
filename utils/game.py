def notation_to_cell_index(cell_notation: str) -> tuple[int, int]:
    """Convert a cell game notation into the corresponding row and column index.

    Args:
        cell_notation (str): game notation of the cell.

    Returns:
        tuple[int, int]: row and column of the cell.
    """
    row, col = list(cell_notation)

    return (ord(row) - 97, int(col) - 1)
