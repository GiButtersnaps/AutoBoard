
from MotorLogic import StrightLine
import numpy as np

checkers_mappings_game = {   # I for Inferior(Lower) edge of board,  U for upper edge of board, R for right side of baord, L for left side of board
'A0' :(0, -1), 'B0' :(1, -1), 'C0' :(2, -1), 'D0' :(3, -1), 'E0' :(4, -1), 'F0' :(5, -1), 'G0' :(6, -1), 'H0' :(7, -1), 
'A1' : (0, 0), 'B1' : (1,0), 'C1' : (2,0), 'D1' : (3,0), 'E1' : (4, 0), 'F1' : (5, 0), 'G1' : (6, 0), 'H1' : (7,0), 
'A2' : (0, 1), 'B2' : (1,1), 'C2' : (2,1), 'D2' : (3,1), 'E2' : (4, 1), 'F2' : (5, 1), 'G2' : (6, 1), 'H2' : (7,1), 
'A3' : (0, 2), 'B3' : (1,2), 'C3' : (2,2), 'D3' : (3,2), 'E3' : (4, 2), 'F3' : (5, 2), 'G3' : (6, 2), 'H3' : (7,2), 
'A4' : (0, 3), 'B4' : (1,3), 'C4' : (2,3), 'D4' : (3,3), 'E4' : (4, 3), 'F4' : (5, 3), 'G4' : (6, 3), 'H4' : (7,3), 
'A5' : (0, 4), 'B5' : (1,4), 'C5' : (2,4), 'D5' : (3,4), 'E5' : (4, 4), 'F5' : (5, 4), 'G5' : (6, 4), 'H5' : (7,4), 
'A6' : (0, 5), 'B6' : (1,5), 'C6' : (2,5), 'D6' : (3,5), 'E6' : (4, 5), 'F6' : (5, 5), 'G6' : (6, 5), 'H6' : (7,5), 
'A7' : (0, 6), 'B7' : (1,6), 'C7' : (2,6), 'D7' : (3,6), 'E7' : (4, 6), 'F7' : (5, 6), 'G7' : (6, 6), 'H7' : (7,6), 
'A8' : (0, 7), 'B8' : (1,7), 'C8' : (2,7), 'D8' : (3,7), 'E8' : (4, 7), 'F8' : (5, 7), 'G8' : (6, 7), 'H8' : (7,7), 
'A9' : (0, 8), 'B9' : (1,8), 'C9' : (2,8), 'D9' : (3,8), 'E9' : (4, 8), 'F9' : (5, 8), 'G9' : (6, 8), 'H9' : (7,8)
}

