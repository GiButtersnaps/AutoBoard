
import time
import board
import busio
import digitalio
#from adafruit_motorkit import MotorKit   # this is to call stepper motors
#from adafruit_motor import stepper       # this is to use direction and style stepper commands. 


#print(dir(board))
#i2c = busio.I2C(board.SCL, board.SDA)
stp = digitalio.DigitalInOut(board.D2)
dir = digitalio.DigitalInOut(board.D3)
MS1 = digitalio.DigitalInOut(board.D4)
MS2 = digitalio.DigitalInOut(board.D5)
EN = digitalio.DigitalInOut(board.D6)

stp.direction =  digitalio.Direction.OUTPUT
dir.direction =  digitalio.Direction.OUTPUT
MS1.direction =  digitalio.Direction.OUTPUT
MS2.direction =  digitalio.Direction.OUTPUT
EN.direction = digitalio.Direction.OUTPUT
EN.value = True

 
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
# #         kit.stepper1.onestep()
        stp.value = False
        time.sleep(0.01)
        stp.value = True
        time.sleep(0.01) 
        stp.value = False
        time.sleep(0.01) 
 
    print("done") 
#    
#time.sleep(10)
#print(EN.value)
# kit = MotorKit(i2c)

# testmotor(kit)

testmotor(250) 
EN.value = True
time.sleep(5)