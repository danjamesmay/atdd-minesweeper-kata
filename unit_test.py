from minesweeper import generate_minefield

def test_no_minefield_description_outputs_nothing():
    output = generate_minefield("0 0")

    assert output is None

def test_outputs_minefield_for_1x1_minefield_description_with_no_mines():
    output = generate_minefield("""1 1
.""")

    assert output == "0"