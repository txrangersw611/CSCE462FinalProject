from setup import *
from functions import *
from MPUdata import *

try:
    while True:
        if readSwitch(sS) == 1:
            readSensor()
        else:
            continue
    
except KeyboardInterrupt:
    print("\nTurning off.")
    
    GPIO.output(good, GPIO.LOW)
    GPIO.output(push, GPIO.LOW)
    GPIO.output(pull, GPIO.LOW)
    
    GPIO.output(a1, GPIO.LOW)
    GPIO.output(b1, GPIO.LOW)
    GPIO.output(c1, GPIO.LOW)
    GPIO.output(d1, GPIO.LOW)
    GPIO.output(e1, GPIO.LOW)
    GPIO.output(f1, GPIO.LOW)
    GPIO.output(g1, GPIO.LOW)
    GPIO.output(b2, GPIO.LOW)
    GPIO.output(c2, GPIO.LOW)
