#!/usr/bin/env python

def generate_minefield(minefield_description):
    if minefield_description == "0 0":
        return None

    output = ""
    for i in minefield_description.split("\n")[1]:
        if i == "*":
            output += "* "
        else:
            output += "0 "
    return output.rstrip()


print("""Field #1:
*100
2210
1*10
1110

Field #2:
**100
33200
1*100""")