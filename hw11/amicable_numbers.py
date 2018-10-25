# Name: Find the Running Median
# Course: CS 370
# Professor: Borowski
# Assignment: Assignment 11
# @file AmicableNumbers.py
# @author: Aimal Wajihuddin
# 			Zach Saegesser
# 			Ryan Edelstein
#
# I pledges my honor that I have abided by the Stevens Honor System
#							- Aimal Wajihuddin
# 							- Zach Saegesser
# 							- Ryan Edelstein

import math
import time
import sys
from itertools import combinations

def findDivisors(n):
	'''
	Function to find all of the divisors of a given number n
	'''
	#initialize list of divisors
	divisors = [1]
	# Only go up to square root of n because no factor of n
	# will be bigger than that
	# Start from 2 because 1 is already added
	# Plus this is faster...
	for i in range(2, math.ceil(math.sqrt(n))):
		# if i evenly divides n
		if n % i == 0:
			# and if i isn't already in divisors
			if i not in divisors:
				divisors.append(i)
				temp = int(n/i)
				# if n/i isn't in divisors (will fo in evenly)
				# added it to divisors
				if temp not in divisors:
					divisors.append(temp)
	return divisors

def findAmicablePairsAndSum(n):
	'''
	Function to find all of the amicable number pairs from 0 to n
	and along with them, their total sum
	'''
	# Initialize list of pairs and sum variable
	resultPairs = []
	totalSum = 0
	# For i up to 100,000
	# used n for testing...
	for i in range(n):
		# Find potential pair of amicable numbers
		a = sum(findDivisors(i))
		b = sum(findDivisors(a))
		#if i and a are amicable and not the same number
		if i == b and i != a:
			res = (min(i,a),max(i,a))
			# Add the new pair to the result list and increment
			# totalSum accordingly
			if res not in resultPairs:
				resultPairs.append(res)
				totalSum += i + a
	return [totalSum, resultPairs]

if __name__ == '__main__':
	# Take time and find result(s)
	startTime = time.time()*1000
	result = findAmicablePairsAndSum(100000)
	pairs = result[1]
	sumOfAmicableNums = str(result[0])

	# Print the pairs
	for pair in pairs:
		sys.stdout.write('(')
		sys.stdout.write(str(pair[0]))
		sys.stdout.write(', ')
		sys.stdout.write(str(pair[1]))
		sys.stdout.write(')\n')
	
	# Calcualte time taken to calculate and print
	endTime = time.time()*1000
	elapsedTime = endTime - startTime

	# Print desired statistics
	sys.stdout.write("Sum: ")
	sys.stdout.write(sumOfAmicableNums)
	sys.stdout.write("\nElapsed time: ")
	sys.stdout.write('{0:.2f}'.format(elapsedTime))
	sys.stdout.write(" ms")