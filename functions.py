from setup import *
from ss_numbers import *
from time import sleep
      
def turnON():
	GPIO.output(good, GPIO.HIGH)
	GPIO.output(push, GPIO.HIGH)
	GPIO.output(pull, GPIO.HIGH)
	GPIO.output(a1, GPIO.HIGH)
	GPIO.output(b1, GPIO.HIGH)
	GPIO.output(c1, GPIO.HIGH)
	GPIO.output(d1, GPIO.HIGH)
	GPIO.output(e1, GPIO.HIGH)
	GPIO.output(f1, GPIO.HIGH)
	GPIO.output(g1, GPIO.HIGH)
	GPIO.output(b2, GPIO.HIGH)
	GPIO.output(c2, GPIO.HIGH)


def turnOFF():
    # Your existing turnOFF logic here
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
    
def turnOFF_SSD():
	GPIO.output(b2, GPIO.LOW)
	GPIO.output(c2, GPIO.LOW)
	GPIO.output(a1, GPIO.LOW)
	GPIO.output(b1, GPIO.LOW)
	GPIO.output(c1, GPIO.LOW)
	GPIO.output(d1, GPIO.LOW)
	GPIO.output(e1, GPIO.LOW)
	GPIO.output(f1, GPIO.LOW)
	GPIO.output(g1, GPIO.LOW)
	
def test_switch(switch):
	prev = 0
	while True:
		if readSwitch(switch) != prev:
			if prev == 0:
				turnON()
				prev = 1
			else:
				turnOFF()
				prev = 0


def countdown():
	nineteen()
	sleep(1)
	eighteen()
	sleep(1)
	seventeen()
	sleep(1)
	sixteen()
	sleep(1)
	fifteen()
	sleep(1)
	fourteen()
	sleep(1)
	thirteen()
	sleep(1)
	twelve()
	sleep(1)
	eleven()
	sleep(1)
	ten()
	sleep(1)
	nine()
	sleep(1)
	eight()
	sleep(1)
	seven()
	sleep(1)
	six()
	sleep(1)
	five()
	sleep(1)
	four()
	sleep(1)
	three()
	sleep(1)
	two()
	sleep(1)
	one()
	sleep(1)
	zero()
	sleep(1)
	turnOFF_SSD()
	
	
def readSwitch(switch):
	lowCnt = 0
	for i in range(6000):
		if GPIO.input(switch) == GPIO.LOW:
			lowCnt += 1
	#print("low count is", lowCnt)
	if lowCnt >= 100:
		return 0
	else:
		return 1

def calcDistance(x_a_max):
	print("Peak Value", x_a_max)
	
	# Acceleration value scaled to match corresponding distance
	if readSwitch(rainy) == 1:
		d = ((5.8833*x_a_max) - 3.9535)*.8
	else:
		d = (5.8833*x_a_max) - 3.9535
	
	# print(d)
	
	return d
