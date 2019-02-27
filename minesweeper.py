#!/usr/bin/env python

def generate_minefield(minefield_description):
    if minefield_description == "0 0":
        return None

    output = ""
    lines = minefield_description.split("\n")
    for line in lines[1:]:
        for i in line:
            if i == "*":
                output += "*"
            else:
                output += "0"
        output += "\n"
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