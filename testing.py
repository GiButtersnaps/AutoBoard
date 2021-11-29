import time
import board
import digitalio

# will have to change this for our pcb and put this in main while loop code
stp = digitalio.DigitalInOut(board.D2)
dir = digitalio.DigitalInOut(board.D3)
MS1 = digitalio.DigitalInOut(board.D4)
MS2 = digitalio.DigitalInOut(board.D5)
EN = digitalio.DigitalInOut(board.D6)

MAG = digitalio.DigitalInOut(board.D12)  
Button = digitalio.DigitalInOut(board.D13) 

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
 
print(EN.value)
def testmotor( steps):

    EN.value = False
    print(EN)
    MS1.value = False
    MS2.value = False
    dir.value = False
    print("testing motor")
    for i in range(steps):
        print(i)
        stp.value = False
        time.sleep(0.01)
        stp.value = True
        time.sleep(0.01) 
        stp.value = False
        time.sleep(0.01) 
 
    print("done") 

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

def testyaxis(steps):
    ENY.value = False
    for i in range(steps):
        print(i)
        stpY.value = True
        time.sleep(0.01) 
        stpY.value = False
        time.sleep(0.01) 
    ENY.value = True

def testmagnet(sec):
    MAG.value = True
    for i in range(sec):
        time.sleep(1)
        print(i)
    MAG.value = False

def testButton():
    pressed =0
    while pressed < 5:
        if Button.value == True:
            pressed +=1



testyaxis(250) 
EN.value = True
time.sleep(5)