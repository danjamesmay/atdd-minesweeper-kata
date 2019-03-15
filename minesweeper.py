#!/usr/bin/env python

def generate_minefield(minefield_description):
    if minefield_description == "0 0":
        return None

    output = ""
    lines = minefield_description.split("\n")
    field_description = lines[1:]
    for y, line in enumerate(field_description):
        for x, cell in enumerate(line):
            if cell == "*":
                output += "*"
            else:
                output += _mines_in_proximity(x, y, field_description)
                
        output += "\n"
    return output.rstrip()

def _mines_in_proximity(x, y, field_description):
    def mine_to_the_right():
        return x < len(field_description[y]) - 1 and field_description[y][x+1] == "*"
    def mine_to_the_left():
        return x - 1 >= 0 and field_description[y][x-1] == "*"
    mines = 0
    if mine_to_the_left():
        mines += 1
    if mine_to_the_right():
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