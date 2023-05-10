print("hi there")
from array import *
# Sudoku board represented by a 2d array
# 0 = empty space
Problem = [
[8,5,0,0,2,4,0,0,0],
[7,2,0,0,0,0,0,0,0],
[7,2,0,0,0,0,0,0,0],
[7,2,0,0,0,0,0,0,0],
[7,2,0,0,0,0,0,0,0],
[7,2,0,0,0,0,0,0,0],
[7,2,0,0,0,0,0,0,0],
[7,2,0,0,0,0,0,0,0],
[7,2,0,0,0,0,0,0,0],
]
print("╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗");
for y in range(3):
    for x in range(3):
        s_row_val = (3 * y) + x # Current sudoku row
        row = "║"
        for z in Problem[s_row_val]:
            num = str(z)
            if z == 0:
                num = " "
            row += " " + num + " │"
            #print("║   │   │   ║   │   │   ║   │   │   ║")
        print(row)
        if y == 2 and x == 2:
            print("╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")
        elif x == 2:
            print("╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")
        else:
            print("╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")
