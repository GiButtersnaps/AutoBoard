from os import lchown
import time
import board
from adafruit_motorkit import MotorKit   # this is to call stepper motors
from adafruit_motor import stepper       # this is to use direction and style stepper commands. 

def testmotor(kit):
    for i in range(100):
        kit.stepper1.onestep()
        time.sleep(0.01)