from array import *
# Sudoku board represented by a 2d array
# 0 = empty space
Problem = [
[3,0,6,5,0,8,4,0,0],
[5,2,0,0,0,0,0,0,0],
[0,8,7,0,0,0,0,3,1],
[0,0,3,0,1,0,0,8,0],
[9,0,0,8,6,3,0,0,5],
[0,5,0,0,9,0,6,0,0],
[1,3,0,0,0,0,2,5,0],
[0,0,0,0,0,0,0,7,4],
[0,0,5,2,0,6,3,0,0],
]



def main():
    print("SUDOKU")
    print("Press 1 to start")
    while True:
        gamemode = input()
        try:
            gamemode = int(gamemode)
           # gamemode = 1
        except:
            print("Invalid input")
            continue
        if gamemode != 1:
            print("Invalid number")
            continue
        break

    printSudokuTable()

def printSudokuTable():
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