# Name: Scrable Squares Puzzle Solver
# Course: CS 370
# Professor: Borowski
# Assignment: Assignment 5
# @file puzzlesolver.py
# @author: Aimal Wajihuddin
# 			Zach Saegesser
# 			Ryan Edelstein
#
# I pledge my honor that I have abided by the Stevens Honor System
#							- Aimal Wajihuddin
# 							- Zach Saegesser
# 							- Ryan Edelstein

import sys
import copy
import numpy as np
import block as b
import readFile as r
from itertools import permutations

SOLUTIONS = []

def checkIndex(i,j, arr,sq):
    if i ==0 and j == 0:
        return True
    elif i==0 and j ==1:
        #check match with 0,0 right
        return b.checkSideMatch(1,arr[0][0],None ,sq)
    elif i ==0 and j ==2:
        #check match with 0,1 right
        return b.checkSideMatch(1,arr[0][1],None, sq)
    elif i==1 and j ==0:
        #check match with 0,0 bottom
        return b.checkSideMatch(2,None,arr[0][0], sq)
    elif i==1 and j ==1:
        #check match with 1,0 right and 0,1 bottom
        return b.checkSideMatch(3,arr[1][0], arr[0][1], sq)
    elif i==1 and j ==2:
        #check match with 1,1 right and 0,2 bottom
        return b.checkSideMatch(3,arr[1][1], arr[0][2], sq)
    elif i ==2 and j ==0:
        #check match with 1,0 bottom
        return b.checkSideMatch(2,None, arr[1][0], sq)
    elif i ==2 and j ==1:
        #check match with 2,0 right and 1,1 bottom
        return b.checkSideMatch(3,arr[2][0], arr[1][1], sq)
    elif i ==2 and j ==2:
        #check match with 2,1 right and 1,2 bottom
        return b.checkSideMatch(3,arr[2][1], arr[1][2], sq)
    print("Oh no! My potions are too strong for you warrior. Don't come back until you're ready for my potions...")
    return False

# subfunction of printArr to print the divider line of each row
def divider():
	sys.stdout.write('+--------+--------+--------+\n')

# subfunction of printArr to print the 1st line of each row
def printFirstLineOfRow(row):
	sys.stdout.write('|')
	for square in row:
		sys.stdout.write(str(square.num))
		sys.stdout.write('  ')
		sys.stdout.write(str(square.sides[0]))
		sys.stdout.write('   |')
	sys.stdout.write('\n')

# subfunction of printArr to print the 2nd line of each row
def printSecondLineOfRow(row):
	sys.stdout.write('|')
	for square in row:
		sys.stdout.write(str(square.sides[3]))
		sys.stdout.write('    ')
		sys.stdout.write(str(square.sides[1]))
		sys.stdout.write('|')
	sys.stdout.write('\n')

# subfunction of printArr to print the 3rd line of each row
def printThirdLineOfRow(row):
	sys.stdout.write('|   ')
	sys.stdout.write(str(row[0].sides[2]))
	sys.stdout.write('   |   ')
	sys.stdout.write(str(row[1].sides[2]))
	sys.stdout.write('   |   ')
	sys.stdout.write(str(row[2].sides[2]))
	sys.stdout.write('   |\n')

# function to prettyPrint the solution
def printArr(arr):
	for row in arr:
		divider()
		printFirstLineOfRow(row)
		printSecondLineOfRow(row)
		printThirdLineOfRow(row)
	divider()

# starter function to execute the algorithm
def executeAlgo(squares):
    arr = np.empty((3,3), dtype = "O")
    grid = np.array([[0,0],[0,1],[0,2],[1,0],[1,1],[1,2],[2,0],[2,1],[2,2]])
    algo(arr, grid, squares, 0)

