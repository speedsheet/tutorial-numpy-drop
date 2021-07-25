#!/usr/bin/env python3

from math import log10
from math import cos

from shared import *
from math import sqrt


RADIAN = 6.283185307179586

MAX_VALUE = 10
STEP = 0.1
DECAY_MULTIPLIER = 9 / MAX_VALUE

HEIGHT_MULTIPLIER = RADIAN * 4 / MAX_VALUE
PERIODS = 4

SHOW_FORMATTED = True


def decay(index):
	''' Returns a value from 1 to 0
		over a range of 0 to MAX_VALUE
		reduced logaritmicly.

		> MAX_VALUE returns 0
	'''

	if index > MAX_VALUE:
		return 0

	adjusted = 1 + index * DECAY_MULTIPLIER
	value = 1 - log10 (adjusted)

	return value


def decayed_height(index):
	return decay(index) * height(index)


def distance(x, y):
	return sqrt(x ** 2 + y **2)


def height (index):
	return cos(index * HEIGHT_MULTIPLIER)


def frange (start, stop, step = 1):
	value = start

	if step == 0:
		raise ValueError ("Invalid step value of 0")

	if step < 0:

		while value >= stop:
			yield value
			value = value + step

	else:

		while value <= stop:
			yield value
			value = value + step


def new_array (min, max, step, ):
	pass



title("Exponent Decay")


short_heading ("Decay Calc")

if SHOW_FORMATTED:

	print ("  index      decay     height   combined")
	nl()

	for value in frange (0, MAX_VALUE, STEP):
		print (f"{value:>7.1f}    {decay(value):>7.2f}    {height(value):7.2f}    {decayed_height(value):>7.2f}")

else:

	for value in frange (0, MAX_VALUE, STEP):
		print (value, decay(value), height(value), decayed_height(value))

nl()


if False:


	with open("data_xyz.csv", 'w') as file:

		file.write ("x,y,z\n")

		for y in frange(-MAX_VALUE, MAX_VALUE, STEP):

			print (f"{y:.2f}...")

			for x in frange(-MAX_VALUE, MAX_VALUE, STEP):

				length = distance (x, y)
				z = decayed_height (length)

				file.write(f"{x:.2f},{y:.2f},{z:.3f}\n")




	with open("data_zz.csv", 'w') as file:

		for y in frange(-MAX_VALUE, MAX_VALUE, STEP):

			print (f"{y:.2f}...")

			first = True

			for x in frange(-MAX_VALUE, MAX_VALUE, STEP):

				if first:
					first = False
				else:
					file.write(",")

				length = distance (x, y)
				z = decay (length) * height (length)

				file.write(f"{z:.3f}")

			file.write("\n")



