from utils.game import notation_to_cell_index


def test_notation_to_cell_index():
    assert notation_to_cell_index("a1") == (0, 0)
    assert notation_to_cell_index("a8") == (0, 7)
    assert notation_to_cell_index("h1") == (7, 0)
    assert notation_to_cell_index("h8") == (7, 7)
    assert notation_to_cell_index("d4") == (3, 3)
    assert notation_to_cell_index("g2") == (6, 1)
