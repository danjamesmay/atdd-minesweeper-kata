#!/usr/bin/env python

def generate_minefield(minefield_description):
    if minefield_description == "0 0":
        return None

    output = ""
    lines = minefield_description.rstrip().split("\n")
    field_description = lines[1:]
    for row, _ in enumerate(field_description):
        for column, _ in enumerate(field_description[row]):
            if field_description[row][column] == "*":
                output += "*"
            else:
                output += _count_of_mines_in_proximity(column, row, field_description)
                
        output += "\n"
    return output.rstrip()

def _count_of_mines_in_proximity(column, row, field_description):
    def mine_to_the_right():
        return no_more_mines_to_the_right() and field_description[row][column+1] == "*"    
    def mine_to_the_left():
        return no_more_mines_to_left() and field_description[row][column-1] == "*"
    
    def mine_to_the_top():
        return no_more_mines_above() and field_description[row-1][column] == "*"
    def mine_to_the_bottom():
        return no_more_mines_below() and field_description[row+1][column] == "*"
    def mine_to_the_bottom_right():
        return no_more_mines_below() and no_more_mines_to_the_right() and field_description[row+1][column+1] == "*"
    def mine_to_the_top_left():
        return no_more_mines_above() and no_more_mines_to_left() and field_description[row-1][column-1] == "*"
    def mine_to_the_top_right():
        return no_more_mines_above() and no_more_mines_to_the_right() and field_description[row-1][column+1] == "*"

    def no_more_mines_to_left():
        return column - 1 >= 0
    def no_more_mines_to_the_right():
        return column < len(field_description[row]) - 1
    def no_more_mines_above():
        return row != 0
    def no_more_mines_below():
        return row < len(field_description) - 1

    mines = 0
    if mine_to_the_left():
        mines += 1
    if mine_to_the_right():
        mines += 1
    if mine_to_the_top():
        mines += 1
    if mine_to_the_bottom():
        mines += 1
    if mine_to_the_bottom_right():
        mines += 1
    if mine_to_the_top_left():
        mines += 1
    if mine_to_the_top_right():
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