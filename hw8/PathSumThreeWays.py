# Name: Path sum: three ways
# Course: CS 370
# Professor: Borowski
# Assignment: Assignment 8
# @file PathSumThreeWays.py
# @author: Aimal Wajihuddin
# 			Zach Saegesser
# 			Ryan Edelstein
#
# rowPos pledge my honor that rowPos have abided by the Stevens Honor System
#							- Aimal Wajihuddin
# 							- Zach Saegesser
# 							- Ryan Edelstein

import sys

FILE_NAME = 'matrix.txt'

def readMatrixData(fileName):
	"""
	Function to read the data from the given file, and
	return a matrix, which is a 2D array, for use in the
	algorithm
	"""
	matrix = []
	f = open(fileName,'r')
	for i in f:
		matrix.append([int(i) for i in i.split(',')])
	f.close()
	return matrix

def pathSum(matrix):
	"""
	Function to build the sum table fully (with the minimum
	possible sums from the three possible directions) and 
	pass it on to findValues so it can backtrack and return
	the values used for the sum
	"""
	#establish the size of the matrix
	matrixSize = len(matrix[0])

	#base case so out code doesn't break
	if matrixSize == 1:
		return [matrix[0][0],[matrix[0][0]]]
	
	#initialize the workTable so we can access indices 
	workTable = [[0 for rowPos in range(matrixSize)] for columnPos in range(matrixSize)]
	
	#copy over the left-most column into workTable
	for rowPos in range(matrixSize):
		workTable[rowPos][0] = matrix[rowPos][0]

	#start solving and populating workTable for sums
	for columnPos in range(1,matrixSize):

		#you can only initially come from the left
		workTable[0][columnPos] = matrix[0][columnPos] + workTable[0][columnPos - 1]

		#populate this row in the table moving down
		for rowPos in range(1, matrixSize):
			workTable[rowPos][columnPos] = min(matrix[rowPos][columnPos] + workTable[rowPos][columnPos - 1], matrix[rowPos][columnPos] + workTable[rowPos - 1][columnPos])

		#populate the row moving back up, adjusting values if needed
		for rowPos in range(matrixSize-2, -1, -1):
			workTable[rowPos][columnPos] = min(matrix[rowPos][columnPos] + workTable[rowPos + 1][columnPos], workTable[rowPos][columnPos])
	
	result = findValues(workTable, matrixSize)
	return result

def findValues(matrix, size):
	"""
	Return the final result for the algorithm. It gets the
	fully built sum table from pathSum and returns the values
	used to obtain the minimum sum from the three way sum
	"""
	#initialize variables
	values = []
	start  = 0
	sumVar = matrix[0][size-1]
	rowPos = 0
	columnPos = size - 1

	#obtain the minimum sum that we have come to
	while rowPos < size:
		if sumVar > matrix[rowPos][size - 1]:
			sumVar = matrix[rowPos][size - 1]
			start = i
		rowPos += 1
	
	#initialize more variables
	result = sumVar	
	lastMove = 'none'
	rowPos = start

	#while we are traversing back to the left
	while columnPos != 0:
		
		#if we are at the top-most row in the table
		#find the next appropriate matching value for
		#resultSum and backtrack. Add the number found
		#to the values list and continue
		if rowPos == 0:
			#traverse downwards
			if lastMove != 'up' and matrix[rowPos + 1][columnPos] < matrix[rowPos][columnPos - 1]:
				lastMove = 'down'
				temp = matrix[rowPos + 1][columnPos]
				rowPos += 1
			#traverse to the right
			else:
				lastMove = 'right'
				temp = matrix[rowPos][columnPos - 1]
				columnPos -= 1
			values.append(sumVar - temp)
			sumVar = temp

		#if we are at the bottom most row in the table
		#find the next appropriate matching value for
		#resultSum and backtrack. Add the number found
		#to the values list and continue
		elif rowPos == size - 1:
			#traverse upwards
			if (lastMove != 'down') and matrix[rowPos - 1][columnPos] < matrix[rowPos][columnPos - 1]:
				lastMove = 'up'
				temp = matrix[rowPos - 1][columnPos]
				rowPos -= 1
			#traverse to the right
			else:
				lastMove = 'right'
				temp = matrix[rowPos][columnPos - 1]
				columnPos -= 1
			values.append(sumVar - temp)
			sumVar = temp

		#for any other row in the table
		#find the next appropriate matching value for
		#resultSum and backtrack. Add the number found
		#to the values list and continue
		else:
			#traverse upwards
			if (lastMove != 'down') and matrix[rowPos - 1][columnPos] <= matrix[rowPos + 1][columnPos] and matrix[rowPos - 1][columnPos] <= matrix[rowPos][columnPos - 1]:
				lastMove = 'up'
				temp = matrix[rowPos - 1][columnPos]
				rowPos -= 1
			#traverse downwards
			elif (lastMove != 'up') and matrix[rowPos + 1][columnPos] <= matrix[rowPos - 1][columnPos] and matrix[rowPos + 1][columnPos] <= matrix[rowPos][columnPos - 1]:
				lastMove = 'down'
				temp = matrix[rowPos + 1][columnPos]
				rowPos += 1
			#traverse upwards
			else:
				lastMove = 'right'
				temp = matrix[rowPos][columnPos - 1]
				columnPos -= 1
			#add next value to values list and reassign sumVar as appropriate
			values.append(sumVar - temp)
			sumVar = temp
	#append final vallue to values and return the appropriate
	#output so we can print it
	values.append(sumVar)
	return [result, values[::-1]]

if __name__ == '__main__':
	matrix = readMatrixData(FILE_NAME)
	result = pathSum(matrix)

	sys.stdout.write('Min sum: ' + str(result[0]) + '\nValues: [')
	for i in range(len(result[1]) - 1):
		sys.stdout.write(str(result[1][i]) + ', ')
	sys.stdout.write(str(result[1][-1]) + ']\n')