# Name: Scrable Squares Puzzle Solver
# Course: CS 370
# Professor: Borowski
# Assignment: Assignment 5
# @file readFile.py
# @author: Aimal Wajihuddin
# 			Zach Saegesser
# 			Ryan Edelstein
#
# I pledge my honor that I have abided by the Stevens Honor System
#							- Aimal Wajihuddin
# 							- Zach Saegesser
# 							- Ryan Edelstein

import numpy as np
import block as b
import sys

def getNumpyArrayOfSquares(filename):
	#set np array type to python object
	dt = np.dtype('O')
	arr = np.array([], dtype = dt)
	#go through each line in file, removing "\n", spliting by ",", then appending to arr
	#i is used to number the blocks
	with open(filename) as file:
		counter = 1
		sys.stdout.write('Input tiles:\n')
		for i,line in enumerate(file):
			curr = np.array(line.replace("\n", "").split(','))

			sys.stdout.write(str(counter))
			sys.stdout.write('. <')
			sys.stdout.write(curr[0])
			sys.stdout.write(',')
			sys.stdout.write(curr[1])
			sys.stdout.write(',')
			sys.stdout.write(curr[2])
			sys.stdout.write(',')
			sys.stdout.write(curr[3])
			sys.stdout.write('>\n')

			counter += 1
			arr = np.append(arr, b.Square(curr, i+1))
		sys.stdout.write('\n')
		return arr
