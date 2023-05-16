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

# This is the solution. Check if the board is equal to this.
Solution = [
[3,1,6,5,7,8,4,9,2],
[5,2,9,1,3,4,7,6,8],
[4,8,7,6,2,9,5,3,1],
[2,6,3,4,1,5,9,8,7],
[9,7,4,8,6,3,1,2,5],
[8,5,1,7,9,2,6,4,3],
[1,3,8,9,4,7,2,5,6],
[6,9,2,3,5,1,8,7,4],
[7,4,5,2,8,6,3,1,9],
]

selected = [0,0] # Selected space (x,y)


def main():
    print("TERMINAL SUDOKU")
    print("Press 1 to start")
    while True: # Input validation
        gamemode = input()
        try:
            gamemode = int(gamemode)
        except:
            print("Invalid input")
            continue
        if gamemode != 1:
            print("Invalid number")
            continue
        break
    game()
    exitGame()

def printSudokuTable(Board_Problem):
    print("╔═══╤═══╤═══╦═══╤═══╤═══╦═══╤═══╤═══╗");
    for y in range(3):
        for x in range(3):
            s_row_val = (3 * y) + x # Current sudoku row
            row = "║"
            for z in range(9):
                num = str(Board_Problem[s_row_val][z])
                if Board_Problem[s_row_val][z] == 0:
                    if s_row_val == selected[0] and z == selected[1]:
                        num = "X"
                    else: 
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

def game():
    Game_Board = Problem.copy()
    running = True
    findNearestEmptySpace(Game_Board)
    while running:
        printSudokuTable(Game_Board)
        print(selected)
        print("Press Q to quit")
        print("Press F when finished filling out the sudoku table")
        print("Press u, d, l, r to move to cursor")
        print("Input a # from 1 - 9 to add it to the square")
        choice = input("Your next move: ")
        match choice: # Note: Only works with 3.10+ versions of Python.
            case "Q" :
                running = False
            case "F":
                check(Game_Board)
                running = False
            case "u" :
                search_up = selected[0]
                for y in range(9):
                    search_up -= 1
                    if search_up < 0:
                        search_up += 9
                    print(search_up)
                    if Game_Board[search_up][selected[1]] == 0:
                        selected[0] = search_up
                        break
            case "d" :
                search_down = selected[0]
                for y in range(9):
                    search_down += 1
                    if search_down > 8:
                        search_down -= 9
                    print(search_down)
                    if Game_Board[search_down][selected[1]] == 0:
                        selected[0] = search_down
                        break
            case "l" :
                search_left = selected[1]
                for x in range(9):
                    search_left -= 1
                    if search_left < 0:
                        search_left += 9
                    print(search_left)
                    if Game_Board[selected[0]][search_left] == 0:
                        selected[1] = search_left
                        break
            case "r" :
                search_right = selected[1]
                for x in range(9):
                   search_right += 1
                   if search_right > 8:
                       search_right -= 9
                   print(search_right)
                   if Game_Board[selected[0]][search_right] == 0:
                       selected[1] = search_right
                       break
            case "1" | "2" | "3" | "4" | "5" | "6" | "7" | "8" | "9" :
                print("inserted a " + str(choice) + " at " + str(selected))
                Game_Board[selected[0]][selected[1]] = int(choice)
                search_row = selected[0]
                search_col = selected[1]
                free_space_found = False
                findNearestEmptySpace(Game_Board)
            case _ :
                print("Invalid")

def findNearestEmptySpace(Board):
    search_row = selected[0]
    search_col = selected[1]
    free_space_found = False
    for x in range(9):
        for y in range(9):
            search_col += 1
            if search_col > 8:
                search_col -= 9
            if Board[search_row][search_col] == 0:
                selected[1] = search_col
                selected[0] = search_row
                free_space_found = True
                break
        if free_space_found:
            break
        search_row += 1
        if search_row > 8:
            search_row -= 9
            
            
            
def check(player_board):
    if check_for0(player_board) == True:
        a1 = [
            [3,1,6,5,7,8,4,9,2],
            [5,2,9,1,3,4,7,6,8],
            [4,8,7,6,2,9,5,3,1],
            [2,6,3,4,1,5,9,8,7],
            [9,7,4,8,6,3,1,2,5],
            [8,5,1,7,9,2,6,4,3],
            [1,3,8,9,4,7,2,5,6],
            [6,9,2,3,5,1,8,7,4],
            [7,4,5,2,8,6,3,1,9],
            ]
    
        for i, row in enumerate(player_board):
            #dup = duplicates
            dup = ifdup(row)
            if dup:
                print(f"Duplicate values at row {i+1}  at position:{dup}")
    
        for i, row in enumerate(player_board):    
            dup = ifdup(getColumn(player_board, i))
            if dup:
                print(f"Duplicate values at column {dup[1]}  at position:{dup}")
                
        if player_board == a1:
            print("correct answer")
        elif player_board != a1:
            print("wrong answer")
    elif checkfor0(playerboard) == False:
        print("not complete")

#check if any duplicates within an array
def ifdup(array):
    #create dictionary exist
    exist = {}
    #duplicate list to store positions
    dup = []
    for i, num in enumerate(array):
        #set !=0 since our placeholders are 0
        if num !=0:
            #if the number exists in the dictionary append to duplicate list with its positions
            if num in exist:
                dup.append(i)
                dup.append(exist[num])
            else:
                exist[num] = i
    return dup
#check if there are any empty spaces

def getColumn(player_board, columnNum):
    column = []
    for row in player_board:
        column.append(row[columnNum])
    return column

def check_for0(Board):
    for row in Board:
        if 0 in row:
            print("not complete")
            return False
    print("complete")
    return True
              

def exitGame():
    print("Game Over! Thanks for playing!")
    quit()
    
main()
