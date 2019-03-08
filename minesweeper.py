#!/usr/bin/env python

def generate_minefield(minefield_description):
    if minefield_description == "0 0":
        return None

    output = ""
    lines = minefield_description.split("\n")
    for line in lines[1:]:
        for i, cell in enumerate(line):
            if cell == "*":
                output += "*"
            else:
                output += _mines_in_proximity(i, line)
                
        output += "\n"
    return output.rstrip()

def _mines_in_proximity(i, line):
    def mine_to_the_left(i, line):
        return i < len(line) - 1 and line[i+1] == "*"
    def mine_to_the_right(i, line):
        return i - 1 >= 0 and line[i-1] == "*"
    mines = 0
    if mine_to_the_left(i, line):
        mines += 1
    if mine_to_the_right(i, line):
        mines += 1
    return str(mines)


print("""Field #1:
*100
2210
1*10
1110

Field #2:
**100
33200
1*100""")