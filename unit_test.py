from minesweeper import generate_minefield
import pytest


def test_empty_minefield_description_outputs_nothing():
    output = generate_minefield("0 0")

    assert output is None

@pytest.mark.parametrize("minefield_description,expected_minefield", [
    ("""1 1
.""", "0"),
    ("""1 2
..""", "00"),
    ("""2 1
.
.""", """0
0"""),
    ("""3 1
.
.
.""", """0
0
0"""),
    ("""2 2
..
..""","""00
00""")
])
def test_outputs_minefield_for_n_by_m_minefield_description_with_no_mines(
    minefield_description,
    expected_minefield):
    assert generate_minefield(minefield_description) == expected_minefield


def test_outputs_minefield_for_1x1_minefield_description_with_one_mine():
    output = generate_minefield("""1 1
*""")

    assert output == "*"