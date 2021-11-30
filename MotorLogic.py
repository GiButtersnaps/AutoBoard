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
'A0' : (0, 0), 'B0' : (185, 0), 'C0' : (371, 0), 'D0' : (557, 0), 'E0' : (743, 0), 'F0' : (929, 0), 'G0' : (1115, 0), 'H0' : (1300, 0), 
 'A1' : (0,0), 'B1' : (185,0), 'C1' : (371,0), 'D1' : (557,0), 'E1' : (743,0), 'F1' : (929,0), 'G1' : (1115,0), 'H1' : (1300,0), 
 'A2' : (0,185), 'B2' : (185,185), 'C2' : (371,185), 'D2' : (557,185), 'E2' : (743,185), 'F2' : (929,185), 'G2' : (1115,185), 'H2' : (1300,185), 
 'A3' : (0,371), 'B3' : (185,371), 'C3' : (371,371), 'D3' : (557,371), 'E3' : (743,371), 'F3' : (929,371), 'G3' : (1115,371), 'H3' : (1300,371), 
 'A4' : (0,557), 'B4' : (185,557), 'C4' : (371,557), 'D4' : (557,557), 'E4' : (743,557), 'F4' : (929,557), 'G4' : (1115,557), 'H4' : (1300,557), 
 'A5' : (0,743), 'B5' : (185,743), 'C5' : (371,743), 'D5' : (557,743), 'E5' : (743,743), 'F5' : (929,743), 'G5' : (1115,743), 'H5' : (1300,743), 
 'A6' : (0,929), 'B6' : (185,929), 'C6' : (371,929), 'D6' : (557,929), 'E6' : (743,929), 'F6' : (929,929), 'G6' : (1115,929), 'H6' : (1300,929), 
 'A7' : (0,1115), 'B7' : (185,1115), 'C7' : (371,1115), 'D7' : (557,1115), 'E7' : (743,1115), 'F7' : (929,1115), 'G7' : (1115,1115), 'H7' : (1300,1115), 
 'A8' : (0,1300), 'B8' : (185,1300), 'C8' : (371,1300), 'D8' : (557,1300), 'E8' : (743,1300), 'F8' : (929,1300), 'G8' : (1115,1300), 'H8' : (1300,1300), 
'A9' : (0,1300), 'B9' : (185,1300), 'C9' : (371,1300), 'D9' : (557,1300), 'E9' : (743,1300), 'F9' : (929,1300), 'G9' : (1115,1300), 'H9' : (1300,1300)
}

chutes_mappings = {
'1' : (0,0), '2' : (146,0), '3' : (290,0), '4' : (434,0), '5' : (578,0), '6' : (722,0), '7' : (866,0), '8' : (1010,0), '9' : (1154,0), '10' : (3686,0),
'20': (0,146), '19': (146,146), '18': (290,146), '17': (434,146), '16': (578,146), '15': (722,146), '14': (866,146), '13': (1010,146), '12': (1154,146), '11' : (3686,146), 
'21': (0,290), '22': (146,290), '23': (290,290), '24': (434,290), '25': (578,290), '26': (722,290), '27': (866,290), '28': (1010,290), '29': (1154,290), '30': (3686,290), 
'40': (0,434), '39': (146,434), '38': (290,434), '37': (434,434), '36': (578,434), '35': (722,434), '34': (866,434), '33': (1010,434), '32': (1154,434), '31': (3686,434), 
'41': (0,578), '42': (146,578), '43': (290,578), '44': (434,578), '45': (578,578), '46': (722,578), '47': (866,578), '48': (1010,578), '49': (1154,578), '50': (3686,578), 
'60': (0,722), '59': (146,722), '58': (290,722), '57': (434,722), '56': (578,722), '55': (722,722), '54': (866,722), '53': (1010,722), '52': (1154,722), '51': (3686,722), 
'61': (0,866), '62': (146,866), '63': (290,866), '64': (434,866), '65': (578,866), '66': (722,866), '67': (866,866), '68': (1010,866), '69': (1154,866), '70': (3686,866), 
'80': (0,1010), '79': (146,1010), '78': (290,1010), '77': (434,1010), '76': (578,1010), '75': (722,1010), '74': (866,1010), '73': (1010,1010), '72': (1154,1010), '71': (3686,1010), 
'81': (0,1154), '82': (146,1154), '83': (290,1154), '84': (434,1154), '85': (578,1154), '86': (722,1154), '87': (866,1154), '88': (1010,1154), '89': (1154,1154), '90': (3686,1154), 
'100': (0,1300), '99': (146,1300), '98': (290,1300), '97': (434,1300), '96': (578,1300), '95': (722,1300), '94': (866,1300), '93': (1010,1300), '92': (1154,1300), '91': (3686,1300)
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
def StrightLine(start, end, current, game):
    if game == 'checkers':
        start = checkers_mappings[start]    # converts it to (#,#)
        end = checkers_mappings[end]
        current = checkers_mappings[current]
    elif game == 'chutes':
        start = chutes_mappings[start]    # converts it to (#,#)
        end = chutes_mappings[end]
        current = chutes_mappings[current]
        

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
    

