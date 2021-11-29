import time
import board
import digitalio

# will have to change this for our pcb and put this in main while loop code
stp = digitalio.DigitalInOut(board.D2)
dir = digitalio.DigitalInOut(board.D3)
MS1 = digitalio.DigitalInOut(board.D4)
MS2 = digitalio.DigitalInOut(board.D5)
EN = digitalio.DigitalInOut(board.D6)

Button = digitalio.DigitalInOut(board.D13)
MAG = digitalio.DigitalInOut(board.D12)  

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

MAG.direction =  digitalio.Direction.OUTPUT
Button.direction = digitalio.Direction.INPUT

stpY.direction =  digitalio.Direction.OUTPUT
dirY.direction =  digitalio.Direction.OUTPUT
MS1Y.direction =  digitalio.Direction.OUTPUT
MS2Y.direction =  digitalio.Direction.OUTPUT
ENY.direction = digitalio.Direction.OUTPUT 


stp.value = False    # deafult no step
EN.value = True      # default to being off   True = off,   False = on
MS1.value = False    # default to full steps
MS2.value = False 
dir.value = False     # will have to change this. Make default positive direction 
MAG.value = False    #defult magnet off

stpY.value = False    # deafult no step
ENY.value = True      # default to being off   True = off,   False = on
MS1Y.value = False    # default to full steps
MS2Y.value = False 
dirY.value = True     # will have to change this. Make default positive direction 


#Deans work is crap not 5175 per axis more like 1300. Will have to test to get 
# test x-axis  = 1300 y axis= 1425


# checkers board is perfect square so 1300 x 1300
# 1300/8 = 162.5 = 162

checkers_mappings = { #col0 = lower level,  col9 = upper level, R for right side of baord, L for left side of board
            'A0' : (81, 0), 'B0' : (243, 0), 'C0' : (405, 0), 'D0' : (567, 0), 'E0' : (729, 0), 'F0' : (891, 0), 'G0' : (1053, 0), 'H0' : (1215, 0), 
 'L1' : (0,81), 'A1' : (81,81), 'B1' : (243,81), 'C1' : (405,81), 'D1' : (567,81), 'E1' : (729,81), 'F1' : (891,81), 'G1' : (1053,81), 'H1' : (1215,81), 'R1' : (1300,81),
 'L2' : (0,243), 'A2' : (81,243), 'B2' : (243,243), 'C2' : (405,243), 'D2' : (567,243), 'E2' : (729,243), 'F2' : (891,243), 'G2' : (1053,243), 'H2' : (1215,243), 'R2' : (1300,243),
 'L3' : (0,405), 'A3' : (81,405), 'B3' : (243,405), 'C3' : (405,405), 'D3' : (567,405), 'E3' : (729,405), 'F3' : (891,405), 'G3' : (1053,405), 'H3' : (1215,405), 'R3' : (1300,405),
 'L4' : (0,567), 'A4' : (81,567), 'B4' : (243,567), 'C4' : (405,567), 'D4' : (567,567), 'E4' : (729,567), 'F4' : (891,567), 'G4' : (1053,567), 'H4' : (1215,567), 'R4' : (1300,567),
 'L5' : (0,729), 'A5' : (81,729), 'B5' : (243,729), 'C5' : (405,729), 'D5' : (567,729), 'E5' : (729,729), 'F5' : (891,729), 'G5' : (1053,729), 'H5' : (1215,729), 'R5' : (1300,729),
 'L6' : (0,891), 'A6' : (81,891), 'B6' : (243,891), 'C6' : (405,891), 'D6' : (567,891), 'E6' : (729,891), 'F6' : (891,891), 'G6' : (1053,891), 'H6' : (1215,891), 'R6' : (1300,891),
 'L7' : (0,1053), 'A7' : (81,1053), 'B7' : (243,1053), 'C7' : (405,1053), 'D7' : (567,1053), 'E7' : (729,1053), 'F7' : (891,1053), 'G7' : (1053,1053), 'H7' : (1215,1053), 'R7' : (1300,1053),
 'L8' : (0,1215), 'A8' : (81,1215), 'B8' : (243,1215), 'C8' : (405,1215), 'D8' : (567,1215), 'E8' : (729,1215), 'F8' : (891,1215), 'G8' : (1053,1215), 'H8' : (1215,1215), 'R8' : (1300,1215),
                'A9' : (81,1300), 'B9' : (243,1300), 'C9' : (405,1300), 'D9' : (567,1300), 'E9' : (729,1300), 'F9' : (891,1300), 'G9' : (1053,1300), 'H9' : (1215,1300)
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
            dir.value = False
        elif direction == 'backward':
            dir.value = True
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

    diffx1 = start[0] - current[0]     
    diffy1 = start[1] - current[1] 
    diffx2 = end[0] - start[0]
    diffy2 = end[1] - start[1]

    EN.value = False
    ENY.value = False
    if abs(diffx1) >= abs(diffy1):
        LargestJump = diffx1
    else: 
        LargestJump = diffy1

    for steps in range(abs(LargestJump)):
        cXStep = (abs(diffx1) * steps) / LargestJump
        fXStep = (abs(diffx1) * (steps + 1)) / LargestJump
        cYStep = (abs(diffy1) * steps) / LargestJump
        fYStep = (abs(diffy1) * (steps + 1)) / LargestJump

        if cXStep != fXStep and  cYStep != fYStep:
            if diffx1 > 0:
                step('x', 'forward')
            if diffx1 < 0:
                step('x','backward')
            if diffy1 > 0:
                step('y','forward')
            if diffy1 < 0:   
                step('y','backward')
        elif cXStep != fXStep:
            if diffx1 > 0:
                step('x','forward')
            if diffx1 < 0:
                step('x','backward')
        else: 
            if diffy1 > 0:
                step('y','forward')
            if diffy1 < 0:
                step('y', 'backward')
        #time.sleep(0.01)
    # we have reached our start location turn magnet on to drag piece 
    MAG.value = True                                         
    #now same idea but from start to end instead of current to start
    if abs(diffx2) >= abs(diffy2):
        LargestJump = diffx2
    else: 
        LargestJump = diffy2

    for steps in range(abs(LargestJump)):
        cXStep = (abs(diffx2) * steps) / LargestJump
        fXStep = (abs(diffx2) * (steps + 1)) / LargestJump
        cYStep = (abs(diffy2) * steps) / LargestJump
        fYStep = (abs(diffy2) * (steps + 1)) / LargestJump

        if cXStep != fXStep and  cYStep != fYStep:
            if diffx2 > 0:
                step('x','forward') 
            if diffx2 < 0:
                step('x','backward')
            if diffy2 > 0:
                step('y','forward')
            if diffy2 < 0:
                step('y','backward')
        elif cXStep != fXStep:
            if diffx2 > 0: 
                step('x','forward')
            if diffx2 < 0:
                step('x', 'backward')
        else: 
            if diffy2 > 0:
                step('y','forward')
            if diffy2 < 0: 
                step('y','backward')
        #time.sleep(0.01)
    MAG.value = False            
    # we have completed the move from start to end and now we turn off electromagnet. 
    

