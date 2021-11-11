from os import lchown   # What is this again
import time
import board
import digitalio

# will have to change this for our pcb and put this in main while loop code
stp = digitalio.DigitalInOut(board.D2)
dir = digitalio.DigitalInOut(board.D3)
MS1 = digitalio.DigitalInOut(board.D4)
MS2 = digitalio.DigitalInOut(board.D5)
EN = digitalio.DigitalInOut(board.D6)

MAG = digitalio.DigitalInOut(board.D12)   # problem with dev board we need 5V not 3.3V 

stpY = digitalio.DigitalInOut(board.D7)
dirY = digitalio.DigitalInOut(board.D8)
MS1Y = digitalio.DigitalInOut(board.D9)
MS2Y = digitalio.DigitalInOut(board.D10)
ENY = digitalio.DigitalInOut(board.D11)

stp.direction =  digitalio.Direction.OUTPUT
dir.direction =  digitalio.Direction.OUTPUT
MS1.direction =  digitalio.Direction.OUTPUT
MS2.direction =  digitalio.Direction.OUTPUT
EN.direction = digitalio.Direction.OUTPUT

stpY.direction =  digitalio.Direction.OUTPUT
dirY.direction =  digitalio.Direction.OUTPUT
MS1Y.direction =  digitalio.Direction.OUTPUT
MS2Y.direction =  digitalio.Direction.OUTPUT
ENY.direction = digitalio.Direction.OUTPUT


stp.value = False    # deafult no step
EN.value = True      # default to being off   True = off,   False = on
MS1.value = False    # default to full steps
MS2.value = False 
dir.value = True     # will have to change this. Make default positive direction 
MAG.value = False    #defult magnet off

stpY.value = False    # deafult no step
ENY.value = True      # default to being off   True = off,   False = on
MS1Y.value = False    # default to full steps
MS2Y.value = False 
dirY.value = True     # will have to change this. Make default positive direction 


#Deans work is crap not 5175 per axis more like 1300. Will have to test to get 

checkers_mappings = { # I for Inferior(Lower) edge of board,  U for upper edge of board, R for right side of baord, L for left side of board
'I1' :(323, 0), 'I2' :(969, 0), 'I3' :(1615, 0), 'I4' :(2261, 0), 'I5' :(2907, 0), 'I6' :(3553, 0), 'I7' :(4199, 0), 'I8' :(4845, 0), 
'L1' : (0, 323), 'A1' : (323, 323), 'B1' : (969,323), 'C1' : (1615,323), 'D1' : (2261,323), 'E1' : (2907, 323), 'F1' : (3553, 323), 'G1' : (4199, 323), 'H1' : (4845,323), 'R1' : (5168, 323),
'L1' : (0, 323), 'A2' : (323, 969), 'B2' : (969,969), 'C2' : (1615,969), 'D2' : (2261,969), 'E2' : (2907, 969), 'F2' : (3553, 969), 'G2' : (4199, 969), 'H2' : (4845,969), 'R2' : (5168, 969), 
'L1' : (0, 323), 'A3' : (323, 1615), 'B3' : (969,1615), 'C3' : (1615,1615), 'D3' : (2261,1615), 'E3' : (2907, 1615), 'F3' : (3553, 1615), 'G3' : (4199, 1615), 'H3' : (4845,1615), 'R3' : (5168, 1615), 
'L1' : (0, 323), 'A4' : (323, 2261), 'B4' : (969,2261), 'C4' : (1615,2261), 'D4' : (2261,2261), 'E4' : (2907, 2261), 'F4' : (3553, 2261), 'G4' : (4199, 2261), 'H4' : (4845,2261), 'R4' : (5168, 2261), 
'L1' : (0, 323), 'A5' : (323, 2907), 'B5' : (969,2907), 'C5' : (1615,2907), 'D5' : (2261,2907), 'E5' : (2907, 2907), 'F5' : (3553, 2907), 'G5' : (4199, 2907), 'H5' : (4845,2907), 'R5' : (5168, 2907), 
'L1' : (0, 323), 'A6' : (323, 3553), 'B6' : (969,3553), 'C6' : (1615,3553), 'D6' : (2261,3553), 'E6' : (2907, 3553), 'F6' : (3553, 3553), 'G6' : (4199, 3553), 'H6' : (4845,3553), 'R6' : (5168, 3553), 
'L1' : (0, 323), 'A7' : (323, 4199), 'B7' : (969,4199), 'C7' : (1615,4199), 'D7' : (2261,4199), 'E7' : (2907, 4199), 'F7' : (3553, 4199), 'G7' : (4199, 4199), 'H7' : (4845,4199), 'R7' : (5168, 4199), 
'L1' : (0, 323), 'A8' : (323, 4845), 'B8' : (969,4845), 'C8' : (1615,4845), 'D8' : (2261,4845), 'E8' : (2907, 4845), 'F8' : (3553, 4845), 'G8' : (4199, 4845), 'H8' : (4845,4845), 'R8' : (5168, 4845), 
'U1' : (323, 5168), 'U2' : (969,5168), 'U3' : (1615,5168), 'U4' : (2261,5168), 'U5' : (2907, 5168), 'U6' : (3555, 5168), 'U7' : (4199, 5168), 'U8' : (4845,5168)
}

