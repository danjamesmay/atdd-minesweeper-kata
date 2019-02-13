import subprocess
import textwrap

def test_counts_adjacent_mines():
    minefield_description = """4 4
*...
....
.*..
....
3 5
**...
.....
.*...
0 0"""

    output = subprocess.run(
        ["./minesweeper.py"],
        input=minefield_description,
        encoding='ascii',
        check=True,
        stdout=subprocess.PIPE).stdout

    expected = """Field #1:
*100
2210
1*10
1110

Field #2:
**100
33200
1*100\n"""
    assert expected == output