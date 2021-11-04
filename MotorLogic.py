from os import lchown
import time
import board
import digitalio
#from adafruit_motorkit import MotorKit   # this is to call stepper motors
#from adafruit_motor import stepper       # this is to use direction and style stepper commands. 

#kit = MotorKit()



# will have to change this for our pcb and put this in main while loop code
stp = digitalio.DigitalInOut(board.D2)
dir = digitalio.DigitalInOut(board.D3)
MS1 = digitalio.DigitalInOut(board.D4)
MS2 = digitalio.DigitalInOut(board.D5)
EN = digitalio.DigitalInOut(board.D6)
MAG = digitalio.DigitalInOut(board.D7)

stp.direction =  digitalio.Direction.OUTPUT
dir.direction =  digitalio.Direction.OUTPUT
MS1.direction =  digitalio.Direction.OUTPUT
MS2.direction =  digitalio.Direction.OUTPUT
EN.direction = digitalio.Direction.OUTPUT
stp.value = False    # deafult no step
EN.value = True      # default to being off   True = off,   False = on
MS1.value = False    # default to full steps
MS2.value = False 
dir.value = True     # will have to change this. Make default positive direction 
MAG.value = False    #defult magnet off

#If deans work is correct distance(m) = 1(rev)/.005*pi * 200(steps)/1(rev)
#therefor 16in for playable area is 5174.45 steps. lets say 5175 steps. 
#So for coding purpuses we have a 5175,5175 step playable area. These will be our coordinates.
# we will then go ahead and figure out what space on the board refer to wait coordinate
#For example, black e4 to g5. e4 will be coords #, # and g5 will be coords #,# and then you can preform all functions below. 
# 646 * 8 = 5168 so each square will be 646 by 646

checkers_mappings = {
    'A1' : (323, 323), 'B1' : (969,323), 'C1' : (1615,323), 'D1' : (2261,323), 'E1' : (2907, 323), 'F1' : (3553, 323), 'G1' : (4199, 323), 'H1' : (4845,323), 
    'A2' : (323, 969), 'B2' : (969,969), 'C2' : (1615,969), 'D2' : (2261,969), 'E2' : (2907, 969), 'F2' : (3553, 969), 'G2' : (4199, 969), 'H2' : (4845,969),
    'A3' : (323, 1615), 'B3' : (969,1615), 'C3' : (1615,1615), 'D3' : (2261,1615), 'E3' : (2907, 1615), 'F3' : (3553, 1615), 'G3' : (4199, 1615), 'H3' : (4845,1615),
    'A4' : (323, 2261), 'B4' : (969,2261), 'C4' : (1615,2261), 'D4' : (2261,2261), 'E4' : (2907, 2261), 'F4' : (3553, 2261), 'G4' : (4199, 2261), 'H4' : (4845,2261),
    'A5' : (323, 2907), 'B5' : (969,2907), 'C5' : (1615,2907), 'D5' : (2261,2907), 'E5' : (2907, 2907), 'F5' : (3553, 2907), 'G5' : (4199, 2907), 'H5' : (4845,2907),
    'A6' : (323, 3553), 'B6' : (969,3553), 'C6' : (1615,3553), 'D6' : (2261,3553), 'E6' : (2907, 3553), 'F6' : (3553, 3553), 'G6' : (4199, 3553), 'H6' : (4845,3553),
    'A7' : (323, 4199), 'B7' : (969,4199), 'C7' : (1615,4199), 'D7' : (2261,4199), 'E7' : (2907, 4199), 'F7' : (3553, 4199), 'G7' : (4199, 4199), 'H7' : (4845,4199),
    'A8' : (323, 4845), 'B8' : (969,4845), 'C8' : (1615,4845), 'D8' : (2261,4845), 'E8' : (2907, 4845), 'F8' : (3553, 4845), 'G8' : (4199, 4845), 'H8' : (4845,4845)
}

chutes_mappings = {
    'A1' : (0, 0),
}

# checkers_mappings['A1'] -> (0, 0)
# start = checkers_mapping[ 'B1']
#start[0] = x coordinate, start[1] = y coordinate

#stepper 1 will be the two stpper motors on y axis
#stepper 2 will be the one stepper motor on x axis


def commandcheck(start, end):
    leftbottombound =0
    righttopbound = 5175    
    if start[0] < leftbottombound and start[0] > righttopbound:
        return False
    elif start[1] < leftbottombound and start[1] > righttopbound:
        return False
    elif end[0] < leftbottombound and end[0] > righttopbound:
        return False
    elif end[1] < leftbottombound and end[1] > righttopbound:
        return False
    else:
        return True

def step(direction):
    if direction == 'forward':
        dir.value = True
    if direction == 'backward':
        dir.value = False
    stp.value = True
    time.sleep(0.01)
    stp.value = False

    

# idk if this should be a function or in the main while loop. 
#assume start, end, current are 2 elements one for x and another y
def StrightLine(start, end, current):
    diffx1 = current[0] - start[0]
    diffy1 = current[1] - start[1] 
    diffx2 = end[0] - start[0]
    diffy2 = end[1] - start[1]

    EN.value = False

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
#                kit.stepper1.onestep(direction=stepper.BACKWARD)
                step('backward')
            if diffx1 < 0:
#                kit.stepper1.onestep()
                step('forward')
            if diffy1 > 0:
#                kit.stepper2.onestep(direction=stepper.BACKWARD)
                step('backward')
            if diffy1 < 0:
#                kit.stepper2.onestep()    
                step('forward')
        elif cXStep != fXStep:
            if diffx1 > 0:
#                kit.stepper1.onestep(direction=stepper.BACKWARD)
                step('backward')
            if diffx1 < 0:
#                kit.stepper1.onestep()
                step('forward')
        else: 
            if diffy1 > 0:
#                kit.stepper2.onestep(direction=stepper.BACKWARD)
                step('backward')
            if diffy1 < 0:
#                kit.stepper2.onestep()
                step('forward')
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
#                kit.stepper1.onestep(direction=stepper.BACKWARD)
                step('backward')
            if diffx2 < 0:
#                kit.stepper1.onestep()
                step('forward')
            if diffy2 > 0:
#                kit.stepper2.onestep(direction=stepper.BACKWARD)
                step('backward')
            if diffy2 < 0:
#                kit.stepper2.onestep()  
                step('forward')
        elif cXStep != fXStep:
            if diffx2 > 0:
#                kit.stepper1.onestep(direction=stepper.BACKWARD)
                step('backward')
            if diffx2 < 0:
#                kit.stepper1.onestep()
                step('forward')
        else: 
            if diffy2 > 0:
#                kit.stepper2.onestep(direction=stepper.BACKWARD)
                step('backward')
            if diffy2 < 0:
#                kit.stepper2.onestep()
                step('forward')
        time.sleep(0.01)
    MAG.value = False                              
    # we have completed the move from start to end and now we turn off electromagnet. 
    