chutes_mappings = {
'1' : (194,258), '2' : (582,258), '3' : (970,258), '4' : (1358,258), '5' : (1746,258), '6' : (2134,258), '7' : (2522,258), '8' : (2910,258), '9' : (3298,258), '10' : (3686,258),
'20': (194,774), '19': (582,774), '18': (970,774), '17': (1358,774), '16': (1746,774), '15': (2134,774), '14': (2522,774), '13': (2910,774), '12': (3298,774), '11' : (3686,774), 
'21': (194,1290), '22': (582,1290), '23': (970,1290), '24': (1358,1290), '25': (1746,1290), '26': (2134,1290), '27': (2522,1290), '28': (2910,1290), '29': (3298,1290), '30': (3686,1290), 
'40': (194,1806), '39': (582,1806), '38': (970,1806), '37': (1358,1806), '36': (1746,1806), '35': (2134,1806), '34': (2522,1806), '33': (2910,1806), '32': (3298,1806), '31': (3686,1806), 
'41': (194,2322), '42': (582,2322), '43': (970,2322), '44': (1358,2322), '45': (1746,2322), '46': (2134,2322), '47': (2522,2322), '48': (2910,2322), '49': (3298,2322), '50': (3686,2322), 
'60': (194,2838), '59': (582,2838), '58': (970,2838), '57': (1358,2838), '56': (1746,2838), '55': (2134,2838), '54': (2522,2838), '53': (2910,2838), '52': (3298,2838), '51': (3686,2838), 
'61': (194,3354), '62': (582,3354), '63': (970,3354), '64': (1358,3354), '65': (1746,3354), '66': (2134,3354), '67': (2522,3354), '68': (2910,3354), '69': (3298,3354), '70': (3686,3354), 
'80': (194,3870), '79': (582,3870), '78': (970,3870), '77': (1358,3870), '76': (1746,3870), '75': (2134,3870), '74': (2522,3870), '73': (2910,3870), '72': (3298,3870), '71': (3686,3870), 
'81': (194,4386), '82': (582,4386), '83': (970,4386), '84': (1358,4386), '85': (1746,4386), '86': (2134,4386), '87': (2522,4386), '88': (2910,4386), '89': (3298,4386), '90': (3686,4386), 
'100': (194,4902), '99': (582,4902), '98': (970,4902), '97': (1358,4902), '96': (1746,4902), '95': (2134,4902), '94': (2522,4902), '93': (2910,4902), '92': (3298,4902), '91': (3686,4902)
}



# checkers_mappings['A1'] -> (0, 0)
# start = checkers_mapping[ 'B1']
#start[0] = x coordinate, start[1] = y coordinate



def step( axis, direction):
    if axis == 'x':
        if direction == 'forward':
            dir.value = True
        elif direction == 'backward':
            dir.value = False
        stp.value = True
        time.sleep(0.01)
        stp.value = False
    elif axis == 'y':
        if direction == 'forward':
            dirY.value = True
        elif direction == 'backward':
            dirY.value = False
        stpY.value = True
        time.sleep(0.01)
        stpY.value = False

    

#aarguments are 'A1' type
def StrightLine(start, end, current):
    start = checkers_mappings[start]    # converts it to (#,#)
    end = checkers_mappings[end]
    current = checkers_mappings[current]

    diffx1 = current[0] - start[0]     
    diffy1 = current[1] - start[1] 
    diffx2 = end[0] - start[0]
    diffy2 = end[1] - start[1]

    EN.value = False
    ENY.value = False
    if abs(diffx1) > abs(diffy1):
        LargestJump = diffx1
    else: 
        LargestJump = diffy1

    for steps in range(LargestJump):
        cXStep = abs(diffx1) * steps / LargestJump
        fXStep = abs(diffx1) * (steps + 1) / LargestJump
        cYStep = abs(diffy1) * steps / LargestJump
        fYStep = abs(diffy1) * (steps + 1) / LargestJump

        if cXStep != fXStep and  cYStep != fYStep:
            if diffx1 > 0:
                step('x', 'backward')
            if diffx1 < 0:
                step('x','forward')
            if diffy1 > 0:
                step('y','backward')
            if diffy1 < 0:   
                step('y','forward')
        elif cXStep != fXStep:
            if diffx1 > 0:
                step('x','backward')
            if diffx1 < 0:
                step('x','forward')
        else: 
            if diffy1 > 0:
                step('y','backward')
            if diffy1 < 0:
                step('y', 'forward')
        time.sleep(0.01)
    # we have reached our start location turn magnet on to drag piece 
    MAG.value = True                                         
    #now same idea but from start to end instead of current to start
    if abs(diffx2) > abs(diffy2):
        LargestJump = diffx2
    else: 
        LargestJump = diffy2

    for steps in range(LargestJump):
        cXStep = abs(diffx2) * steps / LargestJump
        fXStep = abs(diffx2) * (steps + 1) / LargestJump
        cYStep = abs(diffy2) * steps / LargestJump
        fYStep = abs(diffy2) * (steps + 1) / LargestJump

        if cXStep != fXStep and  cYStep != fYStep:
            if diffx2 > 0:
                step('x','backward')
            if diffx2 < 0:
                step('x','forward')
            if diffy2 > 0:
                step('y','backward')
            if diffy2 < 0:
                step('y','forward')
        elif cXStep != fXStep:
            if diffx2 > 0:
                step('x','backward')
            if diffx2 < 0:
                step('x', 'forward')
        else: 
            if diffy2 > 0:
                step('y','backward')
            if diffy2 < 0:
                step('y','forward')
        time.sleep(0.01)
    MAG.value = False                              
    # we have completed the move from start to end and now we turn off electromagnet. 
    

