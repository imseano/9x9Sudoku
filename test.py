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



def main():
    print("Hello World")
    printSudoku()

def printSudoku():
    print("╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗");
    for y in range(3):
        for x in range(3):
            s_row_val = (3 * y) + x # Current sudoku row
            row = "║"
            for z in range(9):
                num = str(Problem[s_row_val][z])
                if Problem[s_row_val][z] == 0:
                    num = " "
                row += " " + num + " "
                if (z + 1) % 3 == 0:
                    row += "║"  
                else:
                    row += "│"
                #print("║   │   │   ║   │   │   ║   │   │   ║")
            print(row)
            if y == 2 and x == 2:
                print("╚═══╧═══╧═══╩═══╧═══╧═══╩═══╧═══╧═══╝")
            elif x == 2:
                print("╠═══╪═══╪═══╬═══╪═══╪═══╬═══╪═══╪═══╣")
            else:
                print("╟───┼───┼───╫───┼───┼───╫───┼───┼───╢")
    
main()