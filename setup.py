import RPi.GPIO as GPIO
import time
import math
import board
import busio
import adafruit_mpu6050

#MPU input 
#i2c = busio.I2C(board.SCL, board.SDA)
#mpu = adafruit_mpu6050.MPU6050(i2c)

#GPIO pins
#LEDS
good = 21
push = 20
pull = 16

#switches
sS = 25
rainy = 24

#number displays
a1 = 23
b1 = 18
c1 = 27
d1 = 22
e1 = 5
f1 = 6
g1 = 13
b2 = 19
c2 = 26

GPIO.setmode(GPIO.BCM)

#Setting up pins
#LEDs
GPIO.setup(good, GPIO.OUT)
GPIO.setup(push, GPIO.OUT)
GPIO.setup(pull, GPIO.OUT)

#Switches
GPIO.setup(sS, GPIO.IN)
GPIO.setup(rainy, GPIO.IN)

# Seven Segment Setup
GPIO.setup(a1, GPIO.OUT)
GPIO.setup(b1, GPIO.OUT)
GPIO.setup(c1, GPIO.OUT)
GPIO.setup(d1, GPIO.OUT)
GPIO.setup(e1, GPIO.OUT)
GPIO.setup(f1, GPIO.OUT)
GPIO.setup(g1, GPIO.OUT)
GPIO.setup(b2, GPIO.OUT)
GPIO.setup(c2, GPIO.OUT)
