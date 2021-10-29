
checkers_mappings = {
    'A1' : (0, 0), 'B1' : (969,323), 'C1' : (1615,323), 'D1' : (2261,323), 'E1' : (2907, 323), 'F1' : (3553, 323), 'G1' : (4199, 323), 'H1' : (4845,323), 
    'A2' : (0, 1), 'B2' : (969,969), 'C2' : (1615,969), 'D2' : (2261,969), 'E2' : (2907, 969), 'F2' : (3553, 969), 'G2' : (4199, 969), 'H2' : (4845,969),
    'A3' : (0, 2), 'B3' : (969,1615), 'C3' : (1615,1615), 'D3' : (2261,1615), 'E3' : (2907, 1615), 'F3' : (3553, 1615), 'G3' : (4199, 1615), 'H3' : (4845,1615),
    'A4' : (0, 3), 'B4' : (969,2261), 'C4' : (1615,2261), 'D4' : (2261,2261), 'E4' : (2907, 2261), 'F4' : (3553, 2261), 'G4' : (4199, 2261), 'H4' : (4845,2261),
    'A5' : (0, 4), 'B5' : (969,2907), 'C5' : (1615,2907), 'D5' : (2261,2907), 'E5' : (2907, 2907), 'F5' : (3553, 2907), 'G5' : (4199, 2907), 'H5' : (4845,2907),
    'A6' : (0, 5), 'B6' : (969,3553), 'C6' : (1615,3553), 'D6' : (2261,3553), 'E6' : (2907, 3553), 'F6' : (3553, 3553), 'G6' : (4199, 3553), 'H6' : (4845,3553),
    'A7' : (0, 6), 'B7' : (969,4199), 'C7' : (1615,4199), 'D7' : (2261,4199), 'E7' : (2907, 4199), 'F7' : (3553, 4199), 'G7' : (4199, 4199), 'H7' : (4845,4199),
    'A8' : (0, 7), 'B8' : (969,4845), 'C8' : (1615,4845), 'D8' : (2261,4845), 'E8' : (2907, 4845), 'F8' : (3553, 4845), 'G8' : (4199, 4845), 'H8' : (4845,4845)
}

boardlayout = [[' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],['x',' ', 'x', ' ', 'x', ' ', 'x', ' '],[' ', 'x', ' ', 'x', ' ', 'x', ' ', 'x'],[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],[' ', ' ', ' ', ' ', ' ', ' ', ' ', ' '],['o',' ', 'o', ' ', 'o', ' ', 'o', ' '],[' ', 'o', ' ', 'o', ' ', 'o', ' ', 'o'],['o',' ', 'o', ' ', 'o', ' ', 'o', ' ']]

previousmove = []

magnet_location = "A1"



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


def changeBoard(move):
    if move[0] == "move":
        if move[1] == "black":
            color = 0
        else:
            color = 1
        if move[2] not in checkers_mappings:
            return "invalid command"
        start = checkers_mappings(move[2])


        


        

    elif move[0] == "start":
        
    elif move[0] == "undo":
        
    elif move[0] == "spin":
        if move[1] == "the":
            if move[2] == "wheel":
                
            else:
                return "invalid command"
        else:
            return "invalid command"

    else:
        return "invalid command"