boardlayout_start = [[' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
                ['x',' ', 'x', ' ', 'x', ' ', 'x', ' '],
                [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['o',' ', 'o', ' ', 'o', ' ', 'o', ' '],
                [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
                ['o',' ', 'o', ' ', 'o', ' ', 'o', ' ']]

boardlayout_current = [[' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
                ['x',' ', 'x', ' ', 'x', ' ', 'x', ' '],
                [' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                [' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],
                ['o',' ', 'o', ' ', 'o', ' ', 'o', ' '],
                [' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],
                ['o',' ', 'o', ' ', 'o', ' ', 'o', ' ']]

previousmove = []

magnet_location = "A1"


def get_key(val):
    for key, value in checkers_mappings_game.items():
        if val == value:
            return key



def findInbetween(start, end):
    #check forward x axis
    if (end[0] - start[0]) ==2:
        # if forward y axis
        if (end[1]- start[1]) == 2:
            return (start[0] + 1, start[1] +1)
        #if backward y axis
        elif (end[1]- start[1]) == -2:
            return (start[0] + 1, start[1] -1)
    #check backward x axis
    if (end[0] - start[0]) == -2:
        #if backward y axis
        if (end[1]- start[1]) == -2:
            return (start[0] - 1, start[1] -1)
        #if forward y axis
        elif (end[1]- start[1]) == 2:
            return (start[0] - 1, start[1] +1)


# location is game mapping not board (2,2)
def findpathstright(location):
    for i in range(location[0]):
        if boardlayout_current[i][location[1]] == 'x' or boardlayout_current[i][location[1]] == 'o':
            break
        else:
            return (-1, location[1])  # might have to change this 
    for j in range(location[0], 8):
        if boardlayout_current[j][location[1]] == 'x' or boardlayout_current[j][location[1]] == 'o':
            break
        else:
            return (8, location[1])  # might have to change this 
    for k in range(location[1]):
        if boardlayout_current[location[0]][k] == 'x' or boardlayout_current[location[0]][k] == 'x':  
            break
        else:
            return (location[0], -1)  # might have to change this 
    for l in range(location[1], 7):
        if boardlayout_current[0][location[l]] == 'x' or boardlayout_current[0][location[l]] == 'o':
            break
        else:
            return (location[0], 8)  # might have to change this 
#returns ( 0,7) or somthing which is x,y of a outer edge position 


# get piece color
# get starting location of piece
# check if piece of color exists at location
# get ending location 
#if one away check if space is clear
# if two away check if space inpetween has piece of oposite color and ending location free
# in first case make single command to move the piece and change the boardlayout then save that move in previous move 
# in second case make list of commands to move piece to new square, 
# then make list of commands to move jumped piece off of the board save all commands done in previous commands 
# update location of magnet


def changeBoard_checkers(move):
    if move[0] == "move":
        #get piece color
        if move[1] == "black":
            color = 0
        else:
            color = 1
        #get start location
        if move[2] not in checkers_mappings_game:
            return "invalid command"
        start = checkers_mappings_game[move[2]]
        #get end location
        if move[4] not in checkers_mappings_game:
            return "invalid command"
        else:
            end = checkers_mappings_game[move[4]]
        #if single space jump
        if (end[0] - start[0]) == 1 or (end[0] - start[0]) == -1:
            if (end[1] - start[1]) == 1 or (end[1] - start[1]) == -1:
                #if spot is empty
                if boardlayout_current[end[0]][end[1]] == ' ':
                    #make move, update current location, update board 
                    #we want 'A1' not (0,0)
                    StrightLine(move[2], move[4], magnet_location, 'checkers')

                    magnet_location = end
                    boardlayout_current[start[0]][start[1]] = ' '
                    if color == 0:
                        boardlayout_current[end[0]][end[1]] = 'o'
                    else:
                        boardlayout_current[end[0]][end[1]] = 'x'
                    previousmove.clear()
                    previousmove.append(start)
                    previousmove.append(end)
            else:
                return "invalid command"
        # if double jump 
        elif (end[0] - start[0]) == 2 or (end[0] - start[0]) == -2:
            if (end[1] - start[1]) == 2 or (end[1] - start[1]) == -2:
                if boardlayout[end[0]][end[1]] == ' ':
                    where = findInbetween(start, end)
                    OffBoard = findpathstright(where)

                    StrightLine(get_key(where),  get_key(OffBoard), magnet_location, 'checkers') #check this kevin
                    StrightLine(move[2], move[4], get_key(OffBoard), 'checkers')  
                    
                    magnet_location = end
                    boardlayout_current[start[0]][start[1]] = ' '
                    boardlayout_current[where[0]][where[1]] = ' '

                    if color == 0:
                        boardlayout_current[end[0]][end[1]] = 'o'
                    else:
                        boardlayout_current[end[0]][end[1]] = 'x'
                    previousmove.clear()
                    previousmove.append(get_key(where))
                    previousmove.append(get_key(OffBoard))
                    previousmove.append(move[2])
                    previousmove.append(move[4])
            else:
                return "invalid command"
        
    elif move[0] == "start":
        boardlayout_current = boardlayout_start    # this is probably wrong


    elif move[0] == "undo":
        if move[1] == "move":
            if len(previousmove) == 4:
                StrightLine( previousmove[3], previousmove[2], magnet_location, 'checkers')
                StrightLine( previousmove[1], previousmove[0], magnet_location, 'checkers')
            elif len(previousmove) ==2:
                StrightLine(previousmove[1], previousmove[0], magnet_location, 'checkers')
        else:
            return "invalid command"

    else:
        return "invalid command"
