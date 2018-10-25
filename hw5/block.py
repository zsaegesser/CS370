# Name: Scrable Squares Puzzle Solver
# Course: CS 370
# Professor: Borowski
# Assignment: Assignment 5
# @file block.py
# @author: Aimal Wajihuddin
# 			Zach Saegesser
# 			Ryan Edelstein
#
# I pledge my honor that I have abided by the Stevens Honor System
#							- Aimal Wajihuddin
# 							- Zach Saegesser
# 							- Ryan Edelstein

import numpy as np

class Square:
    #numpy array of the sides
    dt = np.dtype('O')
    sides = np.array([], dtype = dt)
    #1-9 square number
    num = 0

    #constructor
    def __init__(self, newsides, index):
        self.sides = newsides
        self.num = index

    def copy(self):
        return Square(np.copy(self.sides), self.num)

    def rotateSquareClockwise(self):
        return Square(np.roll(self.sides, 1), self.num)

def checkSideMatch(sideNum, sq1, sq2, sq3):
    #sq1, check right to match left on sq3
    #sq2, check bottom to match top on sq3
    #sq3 is the sqare trying to insert
    #checking right on sq1 match left on sq2

    if sideNum == 1:
        if (sq1.sides[1] == "R0" and sq3.sides[3] == "R1") or (sq1.sides[1] == "R1" and sq3.sides[3] == "R0"):
            return True
        elif (sq1.sides[1] == "Y0" and sq3.sides[3] == "Y1") or (sq1.sides[1] == "Y1" and sq3.sides[3] == "Y0"):
            return True
        elif (sq1.sides[1] == "G0" and sq3.sides[3] == "G1") or (sq1.sides[1] == "G1" and sq3.sides[3] == "G0"):
            return True
        elif (sq1.sides[1] == "B0" and sq3.sides[3] == "B1") or (sq1.sides[1] == "B1" and sq3.sides[3] == "B0"):
            return True
        else:
            return False
    elif sideNum == 2: #checking if bottom on sq1 matches top on sq2
        if (sq2.sides[2] == "R0" and sq3.sides[0] == "R1") or (sq2.sides[2] == "R1" and sq3.sides[0] == "R0"):
            return True
        elif (sq2.sides[2] == "Y0" and sq3.sides[0] == "Y1") or (sq2.sides[2] == "Y1" and sq3.sides[0] == "Y0"):
            return True
        elif (sq2.sides[2] == "G0" and sq3.sides[0] == "G1") or (sq2.sides[2] == "G1" and sq3.sides[0] == "G0"):
            return True
        elif (sq2.sides[2] == "B0" and sq3.sides[0] == "B1") or (sq2.sides[2] == "B1" and sq3.sides[0] == "B0"):
            return True
        else:
            return False

    elif sideNum == 3:
        if ((sq2.sides[2] == "R0" and sq3.sides[0] == "R1") or (sq2.sides[2] == "R1" and sq3.sides[0] == "R0")):
            if (sq1.sides[1] == "R0" and sq3.sides[3] == "R1") or (sq1.sides[1] == "R1" and sq3.sides[3] == "R0"):
                return True
            elif (sq1.sides[1] == "Y0" and sq3.sides[3] == "Y1") or (sq1.sides[1] == "Y1" and sq3.sides[3] == "Y0"):
                return True
            elif (sq1.sides[1] == "G0" and sq3.sides[3] == "G1") or (sq1.sides[1] == "G1" and sq3.sides[3] == "G0"):
                return True
            elif (sq1.sides[1] == "B0" and sq3.sides[3] == "B1") or (sq1.sides[1] == "B1" and sq3.sides[3] == "B0"):
                return True
            else:
                return False
        elif ((sq2.sides[2] == "Y0" and sq3.sides[0] == "Y1") or (sq2.sides[2] == "Y1" and sq3.sides[0] == "Y0")):
            if (sq1.sides[1] == "R0" and sq3.sides[3] == "R1") or (sq1.sides[1] == "R1" and sq3.sides[3] == "R0"):
                return True
            elif (sq1.sides[1] == "Y0" and sq3.sides[3] == "Y1") or (sq1.sides[1] == "Y1" and sq3.sides[3] == "Y0"):
                return True
            elif (sq1.sides[1] == "G0" and sq3.sides[3] == "G1") or (sq1.sides[1] == "G1" and sq3.sides[3] == "G0"):
                return True
            elif (sq1.sides[1] == "B0" and sq3.sides[3] == "B1") or (sq1.sides[1] == "B1" and sq3.sides[3] == "B0"):
                return True
            else:
                return False
        elif ((sq2.sides[2] == "G0" and sq3.sides[0] == "G1") or (sq2.sides[2] == "G1" and sq3.sides[0] == "G0")):
            if (sq1.sides[1] == "R0" and sq3.sides[3] == "R1") or (sq1.sides[1] == "R1" and sq3.sides[3] == "R0"):
                return True
            elif (sq1.sides[1] == "Y0" and sq3.sides[3] == "Y1") or (sq1.sides[1] == "Y1" and sq3.sides[3] == "Y0"):
                return True
            elif (sq1.sides[1] == "G0" and sq3.sides[3] == "G1") or (sq1.sides[1] == "G1" and sq3.sides[3] == "G0"):
                return True
            elif (sq1.sides[1] == "B0" and sq3.sides[3] == "B1") or (sq1.sides[1] == "B1" and sq3.sides[3] == "B0"):
                return True
            else:
                return False
        elif ((sq2.sides[2] == "B0" and sq3.sides[0] == "B1") or (sq2.sides[2] == "B1" and sq3.sides[0] == "B0")):
            if (sq1.sides[1] == "R0" and sq3.sides[3] == "R1") or (sq1.sides[1] == "R1" and sq3.sides[3] == "R0"):
                return True
            elif (sq1.sides[1] == "Y0" and sq3.sides[3] == "Y1") or (sq1.sides[1] == "Y1" and sq3.sides[3] == "Y0"):
                return True
            elif (sq1.sides[1] == "G0" and sq3.sides[3] == "G1") or (sq1.sides[1] == "G1" and sq3.sides[3] == "G0"):
                return True
            elif (sq1.sides[1] == "B0" and sq3.sides[3] == "B1") or (sq1.sides[1] == "B1" and sq3.sides[3] == "B0"):
                return True
            else:
                return False
        else:
            return False
    else:
        print("Something went wrong in checking for match")
        return False
		