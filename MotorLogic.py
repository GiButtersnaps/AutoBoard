from os import lchown
import time
import board
from adafruit_motorkit import MotorKit   # this is to call stepper motors
from adafruit_motor import stepper       # this is to use direction and style stepper commands. 

steps_to_distance_checkers = 5   # temporary until we find out
steps_to_distance_ladders = 6    # temporary until we find out 

kit = MotorKit()
#stepper 1 will be the two stpper motors on y axis
#stepper 2 will be the one stepper motor on x axis

#test 1 move stepper 100 steps.    
# for i in range(100):
#     kit.stepper1.onestep()
#     time.sleep(0.01)



# idk if this should be a function or in the main while loop. 
#assume start, end, current are 2 elements one for x and another y
def StrightLine(start, end, current):
    diffx1 = current[0] - start[0]
    diffy1 = current[1] - start[1] 
    diffx2 = end[0] - start[0]
    diffy2 = end[1] - start[1]
    
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
                kit.stepper1.onestep(direction=stepper.BACKWARD)
            if diffx1 < 0:
                kit.stepper1.onestep()
            if diffy1 > 0:
                kit.stepper2.onestep(direction=stepper.BACKWARD)
            if diffy1 < 0:
                kit.stepper2.onestep()    
        elif cXStep != fXStep:
            if diffx1 > 0:
                kit.stepper1.onestep(direction=stepper.BACKWARD)
            if diffx1 < 0:
                kit.stepper1.onestep()
        else: 
            if diffy1 > 0:
                kit.stepper2.onestep(direction=stepper.BACKWARD)
            if diffy1 < 0:
                kit.stepper2.onestep()
    # we have reached our start location 
    electromagnet = high                                             # idk what the command will be
    # turn on electromagnet
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
                kit.stepper1.onestep(direction=stepper.BACKWARD)
            if diffx2 < 0:
                kit.stepper1.onestep()
            if diffy2 > 0:
                kit.stepper2.onestep(direction=stepper.BACKWARD)
            if diffy2 < 0:
                kit.stepper2.onestep()    
        elif cXStep != fXStep:
            if diffx2 > 0:
                kit.stepper1.onestep(direction=stepper.BACKWARD)
            if diffx2 < 0:
                kit.stepper1.onestep()
        else: 
            if diffy2 > 0:
                kit.stepper2.onestep(direction=stepper.BACKWARD)
            if diffy2 < 0:
                kit.stepper2.onestep()
        time.sleep(0.01)
    electromagnet = low                                 # idk what command will be 
    # we have completed the move from start to end and now we turn off electromagnet. 
    

