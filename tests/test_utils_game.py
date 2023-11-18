from utils.game import cell_index_to_notation, notation_to_cell_index


def test_notation_to_cell_index():
    assert notation_to_cell_index("a1") == (0, 0)
    assert notation_to_cell_index("a8") == (0, 7)
    assert notation_to_cell_index("h1") == (7, 0)
    assert notation_to_cell_index("h8") == (7, 7)
    assert notation_to_cell_index("d4") == (3, 3)
    assert notation_to_cell_index("g2") == (6, 1)


def test_cell_index_to_notation():
    assert cell_index_to_notation((0, 0)) == ("a1")
    assert cell_index_to_notation((0, 7)) == ("a8")
    assert cell_index_to_notation((7, 0)) == ("h1")
    assert cell_index_to_notation((7, 7)) == ("h8")
    assert cell_index_to_notation((3, 3)) == ("d4")
    assert cell_index_to_notation((6, 1)) == ("g2")
