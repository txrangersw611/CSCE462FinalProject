import board
import busio
import adafruit_mpu6050
import numpy as np
import matplotlib.pyplot as plt
from setup import *
from functions import *
from ss_numbers import *

# perf_counter is more precise than time() for dt calculation
from time import time, sleep
i2c = busio.I2C(board.SCL, board.SDA)
mpu = adafruit_mpu6050.MPU6050(i2c)

# Function to calculate simple moving average
def SMA(data, n_points):
    # Use convolution to efficiently calculate the moving average
    weights = np.ones(n_points) / n_points
    sma = np.convolve(data, weights, mode='valid')

    return sma

def readSensor():
	time_points = np.array([])
	x_a = np.array([])
	y_a = np.array([])
	z_a = np.array([])

	# Write a loop to poll sensor for acceleration values and place in respective arrays
	# Calibration is applied to each axis of acceleration as well
	# Old calibration: x: +1.48, y: -9.45, z: +0.02
	#sleep(2) 
	t_init = time()
	t = 0
	while readSwitch(sS) == 1:
		time_points = np.append(time_points, t)
		x_a = np.append(x_a, mpu.acceleration[2]*(-1) + 1.48)
		y_a = np.append(y_a, mpu.acceleration[0]*(-1) - 9.45)
		z_a = np.append(z_a, mpu.acceleration[1] + 0.02)
		t = time() - t_init
			
	# Smooth data
	n_points = 30
	n_z_points = 30

	x_a_smooth = SMA(x_a, n_points)
	y_a_smooth = SMA(y_a, n_points)
	z_a_smooth = SMA(z_a, n_z_points)
	
	# Determining Swing States
	started = False
	afterFirstZero = False
	
	startedIndex = 0
	firstZeroIndex = 0
	finalIndex = 0
	
	
	baseline = np.mean(x_a_smooth[0:6])
	tol = .25
	
	
	for i in range(len(x_a_smooth)):
		if started:
			if ((baseline - tol) < x_a_smooth[i] < (baseline + tol)):
				if afterFirstZero and ((i - firstZeroIndex) > 7):
					finalIndex = i
					break
				
				else:
					afterFirstZero = True
					firstZeroIndex = i
			
		else:
			if (abs(x_a_smooth[i]) > (abs(baseline) + .3)):
				started = True
				startedIndex = i

	
	
	# Test printing
	print("Curve data")
	print(x_a_smooth)
	print(baseline)
	print(x_a_smooth[firstZeroIndex], firstZeroIndex)
	print(x_a_smooth[finalIndex], finalIndex)
	
	
	
	# Good/Push/Pull Light
	# Compare the avg of the z during the downswing against the baseline to determine swing path
	print("Z acceleration data")
	z_baseline = np.mean(z_a_smooth[0:6])
	z_path_max = np.max(z_a_smooth[firstZeroIndex:finalIndex])
	z_path_min = np.min(z_a_smooth[firstZeroIndex:finalIndex])
	z_tol = .5
	
	print(z_baseline)
	print(z_path_max, z_path_min)
	
	# Find which is farther, max or min
	diff_max = abs(z_path_max - z_baseline)
	diff_min = abs(z_path_min - z_baseline)

	# Push
	if (z_path_max > (z_baseline + z_tol)) and (diff_max > diff_min):
		GPIO.output(push, GPIO.HIGH)
		GPIO.output(pull, GPIO.LOW)
		GPIO.output(good, GPIO.LOW)
	
	# Pull
	elif (z_path_min < (z_baseline - z_tol)) and (diff_max < diff_min):
		GPIO.output(push, GPIO.LOW)
		GPIO.output(pull, GPIO.HIGH)
		GPIO.output(good, GPIO.LOW)
	
	# Good
	else:
		GPIO.output(push, GPIO.LOW)
		GPIO.output(pull, GPIO.LOW)
		GPIO.output(good, GPIO.HIGH)
	
	# # Push
	# if z_path > (z_baseline + z_tol):
		# GPIO.output(push, GPIO.HIGH)
		# GPIO.output(pull, GPIO.LOW)
		# GPIO.output(good, GPIO.LOW)
	
	# # Pull
	# elif z_path < (z_baseline - z_tol):
		# GPIO.output(push, GPIO.LOW)
		# GPIO.output(pull, GPIO.HIGH)
		# GPIO.output(good, GPIO.LOW)
	
	# # Good
	# else:
		# GPIO.output(push, GPIO.LOW)
		# GPIO.output(pull, GPIO.LOW)
		# GPIO.output(good, GPIO.HIGH)
		
	# Report distance to user
	d = calcDistance(np.max(x_a_smooth[firstZeroIndex:finalIndex]) - baseline)
	
	
	if d >= 19:
		nineteen()
	elif d >= 18:
		eighteen()
	elif d >= 17:
		seventeen()
	elif d >= 16:
		sixteen()
	elif d >= 15:
		fifteen()
	elif d >= 14:
		fourteen()
	elif d >= 13:
		thirteen()
	elif d >= 12:
		twelve()
	elif d >= 11:
		eleven()
	elif d >= 10:
		ten()
	elif d >= 9:
		nine()
	elif d >= 8:
		eight()
	elif d >= 7:
		seven()
	elif d >= 6:
		six()
	elif d >= 5:
		five()
	elif d >= 4:
		four()
	elif d >= 3:
		three()
	elif d >= 2:
		two()
	elif d >= 1:
		one()
	else:
		zero()
	
	# Graph data
	figure, axis = plt.subplots(3, 3)

	axis[0, 0].plot(time_points, x_a)
	axis[0, 0].set_title("X Acceleration")

	axis[0, 1].plot(time_points, y_a)
	axis[0, 1].set_title("Y Acceleration")

	axis[0, 2].plot(time_points, z_a)
	axis[0, 2].set_title("Z Acceleration")

	time_points_smoothed = np.array([])
	for i in range (n_points, len(time_points) + 1):
		time_points_smoothed = np.append(time_points_smoothed, time_points[i-n_points])
		
	axis[1, 0].plot(time_points_smoothed, x_a_smooth)
	axis[1, 0].set_ylim([-5, 5])

	axis[1, 1].plot(time_points_smoothed, y_a_smooth)
	axis[1, 1].set_ylim([-5, 5])

	axis[1, 2].plot(time_points_smoothed, z_a_smooth)
	axis[1, 2].set_ylim([-5, 5])
	
	# ceriv

	axis[2, 0].plot(time_points_smoothed[0:finalIndex], x_a_smooth[0:finalIndex])
	axis[2, 0].set_ylim([-5, 5])

	axis[2, 1].plot(time_points_smoothed[0:finalIndex], y_a_smooth[0:finalIndex])
	axis[2, 1].set_ylim([-5, 5])

	axis[2, 2].plot(time_points_smoothed[0:finalIndex], z_a_smooth[0:finalIndex])
	axis[2, 2].set_ylim([-5, 5])

	plt.show()
	
	
	# tol = 0.15
	# numZeroDer = 0
	# finalIndex = 0
	# isZero = True
	
	# for i in range(len(clean_x)):
		# if numZeroDer == 3:
			# finalIndex = i
			# break
		# elif abs(clean_x[i]) > tol and isZero:
			# numZeroDer += 1
			# print(numZeroDer)
			# isZero = False
			# continue
		# elif abs(clean_x[i]) < tol and not isZero:
			# isZero = True
			# continue
		# else:
			# continue
			
	# print(finalIndex)
			