# the algorithm to find the solutions
def algo(arr, grid_arr, squares_left, rec_level):
    debugFlag = False

	# A solution has been found
    if np.size(grid_arr) == 0 or rec_level == 9 or np.size(squares_left) == 0:
        SOLUTIONS.append(arr)
        return
		
    curr_grid = grid_arr[0,:]
    i = curr_grid[0]
    j = curr_grid[1]

    for index, sq in enumerate(squares_left):
        if debugFlag:
            print("Attempting to Insert Sq " + str(sq.num))
            sq.printSquare()
            printArr(arr)
        tempsq = sq.copy()
        if checkIndex(i,j,arr, tempsq):
            if debugFlag:
                print("Insterting Sq " + str(sq.num) + " at (" + str(i) + ", " + str(j) + ") if 1")
            temp = arr.copy()
            temp[i][j] = tempsq.copy()
            algo(temp, np.delete(grid_arr,(0), axis=0), np.delete(squares_left,index), rec_level+1)

        if debugFlag:
            print("Rotating Sq " + str(sq.num))
        tempsq = tempsq.rotateSquareClockwise()
        if checkIndex(i,j,arr,tempsq):
            if debugFlag:
                print("Insterting Sq " + str(sq.num) + " at (" + str(i) + ", " + str(j) + ") if 2")
            temp1 = arr.copy()
            temp1[i][j] = tempsq.copy()
            algo(temp1, np.delete(grid_arr,(0), axis=0), np.delete(squares_left,index), rec_level+1)

        if debugFlag:
            print("Rotating Sq " + str(sq.num))
        tempsq = tempsq.rotateSquareClockwise()
        if checkIndex(i,j,arr,tempsq):
            if debugFlag:
                print("Insterting Sq " + str(sq.num) + " at (" + str(i) + ", " + str(j) + ") if 3")
            temp2 = arr.copy()
            temp2[i][j] = tempsq.copy()
            algo(temp2, np.delete(grid_arr,(0), axis=0), np.delete(squares_left,index), rec_level+1)
        if debugFlag:
            print("Rotating Sq " + str(sq.num))

        tempsq = tempsq.rotateSquareClockwise()
        if checkIndex(i,j,arr,tempsq):
            if debugFlag:
                print("Insterting Sq " + str(sq.num) + " at (" + str(i) + ", " + str(j) + ") if 4")
            temp3 = arr.copy()
            temp3[i][j] = tempsq.copy()
            algo(temp3, np.delete(grid_arr,(0), axis=0), np.delete(squares_left,index), rec_level+1)
        if debugFlag:
            print("Failed to insert Sq " + str(sq.num))
    return

# Method to check duplicates
# Use global variable SOLUTIONS to get all possible solutions
# make easy to read/check strings of solutions
# check for duplicates and make all of them empty strings
# only return matches for remaining solutions
def checkDuplicates():

	myDict = []
	currPerms = []
	seenSolutions = []
	final = []

	for grid in SOLUTIONS:
		currGrid = str(grid[0][0].num) + str(grid[0][1].num) + str(grid[0][2].num) + str(grid[1][0].num) + str(grid[1][1].num) + str(grid[1][2].num) + str(grid[2][0].num) + str(grid[2][1].num) + str(grid[2][2].num)

		currPerms.append(currGrid)
		currPerms.append(currGrid[::-1])
		currPerms.append(currGrid[6] + currGrid[3] + currGrid[0] + currGrid[7] + currGrid[4] + currGrid[1] + currGrid[8] + currGrid[5] + currGrid[2])
		currPerms.append(currGrid[2] + currGrid[5] + currGrid[8] + currGrid[1] + currGrid[4] + currGrid[7] + currGrid[0] + currGrid[3] + currGrid[6])

		myDict.append(currPerms)
		currPerms = []

	myCopy = copy.deepcopy(myDict)

	for v in myDict:
		if v == '':
			continue
		permutation = v[0]
		seenSolutions.append(v)
		for v2 in myDict:
			if permutation in v2:
				myDict[myDict.index(v2)] = ''

	for v in seenSolutions:
		final.append(SOLUTIONS[myCopy.index(v)])

	return final
	
	
if __name__ == '__main__':
	if len(sys.argv) != 2:
		raise Exception('Usage: python puzzlesolver <file>')
	
	f = sys.argv[1]
	executeAlgo(r.getNumpyArrayOfSquares(f))
	finalSolutions = checkDuplicates()
	numSolutions = len(finalSolutions)

	if numSolutions == 0:
		sys.stdout.write('No solution found.\n')
	elif numSolutions == 1:
		sys.stdout.write('1 unique solution found:')
		for sol in finalSolutions:
			sys.stdout.write('\n')
			printArr(sol)
	else:
		sys.stdout.write(str(numSolutions) + ' unique solutions found:')
		for sol in finalSolutions:
			sys.stdout.write('\n')
			printArr(sol)